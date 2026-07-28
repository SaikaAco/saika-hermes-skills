#!/usr/bin/env python3
"""Validate a self-contained burnable visual brief using only the standard library."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import stat
import tempfile

DEFAULT_ROOT = Path.cwd() / "scratch" / "visual-briefs"
MAX_BYTES = 1_500_000
MAX_TTL_SECONDS = 7 * 24 * 60 * 60
PLACEHOLDER = re.compile(r"\{\{[^{}]+\}\}")
FORBIDDEN_TAGS = {"script", "link", "iframe", "object", "embed", "form", "base"}
FORBIDDEN_SCHEMES = ("javascript:", "vbscript:", "data:text/html")


class BriefParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tags: list[str] = []
        self.attrs: list[tuple[str, str, str]] = []
        self.ids: set[str] = set()
        self.local_hrefs: list[str] = []
        self.meta: dict[str, str] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        self.tags.append(tag)
        values = {key.lower(): value or "" for key, value in attrs}
        if values.get("id"):
            self.ids.add(values["id"])
        if tag == "meta" and values.get("name"):
            self.meta[values["name"]] = values.get("content", "")
        for key, value in values.items():
            self.attrs.append((tag, key, value.strip()))
        href = values.get("href", "")
        if href.startswith("#") and len(href) > 1:
            self.local_hrefs.append(href[1:])


def parse_utc(value: str, label: str, errors: list[str]) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        errors.append(f"{label} is not valid ISO-8601 UTC: {value!r}")
        return None
    if parsed.tzinfo is None or parsed.utcoffset() != timezone.utc.utcoffset(parsed):
        errors.append(f"{label} must include UTC timezone")
        return None
    return parsed


def validate(
    path: Path, *, template: bool = False, root: Path = DEFAULT_ROOT
) -> list[str]:
    errors: list[str] = []
    try:
        data = path.read_bytes()
    except OSError as exc:
        return [f"cannot read file: {exc}"]

    if len(data) > MAX_BYTES:
        errors.append(f"file exceeds {MAX_BYTES} bytes")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return ["file is not valid UTF-8"]

    if not text.lstrip().lower().startswith("<!doctype html>"):
        errors.append("missing HTML5 doctype")
    if not template and PLACEHOLDER.search(text):
        errors.append("unresolved template placeholder")
    if re.search(r"@import\s|url\(\s*['\"]?(?:https?:)?//", text, re.I):
        errors.append("CSS loads an external resource")
    if "@media" not in text or "max-width" not in text:
        errors.append("responsive mobile CSS is missing")
    if "@media print" not in text:
        errors.append("print CSS is missing")

    parser = BriefParser()
    try:
        parser.feed(text)
    except Exception as exc:
        errors.append(f"HTML parse failed: {exc}")
        return errors

    forbidden = sorted(FORBIDDEN_TAGS.intersection(parser.tags))
    if forbidden:
        errors.append("forbidden tag(s): " + ", ".join(forbidden))
    if "main" not in parser.tags or "footer" not in parser.tags:
        errors.append("required main/footer structure is missing")

    for tag, key, value in parser.attrs:
        lowered = value.lower().replace("\x00", "")
        if key.startswith("on"):
            errors.append(f"inline event handler is forbidden: {tag}[{key}]")
        if key in {"src", "poster"} and value and not lowered.startswith("data:image/"):
            errors.append(f"non-inline asset is forbidden: {tag}[{key}]={value!r}")
        if key in {"href", "src", "action", "formaction"} and lowered.startswith(FORBIDDEN_SCHEMES):
            errors.append(f"unsafe URL scheme: {tag}[{key}]")
        if key == "href" and value and not (lowered.startswith("https://") or lowered.startswith("#")):
            errors.append(f"source hyperlink must use https:// or a local anchor: {value!r}")

    for anchor in parser.local_hrefs:
        if anchor not in parser.ids:
            errors.append(f"unresolved local anchor: #{anchor}")

    if not template:
        if parser.meta.get("hermes-artifact-kind") != "burnable-visual-brief":
            errors.append("missing burnable visual brief metadata")
        created = parse_utc(parser.meta.get("hermes-created-at", ""), "created-at", errors)
        expires = parse_utc(parser.meta.get("hermes-expires-at", ""), "expires-at", errors)
        if created and expires:
            ttl = (expires - created).total_seconds()
            if ttl <= 0 or ttl > MAX_TTL_SECONDS:
                errors.append("expiry must be after creation and no more than seven days")
        try:
            path.resolve(strict=True).relative_to(root.resolve(strict=False))
        except (OSError, ValueError):
            errors.append(f"final brief must be stored under {root}")
        if os.name == "posix":
            mode = stat.S_IMODE(path.stat().st_mode)
            if mode != 0o600:
                errors.append(f"file mode must be 0600, observed {oct(mode)}")

    return sorted(set(errors))


def self_test() -> None:
    valid = """<!doctype html><html><head>
<meta name='viewport' content='width=device-width'>
<style>@media(max-width:600px){} @media print{}</style></head>
<body><main><section id='x'></section></main><footer></footer></body></html>"""
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "template.html"
        path.write_text(valid, encoding="utf-8")
        assert validate(path, template=True) == []
        path.write_text(valid.replace("</main>", "<script>alert(1)</script></main>"), encoding="utf-8")
        assert any("forbidden tag" in item for item in validate(path, template=True))
        path.write_text(valid.replace("</main>", "<img src='https://example.com/x.png'></main>"), encoding="utf-8")
        assert any("non-inline asset" in item for item in validate(path, template=True))
        path.write_text(valid.replace("</main>", "<a href='http://example.com'>source</a></main>"), encoding="utf-8")
        assert any("source hyperlink must use https" in item for item in validate(path, template=True))
    print("self-test passed")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--template", action="store_true")
    parser.add_argument(
        "--root", type=Path, default=DEFAULT_ROOT,
        help="Allowed visual-brief root (default: ./scratch/visual-briefs)",
    )
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if args.path is None:
        parser.error("path is required unless --self-test is used")
    errors = validate(args.path, template=args.template, root=args.root)
    print(json.dumps({"path": str(args.path), "valid": not errors, "errors": errors}, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
