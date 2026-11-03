#!/usr/bin/env python3
"""Check saved model outputs against evals/automated/cases.json.

Save each output as <case-id>.txt in one folder, then run:
    python3 evals/check_output.py path/to/outputs

A case with no saved output is reported as MISSING. Exits 1 if any case fails.
Standard library only.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

CASES = Path(__file__).resolve().parent / "automated" / "cases.json"


def check(case: dict, text: str) -> list[str]:
    low = text.lower()
    problems = []
    for group in case.get("must_include_any", []):
        if not any(p.lower() in low for p in group):
            problems.append(f"missing any of {group}")
    for phrase in case.get("must_not_include", []):
        if phrase.lower() in low:
            problems.append(f"contains prohibited {phrase!r}")
    return problems


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    folder = Path(sys.argv[1])
    cases = json.loads(CASES.read_text(encoding="utf-8"))["cases"]
    failed = 0
    for case in cases:
        out = folder / f"{case['id']}.txt"
        if not out.exists():
            print(f"MISSING {case['id']} ({case['skill']})")
            continue
        problems = check(case, out.read_text(encoding="utf-8"))
        if problems:
            failed += 1
            print(f"FAIL    {case['id']}: " + "; ".join(problems))
        else:
            print(f"PASS    {case['id']}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
