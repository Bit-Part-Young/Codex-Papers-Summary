#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_PROJECT_DIR = Path("~/scripts/Codex-Papers-Summary").expanduser()
DEFAULT_CODEX_HOME = Path("~/.codex").expanduser()
DEFAULT_OUTPUT_NAME = "session-summary-mapping.md"
DEFAULT_RENAMED_DIR_NAME = "3-summaries-renamed"

SESSION_FILE_RE = re.compile(r"rollout-.*-(019[0-9a-f-]+)\.jsonl$")
ABSOLUTE_UPDATED_FILE_RE = re.compile(
    r"[AM] (/Users/sly/scripts/Codex-Papers-Summary/2-summaries/[^\n]+?\.md)"
)
RELATIVE_UPDATED_FILE_RE = re.compile(r"[AM] (2-summaries/[^\n]+?\.md)")


@dataclass(frozen=True)
class SessionMapping:
    session_id: str
    final_name: str
    summary_path: Path
    session_file: Path

    @property
    def summary_name(self) -> str:
        return self.summary_path.name


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Match Codex sessions for ~/scripts/Codex-Papers-Summary with "
            "2-summaries/*.md files, export a Markdown table, and optionally "
            "copy summaries into 3-summaries-renamed using final session names."
        )
    )
    parser.add_argument(
        "--codex-home",
        type=Path,
        default=DEFAULT_CODEX_HOME,
        help="Codex home directory. Default: ~/.codex",
    )
    parser.add_argument(
        "--project-dir",
        type=Path,
        default=DEFAULT_PROJECT_DIR,
        help="Target Codex project directory. Default: ~/scripts/Codex-Papers-Summary",
    )
    parser.add_argument(
        "--output",
        nargs="?",
        const="",
        metavar="OUTPUT_MD",
        help=(
            "Write the mapping as a Markdown file. If no path is given, the file "
            "is saved to <project-dir>/session-summary-mapping.md"
        ),
    )
    parser.add_argument(
        "--rename",
        action="store_true",
        help=(
            "Copy files from 2-summaries into <project-dir>/3-summaries-renamed "
            "and rename them using the final session names."
        ),
    )
    return parser.parse_args()


def load_final_thread_names(session_index: Path) -> dict[str, str]:
    names: dict[str, str] = {}
    with session_index.open("r", encoding="utf-8") as handle:
        for raw_line in handle:
            line = raw_line.strip()
            if not line:
                continue
            item = json.loads(line)
            session_id = item.get("id")
            thread_name = item.get("thread_name")
            if session_id and thread_name:
                # The last occurrence in session_index.jsonl is the final thread name.
                names[session_id] = thread_name
    return names


def iter_session_files(codex_home: Path) -> list[Path]:
    sessions_root = codex_home / "sessions"
    return sorted(sessions_root.rglob("*.jsonl"))


def extract_session_meta(session_file: Path) -> tuple[str | None, str | None]:
    session_id = None
    cwd = None
    with session_file.open("r", encoding="utf-8", errors="ignore") as handle:
        for line in handle:
            if '"type":"session_meta"' not in line:
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                break
            payload = item.get("payload", {})
            session_id = payload.get("session_id") or payload.get("id")
            cwd = payload.get("cwd")
            break

    if session_id is None:
        match = SESSION_FILE_RE.search(session_file.name)
        if match:
            session_id = match.group(1)
    return session_id, cwd


def extract_created_summary_paths(session_file: Path, project_dir: Path) -> list[Path]:
    paths: list[Path] = []
    with session_file.open("r", encoding="utf-8", errors="ignore") as handle:
        for line in handle:
            for match in ABSOLUTE_UPDATED_FILE_RE.findall(line):
                paths.append(Path(match))
            for match in RELATIVE_UPDATED_FILE_RE.findall(line):
                paths.append(project_dir / match)
    return sorted(set(paths))


def build_mappings(codex_home: Path, project_dir: Path) -> list[SessionMapping]:
    session_index = codex_home / "session_index.jsonl"
    if not session_index.exists():
        raise FileNotFoundError(f"Missing session index: {session_index}")

    final_names = load_final_thread_names(session_index)
    target_cwd = str(project_dir.resolve())
    mappings: list[SessionMapping] = []

    for session_file in iter_session_files(codex_home):
        session_id, cwd = extract_session_meta(session_file)
        if cwd != target_cwd or not session_id:
            continue

        summary_paths = extract_created_summary_paths(session_file, project_dir)
        if not summary_paths:
            continue

        final_name = final_names.get(session_id)
        if not final_name:
            continue

        for summary_path in summary_paths:
            mappings.append(
                SessionMapping(
                    session_id=session_id,
                    final_name=final_name,
                    summary_path=summary_path,
                    session_file=session_file,
                )
            )

    return mappings


def validate_mappings(mappings: list[SessionMapping], summary_dir: Path) -> None:
    seen_summary: dict[str, SessionMapping] = {}
    duplicate_summaries: list[str] = []

    for mapping in mappings:
        existing = seen_summary.get(mapping.summary_name)
        if existing and existing.session_id != mapping.session_id:
            duplicate_summaries.append(mapping.summary_name)
        else:
            seen_summary[mapping.summary_name] = mapping

    if duplicate_summaries:
        duplicates = ", ".join(sorted(set(duplicate_summaries)))
        raise RuntimeError(f"Found summaries created by multiple sessions: {duplicates}")

    current_summaries = {path.name for path in summary_dir.glob("*.md")}
    mapped_summaries = set(seen_summary)
    missing = sorted(current_summaries - mapped_summaries)
    extra = sorted(mapped_summaries - current_summaries)

    if missing:
        raise RuntimeError(
            "These summary files were not matched to any session: "
            + ", ".join(missing)
        )
    if extra:
        raise RuntimeError(
            "These mapped summaries do not exist in 2-summaries: " + ", ".join(extra)
        )


def sanitize_filename(name: str) -> str:
    replacements = {
        "/": "／",
        "\\": "＼",
        ":": "：",
        "*": "＊",
        "?": "？",
        '"': "＂",
        "<": "＜",
        ">": "＞",
        "|": "｜",
    }
    sanitized = "".join(replacements.get(char, char) for char in name).strip()
    sanitized = re.sub(r"\s+", " ", sanitized)
    return sanitized or "untitled-session"


def build_markdown(mappings: list[SessionMapping]) -> str:
    lines = [
        "# Session 与摘要文件对应表",
        "",
        f"- 找到的 sessions 数目：{len(mappings)}",
        "",
        "| session_id | session 最终名称 | 原始 md 文件名 | session 日志 |",
        "|---|---|---|---|",
    ]

    for mapping in sorted(mappings, key=lambda item: item.session_id):
        session_log = str(mapping.session_file)
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{mapping.session_id}`",
                    escape_pipes(mapping.final_name),
                    escape_pipes(mapping.summary_name),
                    f"`{session_log}`",
                ]
            )
            + " |"
        )

    return "\n".join(lines) + "\n"


def escape_pipes(text: str) -> str:
    return text.replace("|", "\\|")


def write_output(markdown: str, output_arg: str | None, project_dir: Path) -> Path | None:
    if output_arg is None:
        return None

    if output_arg == "":
        output_path = project_dir / DEFAULT_OUTPUT_NAME
    else:
        output_path = Path(output_arg).expanduser()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown, encoding="utf-8")
    return output_path


def rename_summaries(mappings: list[SessionMapping], project_dir: Path) -> list[tuple[Path, Path]]:
    destination_dir = project_dir / DEFAULT_RENAMED_DIR_NAME
    destination_dir.mkdir(parents=True, exist_ok=True)

    copied: list[tuple[Path, Path]] = []
    for mapping in mappings:
        if not mapping.summary_path.exists():
            raise FileNotFoundError(f"Missing source summary: {mapping.summary_path}")

        destination_name = sanitize_filename(mapping.final_name) + ".md"
        destination_path = destination_dir / destination_name
        shutil.copy2(mapping.summary_path, destination_path)
        copied.append((mapping.summary_path, destination_path))

    return copied


def main() -> int:
    args = parse_args()
    codex_home = args.codex_home.expanduser().resolve()
    project_dir = args.project_dir.expanduser().resolve()
    summary_dir = project_dir / "2-summaries"

    if not summary_dir.exists():
        raise FileNotFoundError(f"Missing summary directory: {summary_dir}")

    mappings = build_mappings(codex_home=codex_home, project_dir=project_dir)
    validate_mappings(mappings, summary_dir)

    markdown = build_markdown(mappings)
    print(markdown, end="")
    print(f"找到的 sessions 数目：{len(mappings)}")

    output_path = write_output(markdown, args.output, project_dir)
    if output_path:
        print(f"Markdown 表格已保存到：{output_path}")

    if args.rename:
        copied = rename_summaries(mappings, project_dir)
        print(f"已复制并重命名 {len(copied)} 个文件到：{project_dir / DEFAULT_RENAMED_DIR_NAME}")

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # pragma: no cover
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
