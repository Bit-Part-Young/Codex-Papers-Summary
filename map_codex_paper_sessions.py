#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_PROJECT_DIR = Path("~/scripts/Codex-Papers-Summary").expanduser()
DEFAULT_CODEX_HOME = Path("~/.codex").expanduser()
DEFAULT_OUTPUT_NAME = "session-summary-mapping.md"
DEFAULT_RENAMED_DIR_NAME = "3-summaries-renamed"
STATE_DIR_NAME = ".map-state"

SESSION_FILE_RE = re.compile(r"rollout-.*-(019[0-9a-f-]+)\.jsonl$")
ABSOLUTE_UPDATED_FILE_RE = re.compile(r"[AM] (.+?/2-summaries/[^\n]+?\.md)")
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
            "and rename them using the final session names. Existing destination "
            "files are kept unchanged."
        ),
    )
    parser.add_argument(
        "--overwrite-renamed",
        action="store_true",
        help=(
            "With --rename, overwrite existing files in 3-summaries-renamed. "
            "Use this to discard manual edits and copy the current source summaries."
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
                # Session logs may have been created on a different computer,
                # where the absolute home directory is not the current one.
                paths.append(project_dir / "2-summaries" / Path(match).name)
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
            # Session logs contain command text as well as command results.  A
            # path mentioned in a past command, test, or deleted file is not a
            # current summary and must not prevent the remaining files mapping.
            if not summary_path.exists():
                continue
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


def state_path_for(summary_path: Path, state_dir: Path) -> Path:
    """Return a state-file path stable across devices and destination renames."""
    source_key = hashlib.sha256(summary_path.name.encode()).hexdigest()
    return state_dir / f"{source_key[:16]}.md"


def legacy_state_path_for(summary_path: Path, state_dir: Path) -> Path:
    """Return the full-hash state path used by earlier versions of this script."""
    source_key = hashlib.sha256(summary_path.name.encode()).hexdigest()
    return state_dir / f"{source_key}.md"


def merge_summary(destination_path: Path, base_path: Path, source_path: Path) -> tuple[str, bool]:
    """Merge source changes into a manually edited destination using Git's 3-way merge."""
    base_text = base_path.read_text(encoding="utf-8")
    source_text = source_path.read_text(encoding="utf-8")
    if source_text.startswith(base_text):
        # Follow-up translations are commonly appended to the source.  Treat a
        # pure append specially so that it remains mergeable even if a manual
        # edit changed the final paragraph of the previous version.
        destination_text = destination_path.read_text(encoding="utf-8")
        return destination_text + source_text[len(base_text) :], False

    result = subprocess.run(
        [
            "git",
            "merge-file",
            "--stdout",
            "--diff3",
            "-L",
            "3-summaries-renamed (manual edits)",
            "-L",
            "previously mapped 2-summaries version",
            "-L",
            "current 2-summaries version",
            str(destination_path),
            str(base_path),
            str(source_path),
        ],
        capture_output=True,
        encoding="utf-8",
    )
    if result.returncode > 1:
        raise RuntimeError(
            f"Unable to merge {destination_path.name}: {result.stderr.strip()}"
        )
    return result.stdout, result.returncode == 1


def rename_summaries(
    mappings: list[SessionMapping], project_dir: Path, overwrite: bool = False
) -> tuple[list[tuple[Path, Path]], list[Path], list[Path], list[Path]]:
    destination_dir = project_dir / DEFAULT_RENAMED_DIR_NAME
    destination_dir.mkdir(parents=True, exist_ok=True)
    state_dir = destination_dir / STATE_DIR_NAME
    state_dir.mkdir(parents=True, exist_ok=True)

    copied: list[tuple[Path, Path]] = []
    skipped: list[Path] = []
    merged: list[Path] = []
    conflicts: list[Path] = []
    for mapping in mappings:
        if not mapping.summary_path.exists():
            raise FileNotFoundError(f"Missing source summary: {mapping.summary_path}")

        destination_name = sanitize_filename(mapping.final_name) + ".md"
        destination_path = destination_dir / destination_name
        state_path = state_path_for(mapping.summary_path, state_dir)
        legacy_state_path = legacy_state_path_for(mapping.summary_path, state_dir)

        if not state_path.exists() and legacy_state_path.exists():
            legacy_state_path.replace(state_path)

        if not destination_path.exists() or overwrite:
            shutil.copy2(mapping.summary_path, destination_path)
            shutil.copy2(mapping.summary_path, state_path)
            copied.append((mapping.summary_path, destination_path))
            continue

        if not state_path.exists():
            # Existing files may contain manual changes made before this feature.
            # There is no safe common ancestor, so preserve the file and start
            # tracking future source changes from the current source version.
            shutil.copy2(mapping.summary_path, state_path)
            skipped.append(destination_path)
            continue

        merged_text, has_conflict = merge_summary(
            destination_path, state_path, mapping.summary_path
        )
        destination_path.write_text(merged_text, encoding="utf-8")
        if has_conflict:
            conflicts.append(destination_path)
            continue

        shutil.copy2(mapping.summary_path, state_path)
        merged.append(destination_path)

    return copied, skipped, merged, conflicts


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
        copied, skipped, merged, conflicts = rename_summaries(
            mappings, project_dir, overwrite=args.overwrite_renamed
        )
        print(f"已复制并重命名 {len(copied)} 个文件到：{project_dir / DEFAULT_RENAMED_DIR_NAME}")
        if skipped:
            print(f"已保留 {len(skipped)} 个已有文件，并已建立后续合并基线")
        if merged:
            print(f"已三方合并 {len(merged)} 个已有文件（保留手动修改）")
        if conflicts:
            print(f"有 {len(conflicts)} 个文件存在合并冲突，请处理其中的冲突标记")

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # pragma: no cover
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
