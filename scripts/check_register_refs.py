#!/usr/bin/env python3
"""Check that record IDs cited across a project folder resolve to live register entries.

A record is defined by the first cell of a table row in a Markdown file (for example the
`CL-001` row in claim-register.md). Every other occurrence of an ID is a reference.
Reports references to undefined IDs, IDs defined more than once, and references to
records whose row is marked SUPERSEDED or WITHDRAWN.

Recognised prefixes follow the templates: CL (claims), SRC (sources), D (decisions),
C (corrections), AO (adversarial objections), DW (documents wanted). Add more with --prefix.

Standard library only.

Usage:
    python3 scripts/check_register_refs.py path/to/project
    python3 scripts/check_register_refs.py path/to/project --prefix EX --prefix Q

Exits 1 if any problem is found, else 0.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

DEFAULT_PREFIXES = ["CL", "SRC", "D", "C", "AO", "DW"]
PLACEHOLDER = re.compile(r"\[[A-Z /-]+\]")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder", type=Path)
    ap.add_argument("--prefix", action="append", default=[], help="extra ID prefix to recognise")
    args = ap.parse_args()

    prefixes = sorted(set(DEFAULT_PREFIXES + args.prefix), key=len, reverse=True)
    id_re = re.compile(r"\b(?:" + "|".join(map(re.escape, prefixes)) + r")-\d{2,}\b")

    defined: dict[str, list[str]] = defaultdict(list)
    retired: set[str] = set()
    references: list[tuple[str, int, str, bool]] = []

    files = sorted(p for p in args.folder.rglob("*.md") if ".git" not in p.parts)
    if not files:
        print(f"No Markdown files found under {args.folder}.", file=sys.stderr)
        return 2

    for path in files:
        rel = str(path.relative_to(args.folder))
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            cells = [c.strip() for c in line.strip().strip("|").split("|")] if line.lstrip().startswith("|") else []
            scan = re.sub(r"`[^`]*`", lambda m: " " * len(m.group(0)), line)  # IDs in code spans are examples
            matches = list(id_re.finditer(scan))
            if cells and id_re.fullmatch(cells[0]) and not PLACEHOLDER.search(line):
                row_id = cells[0]
                defined[row_id].append(f"{rel}:{lineno}")
                if re.search(r"\b(SUPERSEDED|WITHDRAWN)\b", line, re.IGNORECASE):
                    retired.add(row_id)
                matches = matches[1:]  # the first match is the definition itself
            mentions_retirement = bool(re.search(r"supersed|withdr", line, re.IGNORECASE))
            for m in matches:
                references.append((rel, lineno, m.group(0), mentions_retirement))

    problems = 0
    for rid, places in sorted(defined.items()):
        if len(places) > 1:
            problems += 1
            print(f"DUPLICATE {rid}: defined at {', '.join(places)}")
    for rel, lineno, rid, mentions_retirement in references:
        if rid not in defined:
            problems += 1
            print(f"UNDEFINED {rid}: referenced at {rel}:{lineno}")
        elif rid in retired and not mentions_retirement:
            problems += 1
            print(f"RETIRED   {rid}: referenced at {rel}:{lineno} (record is superseded or withdrawn)")

    print(f"{len(defined)} records, {len(references)} references, {problems} problem(s).")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
