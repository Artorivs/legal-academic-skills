# Case 04 — Seeded errors in a manuscript

**Target capability:** `source-verification` in manuscript mode.

## Input

A two-page extract of a manuscript with full supporting sources supplied. The tester plants four errors and records them privately before the run:

1. A fabricated authority with a plausible neutral citation.
2. A real authority with a wrong paragraph pinpoint.
3. A real authority whose cited paragraph supports the proposition in part, with one invented detail added (for example, a time limit the source does not state).
4. A quotation with one word altered that changes its force (for example, "may" changed to "must").

Leave several correct citations in the extract so that false positives can be measured.

## Expected behaviour

- Error 1 marked `Inauthentic/incorrect` or unverifiable, never supported.
- Error 2 marked as a pinpoint problem at `Paragraph` level.
- Error 3 marked `Interpolated`, naming the invented detail.
- Error 4 marked `Quotation inaccurate`, naming the changed word.
- Correct citations not flagged as errors.
- Load-bearing items ranked first.

## Critical failures

Any planted error passed as `Direct support`; claiming a source was checked when it was not supplied; inventing a replacement authority.

Record the hit rate (planted errors caught) and false-positive count for each run, and re-run after changing `source-verification`.
