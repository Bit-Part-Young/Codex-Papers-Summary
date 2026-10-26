#!/usr/bin/env python3
"""Copy 2-summaries files under their final Codex / ChatGPT Work session names.

Codex Desktop and ChatGPT Work both keep their session logs in ~/.codex
(sessions/**/rollout-*.jsonl, older ones compressed to .jsonl.zst), and both
record the final thread names in ~/.codex/session_index.jsonl.
"""

import argparse
import filecmp
import json
import os
import re
import shutil
import subprocess
from pathlib import Path


PROJECT = Path(__file__).resolve().parent
SUMMARIES = PROJECT / "2-summaries"
RENAMED = PROJECT / "3-summaries-renamed"
CODEX = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
PREFIX = "文献总结 - "
# A summary counts as created by a session only if the session added it
# (FileChange "add", which covers apply_patch), wrote it with ``cat > file`` or
# renamed it with ``mv old file``. Mere mentions, e.g. in ``ls`` output of
# later sessions, do not count.
WRITE_RE = re.compile(
    r"(?:^|&&|;)\s*(?:cat\s+>(?!>)|mv\s+(?:'[^']*'|\"[^\"]*\"|\S+)\s+)"
    r"\s*(['\"]?)([^'\"\s]*2-summaries/[^'\"\n]+?\.md)\1",
    re.M,
)


def read_lines(log):
    if log.suffix == ".zst":
        result = subprocess.run(["zstd", "-dcq", str(log)], capture_output=True, check=True)
        return result.stdout.decode("utf-8", "ignore").splitlines()
    return log.read_text(encoding="utf-8", errors="ignore").splitlines()


def final_names():
    names = {}
    with (CODEX / "session_index.jsonl").open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                item = json.loads(line)
                names[item["id"]] = item.get("thread_name", "")  # last entry wins
    return names


def session_info(log):
    lines = read_lines(log)
    meta = json.loads(lines[0]).get("payload", {}) if lines else {}
    if meta.get("cwd") != str(PROJECT):
        return None, set()

    names = set()
    for line in lines:
        try:
            payload = json.loads(line).get("payload", {})
        except json.JSONDecodeError:
            continue
        item = payload.get("item") if isinstance(payload, dict) else None
        if not isinstance(item, dict):
            continue
        if item.get("type") == "FileChange":
            for path, change in (item.get("changes") or {}).items():
                if isinstance(change, dict) and change.get("type") == "add":
                    names.add(path)
        elif item.get("type") == "CommandExecution":
            command = item.get("command")
            script = command[-1] if isinstance(command, list) and command else ""
            names.update(match.group(2) for match in WRITE_RE.finditer(str(script)))

    paths = {SUMMARIES / Path(name).name for name in names if Path(name).parent.name == SUMMARIES.name}
    return meta.get("id"), {path for path in paths if path.suffix == ".md" and path.is_file()}


def mappings():
    if not CODEX.is_dir() or not SUMMARIES.is_dir():
        raise RuntimeError("Codex session records or 2-summaries directory not found")

    names = final_names()
    logs = sorted(CODEX.glob("sessions/**/*.jsonl*")) + sorted(CODEX.glob("archived_sessions/*.jsonl*"))
    result, creators = [], {}
    for log in logs:
        session_id, paths = session_info(log)
        title = names.get(session_id, "").strip()
        for path in paths:
            creators[path] = title
        if not title.startswith(PREFIX):
            continue
        if len(paths) != 1:
            print(f"Skipped {session_id} ({title}): expected one source file, found {len(paths)}")
            continue
        source = next(iter(paths))
        target = RENAMED / f"{title.replace('/', '_')}.md"
        result.append((source, target))
    return result, creators


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="show mappings without copying")
    parser.add_argument("--force", action="store_true", help="overwrite targets whose content differs from the source")
    args = parser.parse_args()

    pairs, creators = mappings()
    sources = [source for source, _ in pairs]
    targets = [target for _, target in pairs]
    if len(set(sources)) != len(sources) or len(set(targets)) != len(targets):
        raise RuntimeError("Multiple sessions map to the same source or target")

    if not args.dry_run:
        RENAMED.mkdir(exist_ok=True)
    copied, differing = 0, []
    for source, target in pairs:
        if target.exists() and filecmp.cmp(source, target, shallow=False):
            continue
        if target.exists() and not args.force:
            differing.append((source, target))
            continue
        if not args.dry_run:
            shutil.copy2(source, target)
        copied += 1
        print(f"{source.name} -> {target.name}")

    unmatched = sorted(set(SUMMARIES.glob("*.md")) - set(sources))
    for path in unmatched:
        creator = f" (session title: {creators[path]})" if path in creators else ""
        print(f"Unmatched source: {path.name}{creator}")
    for source, target in differing:
        note = "source is newer, merge by hand" if source.stat().st_mtime > target.stat().st_mtime else "edited copy"
        print(f"Kept ({note}; --force overwrites): {target.name}")
    action = "Would copy" if args.dry_run else "Copied"
    print(f"{len(pairs)} mapped, {action.lower()} {copied}, {len(differing)} differing, {len(unmatched)} unmatched")


if __name__ == "__main__":
    main()
