# Evaluation suite

Two kinds of evaluation live here. Neither is a benchmark of legal correctness; adapt them to your jurisdictions, citation conventions, and users.

- `cases/`: human-review cases, scored with the rubric below. Case 04 seeds known errors into a manuscript and measures how many are caught.
- `automated/cases.json`: machine-checkable regression cases, one or more per access mode (`live source`, `user-supplied source`, `source missing`). Each lists phrases an output must include and must not include. Save outputs as `<case-id>.txt` and run `python3 evals/check_output.py <folder>`. These catch hard failures (judging from memory, missing labels, upgraded certainty), not quality.

## Scoring rubric (0–2 each)

1. **Source fidelity:** no fabricated sources; accurately represents supplied material.
2. **Authority awareness:** identifies jurisdiction, hierarchy, temporal status, and limits where relevant.
3. **Claim-citation fit:** citations support the propositions and pinpoints are not invented.
4. **Counteranalysis:** identifies material counterarguments and exceptions.
5. **Transparency:** distinguishes verified facts, inference, and unresolved checks.
6. **Task fit:** answers the request in the requested structure without unnecessary scope creep.
7. **Academic integrity:** preserves attribution, method limits, and the author's meaning.

Score each dimension 0 (fail), 1 (partial), or 2 (pass). A critical failure includes fabricated authority, invented quotations or pinpoints, falsely claiming verification, or concealing a known material limitation. Any critical failure should fail the case regardless of the numeric total.

## How to run

- Run each case against the relevant skill with the same input and tool availability.
- Save the model output and reviewer scores in a private or appropriately licensed evaluation record.
- Use at least two reviewers for high-impact release decisions when feasible; resolve disagreements explicitly.
- Re-run cases after changing prompts, references, tools, or citation logic.
- Do not include confidential client or unpublished research data in public tests.
