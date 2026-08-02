#!/usr/bin/env python3
"""Validate the public Hermes skill tap using only the Python standard library."""

from __future__ import annotations

from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
REQUIRED_FIELDS = ("name", "description", "version", "author", "license")
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "GitHub token": re.compile(r"\bgh[oprsu]_[A-Za-z0-9]{20,}\b"),
    "OpenAI-style secret": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
}
PRIVATE_MARKERS = (
    "/Users/",
    "@Saika_",
    "@hermes_saika",
    "7382087947",
)


def parse_frontmatter(text: str, path: Path) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError(f"{path}: frontmatter closing delimiter is missing")
    raw = text[4:end]
    body = text[end + 5 :]
    fields: dict[str, str] = {}
    for line in raw.splitlines():
        if not line or line[0].isspace() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields, body


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file() or skill_md.is_symlink():
        return [f"{skill_dir}: regular SKILL.md is required"]

    text = skill_md.read_text(encoding="utf-8")
    try:
        fields, body = parse_frontmatter(text, skill_md)
    except ValueError as exc:
        return [str(exc)]

    for field in REQUIRED_FIELDS:
        if not fields.get(field):
            errors.append(f"{skill_md}: missing frontmatter field {field!r}")
    if fields.get("name") != skill_dir.name:
        errors.append(
            f"{skill_md}: frontmatter name {fields.get('name')!r} "
            f"does not match directory {skill_dir.name!r}"
        )
    if fields.get("version") and not SEMVER.fullmatch(fields["version"]):
        errors.append(f"{skill_md}: version is not semantic: {fields['version']!r}")
    if not body.strip():
        errors.append(f"{skill_md}: body is empty")
    if text.count("```") % 2:
        errors.append(f"{skill_md}: unbalanced fenced code blocks")

    package_root = skill_dir.resolve()
    for path in skill_dir.rglob("*"):
        if path.is_symlink():
            errors.append(f"{path}: symlinks are not allowed in published packages")
            continue
        if not path.is_file():
            continue
        try:
            package_text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for marker in PRIVATE_MARKERS:
            if marker in package_text:
                errors.append(f"{path}: private marker found: {marker!r}")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(package_text):
                errors.append(f"{path}: possible {label} found")
        if path.suffix.lower() != ".md":
            continue
        for raw_target in MARKDOWN_LINK.findall(package_text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("#", "https://", "http://", "mailto:")):
                continue
            relative = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not relative:
                continue
            if Path(relative).is_absolute() or relative.startswith("~"):
                errors.append(f"{path}: package link must be relative: {target!r}")
                continue
            resolved = (path.parent / relative).resolve()
            if not resolved.is_relative_to(package_root):
                errors.append(f"{path}: package link escapes skill directory: {target!r}")
            elif not resolved.exists():
                errors.append(f"{path}: package link target is missing: {target!r}")
    return errors


def main() -> int:
    errors: list[str] = []
    if not SKILLS.is_dir():
        errors.append(f"missing skills directory: {SKILLS}")
        skill_dirs: list[Path] = []
    else:
        skill_dirs = sorted(path for path in SKILLS.iterdir() if path.is_dir())
        if not skill_dirs:
            errors.append("skills directory contains no packages")

    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Validated {len(skill_dirs)} skill package(s):")
    for skill_dir in skill_dirs:
        print(f"- {skill_dir.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
