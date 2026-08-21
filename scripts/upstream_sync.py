#!/usr/bin/env python3
"""Inspect and record the pstack revision from which ppstack is derived."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator


ROOT = Path(__file__).resolve().parents[1]
SELECTION_PATH = ROOT / "selection.json"
LOCK_PATH = ROOT / "upstream.lock.json"
UPSTREAM_REPOSITORY = "https://github.com/cursor/plugins.git"
UPSTREAM_BRANCH = "main"
UPSTREAM_PATH = "pstack/skills"


def run(*args: str, cwd: Path | None = None) -> str:
    result = subprocess.run(
        args,
        cwd=cwd,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout.strip()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_skills_dir(source: Path) -> Path:
    candidates = (
        source / UPSTREAM_PATH,
        source / "pstack" / "skills",
        source / "skills",
        source,
    )
    for candidate in candidates:
        if candidate.is_dir() and any(candidate.glob("*/SKILL.md")):
            return candidate.resolve()
    raise ValueError(f"Could not find upstream skills below {source}")


def git_root(path: Path) -> Path:
    return Path(run("git", "rev-parse", "--show-toplevel", cwd=path))


def git_commit(path: Path) -> str:
    return run("git", "rev-parse", "HEAD", cwd=git_root(path))


def hash_directory(path: Path) -> str:
    digest = hashlib.sha256()
    for file_path in sorted(item for item in path.rglob("*") if item.is_file()):
        relative = file_path.relative_to(path).as_posix().encode()
        digest.update(relative)
        digest.update(b"\0")
        digest.update(file_path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def inventory(skills_dir: Path) -> dict[str, str]:
    return {
        directory.name: hash_directory(directory)
        for directory in sorted(skills_dir.iterdir())
        if directory.is_dir() and (directory / "SKILL.md").is_file()
    }


def classification_errors(upstream_names: set[str]) -> list[str]:
    selection = load_json(SELECTION_PATH)["skills"]
    selected_names = set(selection)
    errors = []
    if missing := sorted(upstream_names - selected_names):
        errors.append("Unclassified upstream skills: " + ", ".join(missing))
    if extra := sorted(selected_names - upstream_names):
        errors.append("Classifications absent upstream: " + ", ".join(extra))

    public_names = {
        path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")
    }
    expected_public = {
        item.get("localName", upstream_name)
        for upstream_name, item in selection.items()
        if item["status"] in {"included", "adapted"}
    }
    if missing := sorted(expected_public - public_names):
        errors.append("Selected skills missing locally: " + ", ".join(missing))
    if extra := sorted(public_names - expected_public):
        errors.append("Public skills missing from selection: " + ", ".join(extra))
    return errors


@contextmanager
def source_checkout(source: str | None) -> Iterator[tuple[Path, str]]:
    if source:
        source_path = Path(source).expanduser().resolve()
        yield resolve_skills_dir(source_path), git_commit(source_path)
        return

    with tempfile.TemporaryDirectory(prefix="ppstack-upstream-") as temp_name:
        checkout = Path(temp_name) / "cursor-plugins"
        run(
            "git",
            "clone",
            "--depth",
            "1",
            "--filter=blob:none",
            "--sparse",
            "--branch",
            UPSTREAM_BRANCH,
            UPSTREAM_REPOSITORY,
            str(checkout),
        )
        run("git", "sparse-checkout", "set", "pstack", cwd=checkout)
        yield resolve_skills_dir(checkout), git_commit(checkout)


def check() -> int:
    lock = load_json(LOCK_PATH)
    remote = run(
        "git", "ls-remote", UPSTREAM_REPOSITORY, f"refs/heads/{UPSTREAM_BRANCH}"
    ).split()[0]
    recorded = lock["commit"]
    if remote == recorded:
        print(f"Current: {recorded}")
        return 0
    print(f"Update available: {recorded} -> {remote}")
    return 1


def audit(source: str | None) -> int:
    lock = load_json(LOCK_PATH)
    with source_checkout(source) as (skills_dir, commit):
        current = inventory(skills_dir)

    previous = lock["skills"]
    current_names = set(current)
    previous_names = set(previous)
    added = sorted(current_names - previous_names)
    removed = sorted(previous_names - current_names)
    changed = sorted(
        name for name in current_names & previous_names if current[name] != previous[name]
    )
    unchanged = sorted(
        name for name in current_names & previous_names if current[name] == previous[name]
    )

    print(f"Recorded commit: {lock['commit']}")
    print(f"Inspected commit: {commit}")
    print("Added: " + (", ".join(added) if added else "none"))
    print("Removed: " + (", ".join(removed) if removed else "none"))
    print("Changed: " + (", ".join(changed) if changed else "none"))
    print(f"Unchanged: {len(unchanged)}")

    errors = classification_errors(current_names)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1 if added or removed or changed or errors or commit != lock["commit"] else 0


def record(source: str | None) -> int:
    with source_checkout(source) as (skills_dir, commit):
        current = inventory(skills_dir)

    errors = classification_errors(set(current))
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    payload = {
        "schemaVersion": 1,
        "repository": UPSTREAM_REPOSITORY,
        "branch": UPSTREAM_BRANCH,
        "path": UPSTREAM_PATH,
        "commit": commit,
        "skills": current,
    }
    LOCK_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Recorded {len(current)} upstream skills at {commit}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("check", help="Compare the lock with upstream main")
    for command in ("audit", "record"):
        child = subparsers.add_parser(command)
        child.add_argument(
            "--source",
            help="Existing cursor/plugins checkout, pstack directory, or skills directory",
        )
    args = parser.parse_args()
    if args.command == "check":
        return check()
    if args.command == "audit":
        return audit(args.source)
    return record(args.source)


if __name__ == "__main__":
    raise SystemExit(main())
