#!/usr/bin/env python3
"""List a text's fixed facts and compare two versions of it.

Fixed facts are items an edit or translation must not change silently: quotations,
numbers, years and dates, paragraph pinpoints, provisions (art, s, para, §, 第…条),
neutral and report citations, case names, DOIs, and URLs.

Standard library only. Accepts .md, .txt, or .docx (body and footnotes).

Usage:
    python3 scripts/integrity_manifest.py list draft.md
    python3 scripts/integrity_manifest.py diff before.docx after.docx

`diff` exits 1 if any fixed fact disappeared or appeared, else 0. Quotations are compared
only within the same language; for a translation, compare the other categories.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

PATTERNS = {
    "quotation": r"[\"“«「『]([^\"”»」』]{8,}?)[\"”»」』]",
    "doi": r"\b10\.\d{4,9}/[^\s\"<>]+",
    "url": r"https?://[^\s)>\]]+",
    "neutral_citation": r"\[\d{4}\]\s+[A-Z][A-Za-z]*(?:\s+[A-Z][A-Za-z]*)?\s+\d+(?:\s*\([A-Za-z]+\))?",
    "report_citation": r"\(\d{4}\)\s+\d+\s+[A-Z][A-Za-z.]*(?:\s+[A-Z][A-Za-z.]*)*\s+\d+",
    "pinpoint": r"(?:at|para|paras|¶)\s*\[?\d+\]?(?:\s*[-–]\s*\[?\d+\]?)?|\[\d{1,4}\](?=\s*[,.;)])",
    "provision": r"\b(?:art|arts|article|articles|s|ss|section|sections|reg|rule|r|para|sch|cap)\.?\s*\d+[A-Za-z]*(?:\(\w+\))*|§+\s*\d+\w*|第[一二三四五六七八九十百千零〇\d]+[条條款项項章节節]",
    "case_name": r"\b[A-Z][\w.'&-]*(?:\s+[A-Z][\w.'&-]*)*\s+v\.?\s+[A-Z][\w.'&-]*(?:\s+[A-Z][\w.'&-]*)*",
    "date": r"\b\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+\d{4}\b|\b\d{4}-\d{2}-\d{2}\b|\d{4}年\d{1,2}月\d{1,2}日",
    "number": r"(?<![\w.,])(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?%?(?![\w])",
}


def read_text(path: Path) -> str:
    if path.suffix.lower() == ".docx":
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from extract_docx import extract, render  # noqa: E402

        paras, notes = extract(path)
        return render(paras, notes)
    return path.read_text(encoding="utf-8")


def manifest(text: str) -> dict[str, Counter]:
    result = {}
    for name, pattern in PATTERNS.items():
        flags = re.IGNORECASE if name == "provision" else 0
        found = [m.group(1) if m.groups() else m.group(0) for m in re.finditer(pattern, text, flags)]
        result[name] = Counter(" ".join(f.split()) for f in found)
    return result


def cmd_list(path: Path) -> int:
    for name, items in manifest(read_text(path)).items():
        if items:
            print(f"## {name} ({sum(items.values())})")
            for item, n in sorted(items.items()):
                print(f"- {item}" + (f"  ×{n}" if n > 1 else ""))
    return 0


def cmd_diff(before: Path, after: Path) -> int:
    a, b = manifest(read_text(before)), manifest(read_text(after))
    changed = False
    for name in PATTERNS:
        lost, gained = a[name] - b[name], b[name] - a[name]
        if lost or gained:
            changed = True
            print(f"## {name}")
            for item, n in sorted(lost.items()):
                print(f"- missing in {after.name}: {item}" + (f" ×{n}" if n > 1 else ""))
            for item, n in sorted(gained.items()):
                print(f"+ new in {after.name}: {item}" + (f" ×{n}" if n > 1 else ""))
    if not changed:
        print("No change in fixed facts.")
    return 1 if changed else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p_list = sub.add_parser("list")
    p_list.add_argument("file", type=Path)
    p_diff = sub.add_parser("diff")
    p_diff.add_argument("before", type=Path)
    p_diff.add_argument("after", type=Path)
    args = ap.parse_args()
    if args.cmd == "list":
        return cmd_list(args.file)
    return cmd_diff(args.before, args.after)


if __name__ == "__main__":
    sys.exit(main())
