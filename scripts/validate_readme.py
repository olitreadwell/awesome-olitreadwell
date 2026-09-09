#!/usr/bin/env python3
"""Validate links in readme.md and civic-tech.md.

Flags malformed markdown links, duplicate URLs, and relative URLs. Skips
HTML comments and in-page fragment links (the table of contents). Runs in
CI on every pull request.

Usage:
    python3 scripts/validate_readme.py
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
FILES = [ROOT / "readme.md", ROOT / "civic-tech.md"]

LINK_RE = re.compile(r"\[([^\]]+)\] ?\(([^)]+)\)")
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)


def check_file(path: Path) -> list[str]:
    """Return a list of problems found in one markdown file."""
    errors: list[str] = []
    text = COMMENT_RE.sub("", path.read_text(encoding="utf-8"))
    urls: list[str] = []

    for lineno, raw in enumerate(text.splitlines(), 1):
        stripped = raw.lstrip(" \t")
        if not stripped.startswith("- "):
            continue
        if stripped.startswith("- [") and not LINK_RE.match(stripped[2:]):
            errors.append(f"{path.name}:{lineno}: malformed link: {raw.strip()}")
        match = LINK_RE.match(stripped[2:])
        if not match:
            continue
        url = match.group(2).strip()
        if url.startswith("#"):
            continue
        urls.append(url)
        if not urlparse(url).scheme:
            errors.append(f"{path.name}:{lineno}: no URL scheme: {url}")

    for url, count in Counter(urls).items():
        if count > 1:
            errors.append(f"{path.name}: duplicate link ({count}x): {url}")
    return errors


def main() -> int:
    """Run all checks and return a process exit code."""
    errors: list[str] = []
    for path in FILES:
        errors.extend(check_file(path))
    if errors:
        print(f"{len(errors)} problem(s) found:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"OK: {len(FILES)} files parse cleanly")
    return 0


if __name__ == "__main__":
    sys.exit(main())
