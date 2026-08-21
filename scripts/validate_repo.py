#!/usr/bin/env python3
"""Validate ppstack's public inventory and portability contract."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "skills"
ALLOWED_STATUSES = {"included", "adapted", "excluded", "pending"}
BANNED_PATTERNS = {
    ".cursor path": re.compile(r"(?:~?/)?\.cursor/", re.IGNORECASE),
    "Cursor question API": re.compile(r"\bAskQuestion\b"),
    "Cursor worker type": re.compile(r"\bsubagent_type\b"),
    "hard-coded model slug": re.compile(r"\b(?:grok|claude|gpt)-[\w.-]+", re.IGNORECASE),
    "pstack model rule": re.compile(r"pstack-models", re.IGNORECASE),
    "pstack personal mode": re.compile(r"poteto", re.IGNORECASE),
    "Cursor-specific reviewer": re.compile(r"Comment Sicko", re.IGNORECASE),
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("missing opening frontmatter fence")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise ValueError("missing closing frontmatter fence") from error
    result = {}
    for line in lines[1:end]:
        match = re.match(r"^([a-zA-Z][\w-]*):\s*(.*)$", line)
        if match:
            result[match.group(1)] = match.group(2).strip().strip('"\'')
    return result


def validate() -> list[str]:
    errors: list[str] = []
    selection = load_json(ROOT / "selection.json")["skills"]
    lock = load_json(ROOT / "upstream.lock.json")

    if set(selection) != set(lock["skills"]):
        missing = sorted(set(lock["skills"]) - set(selection))
        extra = sorted(set(selection) - set(lock["skills"]))
        if missing:
            errors.append("Unclassified locked skills: " + ", ".join(missing))
        if extra:
            errors.append("Classifications absent from lock: " + ", ".join(extra))

    for upstream_name, item in selection.items():
        status = item.get("status")
        if status not in ALLOWED_STATUSES:
            errors.append(f"{upstream_name}: invalid status {status!r}")
        if not item.get("reason"):
            errors.append(f"{upstream_name}: missing reason")
        if status in {"included", "adapted"} and not item.get("localName"):
            errors.append(f"{upstream_name}: selected skill missing localName")

    expected_public = {
        item["localName"]
        for item in selection.values()
        if item["status"] in {"included", "adapted"}
    }
    actual_public = {
        path.parent.name for path in PUBLIC.glob("*/SKILL.md") if path.is_file()
    }
    if missing := sorted(expected_public - actual_public):
        errors.append("Missing public skills: " + ", ".join(missing))
    if extra := sorted(actual_public - expected_public):
        errors.append("Unexpected public skills: " + ", ".join(extra))

    for skill_file in sorted(PUBLIC.glob("*/SKILL.md")):
        try:
            metadata = frontmatter(skill_file)
        except ValueError as error:
            errors.append(f"{skill_file.relative_to(ROOT)}: {error}")
            continue
        folder = skill_file.parent.name
        if metadata.get("name") != folder:
            errors.append(
                f"{skill_file.relative_to(ROOT)}: name {metadata.get('name')!r} does not match folder"
            )
        if not metadata.get("description"):
            errors.append(f"{skill_file.relative_to(ROOT)}: missing description")

    for path in sorted(PUBLIC.rglob("*")):
        if not path.is_file() or path.suffix not in {".md", ".sh", ".tsv"}:
            continue
        text = path.read_text(encoding="utf-8")
        for label, pattern in BANNED_PATTERNS.items():
            if match := pattern.search(text):
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"{path.relative_to(ROOT)}:{line}: {label}")

    updater = ROOT / "maintainer-skills" / "update-ppstack" / "SKILL.md"
    if not updater.is_file():
        errors.append("Missing maintainer update skill")
    elif "internal: true" not in updater.read_text(encoding="utf-8"):
        errors.append("Maintainer update skill must declare metadata.internal: true")

    if any(ROOT.rglob("plugin.json")):
        errors.append("Plugin manifests are not allowed")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("ppstack validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
