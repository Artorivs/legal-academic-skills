---
name: manuscript-consolidation
description: "Restructure a whole manuscript or long section: remove repetition, reorder sections, standardise terms, fix transitions and cross-references, or meet a word limit by moving material to footnotes. For drafting or rewriting individual passages, use academic-legal-drafting."
---

# Manuscript Consolidation

Consolidation is structural and argumentative work, not simply shortening the text.

## Protect the fixed facts

Before editing, list the manuscript's fixed facts: every quotation, number, date, case name, citation, pinpoint, and statutory or treaty provision. After editing, compare the list against the revised text. Any change to a fixed fact is reverted and flagged unless the author approved it or the document itself proves the original was a slip (for example, its own table contradicts the text); in that case, record the correction and its basis. Never correct silently. If the repository's `scripts/integrity_manifest.py` is available, use it to extract and compare.

## Diagnose before editing

Read the whole relevant unit and identify its function in the paper. Mark repeated propositions, duplicative literature summaries, sections that perform the same task, terms used inconsistently, unsupported leaps, paragraphs whose evidence does not support their conclusion, unnecessary headings, missing transitions, and qualifications that are repeated because the underlying structure is unclear.

Distinguish harmful repetition from deliberate recurrence that reminds the reader of a key premise or links sections. Distinguish a removable sentence from a premise needed by a later inference. Do not remove adverse authority, methodological limits, or a qualification merely because it makes the thesis harder to state.

## Rebuild

Propose a sequence in which each section has a distinct argumentative job. Combine material when it genuinely serves the same proposition; split it when distinct claims require different reasoning or evidence. Move background to the point where it becomes necessary. Make transitions state the actual relation between sections, not generic signposting. Standardise terms according to the glossary and project decisions. Remove numbered enumeration of points and cross-references the reader does not need, under the principles in the `academic-legal-drafting` skill; after restructuring, check that every remaining cross-reference still points to the right place.

## Relegation to footnotes (word limits)

When the task is to meet a word limit for body text, move material rather than delete it.

- **Target:** the fraction of body words the author names; default 25%. Land within about two percentage points, or stop short and say why if more would break the argument.
- **The body must stay self-sufficient.** A reader who never looks at a footnote must still follow every step. Protected: thesis statements, steps in the chain of reasoning, definitions used later, primary evidence on which a conclusion rests, and topic sentences.
- **Good candidates:** qualifications not needed for the inference, compressed history, placement within the literature, source criticism, secondary examples, counterexamples already answered, and methodological asides.
- **Move near-verbatim.** Edit only what the passage needs to stand alone as a note (resolve pronouns, drop an opening connective). Do not compress or improve the author's prose.
- **Citations travel with their sentences.** Never strand a citation from the claim it supports.
- **Repair seams** in the body: transitions, back-references ("as noted above"), and enumerations ("three reasons").
- Keep a ledger of each move (first words, word count, category, destination note) and report the achieved fraction.

## Deliverables

Provide the revised text, a concise change log, significant deletions/mergers, any changes in meaning or emphasis, and a list of evidential or authorial questions that prevent a clean resolution. If altering files, reread the current version before writing and edit the intended parts rather than overwriting unrelated user changes. Preserve stable IDs and citation references until the final clean-copy pass.
