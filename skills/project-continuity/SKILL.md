---
name: project-continuity
description: "Continue a long academic research project across sessions or models using stable records, explicit decisions, corrections, evidence gaps, and concise handovers."
---

# Project Continuity and Handover

The files are the project memory; the conversation is temporary. Do not rely on hidden memory or assume the next model can inspect earlier chats.

## Cold-start reading order

1. Read `HANDOVER.md` for current state and next actions.
2. Read `project-brief.md` and `project-instructions.md` for settled scope and constraints.
3. Consult the decision and correction registers before making a change that may revisit earlier work.
4. Read the relevant argument map and claim register.
5. Inspect source-ledger entries and underlying sources needed for the immediate task.
6. Read the relevant draft section, glossary entries, finding files, and active adversarial-cycle log.

If a file is missing or inaccessible, report that limitation and continue only where safe. Do not pretend to have read unseen materials.

## Check the handover against the files

A handover is a claim about the project, not proof of it. Before relying on it, confirm that every artefact it says exists (a drafted section, a completed cycle, an updated register) actually exists and contains what is claimed. Report any gap as a correction, not a silent fix.

Check that IDs cited in drafts, the argument map, and the handover resolve to live records and that no superseded record is cited as current. If the repository's `scripts/check_register_refs.py` is available, run it on the project folder.

A record must not claim more than its own text supports: a claim marked `ESTABLISHED` whose support field reads `PARTIAL`, or a section described as verified while its notes list open checks, is an inconsistency to fix.

## One authoritative home

Each substantive decision, correction, source, major claim, and adversarial objection has one canonical record. Other files refer to its stable ID. Handover summarises and points; it does not duplicate complete records. Never reuse an ID or silently erase a resolved/withdrawn record. Mark obsolete entries as superseded and preserve history when it helps explain the current position.

## Before changing files

Identify the target change, affected records, dependent claims and sections, and any authorial decision needed. Do not make a substantive authorial choice on the author's behalf. Recommend options and explain their consequences. If there is enough information to proceed, do so using recorded decisions; do not re-ask questions already settled.

After a substantive change, update the relevant draft, claim/source register, argument map, glossary, decision/correction register, and handover as appropriate. Do not claim a record was updated unless it was actually changed.

## Handover contents

Record project title and date; research question and current thesis; scope/method; current stage; file reading order; authoritative record paths; settled decisions by ID; important corrections and downstream status; unresolved adversarial objections; priority evidence gaps and documents wanted; most recent changes; next three actions; and any assumptions about tool/source access. Keep it short enough to be useful and precise enough for a cold start.
