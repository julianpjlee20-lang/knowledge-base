#!/usr/bin/env python3
"""Read-only validator for Andy's Obsidian / PARA vault.

This script checks structure and metadata only. It never writes, moves, deletes,
or auto-fixes files.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ALLOWED_ROOT_DIRS = {
    "00-Inbox",
    "01-Projects",
    "02-Areas",
    "03-Resources",
    "04-Archives",
}

ALLOWED_ROOT_FILES = {
    "00-Index.md",
    "AGENTS.md",
    "CLAUDE.md",
    "README.md",
    ".gitignore",
}

ALLOWED_HIDDEN_ROOT_DIRS = {
    ".git",
    ".claude",
    ".obsidian",
}

FORBIDDEN_ROOT_DIRS = {
    "claude",
    "hermes",
    "codex",
    "agent-output",
    "knowledge-base",
    "People",
    "01-People",
    "Admin",
    "04-Admin",
}

REQUIRED_ROOT_DIRS = ALLOWED_ROOT_DIRS
REQUIRED_INDEXES = [
    "00-Index.md",
    "01-Projects/README.md",
    "02-Areas/README.md",
    "03-Resources/README.md",
    "04-Archives/README.md",
]

REQUIRED_FRONTMATTER_FIELDS = {"created", "updated", "type", "status", "tags", "related"}
VALID_TYPES = {"project", "area", "resource", "archive", "inbox", "log"}
VALID_STATUSES = {"active", "draft", "reference", "archived", "needs-triage"}
GOVERNANCE_FILES = {"AGENTS.md", "CLAUDE.md"}
SKIP_DIRS = {".git", ".obsidian", ".trash"}

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
FIELD_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$")


@dataclass
class Finding:
    level: str  # ERROR or WARN
    path: str
    message: str


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def iter_markdown(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        yield path


def parse_frontmatter(text: str) -> dict[str, str] | None:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("-"):
            continue
        field_match = FIELD_RE.match(line)
        if field_match:
            key, value = field_match.groups()
            fields[key.strip()] = value.strip()
    return fields


def validate_root(root: Path) -> list[Finding]:
    findings: list[Finding] = []

    for required in sorted(REQUIRED_ROOT_DIRS):
        path = root / required
        if not path.is_dir():
            findings.append(Finding("ERROR", required, "Missing required PARA root folder"))

    for index in REQUIRED_INDEXES:
        path = root / index
        if not path.is_file():
            findings.append(Finding("ERROR", index, "Missing required index/README file"))

    for child in sorted(root.iterdir(), key=lambda p: p.name.lower()):
        name = child.name
        if child.is_dir():
            if name in FORBIDDEN_ROOT_DIRS:
                findings.append(Finding("ERROR", name, "Forbidden root folder exists"))
            elif name.startswith("."):
                if name not in ALLOWED_HIDDEN_ROOT_DIRS:
                    findings.append(Finding("WARN", name, "Unexpected hidden root folder"))
            elif name not in ALLOWED_ROOT_DIRS:
                findings.append(Finding("ERROR", name, "Unexpected top-level folder; strict PARA allows only 00-Inbox/ to 04-Archives/"))
        elif child.is_file():
            if name.startswith("."):
                if name not in ALLOWED_ROOT_FILES:
                    findings.append(Finding("WARN", name, "Unexpected hidden root file"))
            elif name not in ALLOWED_ROOT_FILES:
                findings.append(Finding("WARN", name, "Unexpected top-level file"))

    return findings


def expected_type_for_path(path: Path, root: Path) -> str | None:
    parts = path.relative_to(root).parts
    if not parts:
        return None
    first = parts[0]
    if first == "00-Inbox":
        return "inbox"
    if first == "01-Projects":
        return "project"
    if first == "02-Areas":
        return "area"
    if first == "03-Resources":
        return "resource"
    if first == "04-Archives":
        return "archive"
    return None


def validate_markdown(root: Path) -> tuple[list[Finding], int]:
    findings: list[Finding] = []
    count = 0

    for path in sorted(iter_markdown(root), key=lambda p: rel(p, root).lower()):
        count += 1
        rp = rel(path, root)
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append(Finding("ERROR", rp, "Markdown file is not valid UTF-8"))
            continue

        if not text.strip():
            findings.append(Finding("WARN", rp, "Markdown file is empty"))
            continue

        fields = parse_frontmatter(text)
        if fields is None:
            findings.append(Finding("WARN", rp, "Missing YAML frontmatter"))
            continue

        missing = sorted(REQUIRED_FRONTMATTER_FIELDS - fields.keys())
        if missing:
            findings.append(Finding("WARN", rp, f"Frontmatter missing fields: {', '.join(missing)}"))

        note_type = fields.get("type", "").strip().strip('"\'')
        status = fields.get("status", "").strip().strip('"\'')

        if note_type and note_type not in VALID_TYPES:
            findings.append(Finding("WARN", rp, f"Unknown frontmatter type: {note_type}"))
        if status and status not in VALID_STATUSES:
            findings.append(Finding("WARN", rp, f"Unknown frontmatter status: {status}"))

        expected = expected_type_for_path(path, root)
        if expected and note_type and note_type != expected:
            # Governance files are allowed to remain resources even at repo root.
            if path.name in GOVERNANCE_FILES and note_type == "resource":
                pass
            # README/index files may describe their container; warn only for clear mismatches.
            elif path.name.lower() == "readme.md" and note_type in VALID_TYPES:
                pass
            else:
                findings.append(Finding("WARN", rp, f"Frontmatter type '{note_type}' differs from folder-implied type '{expected}'"))

    return findings, count


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only PARA/Obsidian vault validator")
    parser.add_argument("root", nargs="?", default=".", help="Vault root directory; defaults to current directory")
    parser.add_argument("--strict-warnings", action="store_true", help="Exit non-zero when WARN findings exist")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"ERROR: vault root does not exist or is not a directory: {root}", file=sys.stderr)
        return 2

    findings = validate_root(root)
    md_findings, md_count = validate_markdown(root)
    findings.extend(md_findings)

    errors = [f for f in findings if f.level == "ERROR"]
    warnings = [f for f in findings if f.level == "WARN"]

    if findings:
        print("Vault validation findings:\n")
        for f in findings:
            print(f"[{f.level}] {f.path}: {f.message}")
        print()

    print(f"Checked {md_count} markdown files")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if errors:
        print("❌ Vault validation failed")
        return 1
    if warnings and args.strict_warnings:
        print("❌ Vault validation failed because --strict-warnings was set")
        return 1

    if warnings:
        print("⚠️ Vault validation passed with warnings")
    else:
        print("✅ Vault validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
