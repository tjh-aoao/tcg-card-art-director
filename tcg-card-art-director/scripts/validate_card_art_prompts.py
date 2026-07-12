#!/usr/bin/env python3
"""Validate clean card-art prompts inside Markdown files.

Checks only fenced code blocks. This keeps prose free to mention rules,
card names, or examples while enforcing clean final prompt lines.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


FORBIDDEN_PATTERNS = [
    (r"\bSUBJECT\s*:", "field label SUBJECT"),
    (r"\bGAMEPLAY EVENT\s*:", "field label GAMEPLAY EVENT"),
    (r"\bENVIRONMENT\s*:", "field label ENVIRONMENT"),
    (r"\bCOMPOSITION CAMERA\s*:", "field label COMPOSITION CAMERA"),
    (r"\bSTYLE MEDIUM\s*:", "field label STYLE MEDIUM"),
    (r"\bPALETTE MATERIAL LIGHT\s*:", "field label PALETTE MATERIAL LIGHT"),
    (r"\bCARD READABILITY\s*:", "field label CARD READABILITY"),
    (r"\bQUALITY\s*:", "field label QUALITY"),
    (r"--ar\b|--raw\b|--s\b|--c\b|--v\b|--style\b|--no\b|--sref\b|--oref\b|--iw\b", "model parameter"),
    (r"::", "Midjourney multi-prompt/text weight"),
    (r"\bZone War\b", "project-internal English name"),
    (r"\bRush Duel\b|\bYu-Gi-Oh\b|\bMagic: The Gathering\b|\bPokemon\b", "third-party named card-game style"),
    (r"\bmasterpiece\b|\bbest quality\b|\bultra-detailed\b|\bepic\b|\bstunning\b|\bgorgeous\b", "vague prestige word"),
]

DEFAULT_INTERNAL_TERMS = [
    "域能",
    "域灵",
    "共鸣",
    "痕迹",
    "机降",
    "行风",
    "绿林",
    "正义式",
    "悲悯式",
    "奉献式",
]


def iter_code_blocks(text: str):
    in_block = False
    start_line = 0
    lines: list[str] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        if line.startswith("```"):
            if in_block:
                yield start_line, lineno, "\n".join(lines)
                in_block = False
                lines = []
            else:
                in_block = True
                start_line = lineno
                lines = []
            continue
        if in_block:
            lines.append(line)


def validate(path: Path, internal_terms: list[str]) -> int:
    text = path.read_text(encoding="utf-8")
    findings: list[str] = []
    compiled = [(re.compile(pattern, re.IGNORECASE), label) for pattern, label in FORBIDDEN_PATTERNS]
    term_patterns = [(re.compile(re.escape(term), re.IGNORECASE), f"internal term {term}") for term in internal_terms]

    for start, _end, block in iter_code_blocks(text):
        for offset, line in enumerate(block.splitlines(), start=1):
            if not line.strip():
                continue
            lineno = start + offset
            for pattern, label in compiled + term_patterns:
                if pattern.search(line):
                    findings.append(f"{path}:{lineno}: {label}: {line.strip()}")

    if findings:
        print("\n".join(findings))
        print(f"\nFAILED: {len(findings)} prompt issue(s) found.")
        return 1

    print(f"OK: no prompt hygiene issues found in {path}")
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Validate clean TCG card-art prompts in Markdown.")
    parser.add_argument("markdown", help="Markdown file to validate")
    parser.add_argument(
        "--internal-term",
        action="append",
        default=[],
        help="Additional internal proper noun or rules term to forbid inside prompt code blocks.",
    )
    parser.add_argument(
        "--no-default-internal-terms",
        action="store_true",
        help="Do not check the built-in Chinese project terms.",
    )
    args = parser.parse_args(argv)

    path = Path(args.markdown)
    if not path.exists():
        print(f"Missing file: {path}", file=sys.stderr)
        return 2

    terms = [] if args.no_default_internal_terms else list(DEFAULT_INTERNAL_TERMS)
    terms.extend(args.internal_term)
    return validate(path, terms)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
