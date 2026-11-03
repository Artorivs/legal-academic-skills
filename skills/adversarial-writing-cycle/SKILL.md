---
name: adversarial-writing-cycle
description: "Run rounds of critique, author response, revision, and retest until the argument holds, or work through real referee reports and draft the response letter. Produces revised text and a response matrix. For a single critical report, use manuscript-review."
---

# Adversarial Writing Cycle

The purpose is not to make one role win or to force the author to abandon a defensible thesis. The purpose is to discover which claims survive informed challenge, which need repair, and which should be narrowed or withdrawn.

## Roles

**Drafting scholar:** develops a coherent version of the author's argument using the supplied research and verified sources. Makes the central claim, premises, inferential steps, and intended contribution visible. Does not hide uncertainties to make the prose sound confident.

**Adversarial reviewer:** evaluates the draft as a demanding, independent critic. Tests the strongest claim rather than a straw man; searches for the best counter-authorities, contrary evidence, omitted premises, doctrinal distinctions, methodological weaknesses, rival explanations, and plausible alternative readings. Does not merely ask for “more nuance” or praise the writing. Does not invent source support. Applies the review dimensions and severity scale of the `manuscript-review` skill, and filters its own objections with that skill's sustainability test before reporting them: an objection that does not survive the author's one-sentence reply, or that a serious scholar would be embarrassed to press, is cut.

**Revising scholar:** answers each material objection. Classifies it as accepted, partly accepted, rejected with reasons, or unresolved. Changes the substance where needed. Where an objection is rejected, provides a reasoned response rather than silently ignoring it.

**Retest reviewer:** checks whether the revised text actually resolves the original objection and whether the revision has introduced new weaknesses. The reviewer must acknowledge when its earlier criticism was mistaken or based on a false premise.

## Cycle

1. Draft the target section or argument from the project brief, argument map, and available evidence.
2. Review the draft. For each objection, identify the exact passage or claim ID, state the problem, explain why it matters, classify severity (`critical`, `major`, `moderate`, `minor`), and specify what would resolve it. Separate factual/legal error from contestable interpretation, methodological concern, and stylistic preference.
3. Prepare a response matrix with one row per substantive objection. Do not merge distinct objections merely to reduce the count.
4. Revise the text and relevant project records. Link changes to objection IDs; preserve a brief account of rejected objections and the reason for rejection.
5. Retest the revision against the same objections before adding new ones. Mark each `resolved`, `partly resolved`, `unresolved`, `withdrawn as mistaken`, or `superseded` with reasons.
6. Repeat until the preset cycle limit is reached or further revision has diminishing value. Default to three full cycles, but do not treat reaching the limit as success.

## External reviews

When the objections come from real referees, an editor, examiners, or co-authors, skip steps 1–2 and start from their text.

1. Identify the master manuscript the response will be made against. If it is unclear which version the reviewers read, ask; a matrix built on the wrong base is unreliable.
2. Extract every request into the response matrix, one row each, with: reviewer, location in the manuscript, the request in the reviewer's own words, type (comment, proposed insertion, deletion, replacement, request for analysis or sources), and any conflict with another reviewer. Do not merge two reviewers' points into one anonymous row. Where a comment's location cannot be matched, mark it `location uncertain` rather than guessing.
3. Default every row to `open`. Do not infer acceptance from a reviewer's seniority or from the editor's tone; the author decides.
4. Flag separately: conflicts between reviewers, requests the editor marked as required, requests that would change the thesis, and requests resting on a misreading.
5. After the author decides, revise and link each change to its row and to its location in the revised manuscript.
6. Draft the response letter: thank briefly, then answer each point in order, quoting or closely summarising the request, saying what changed and where, or explaining respectfully why not. Never claim a change that was not made.

When a report and the manuscript are in different languages, use the `multilingual-legal-writing` skill for the translation of requests and responses.

## Independence and integrity

Where practical, use a separate conversation or model for the reviewer. Give it the research question, draft, relevant primary sources, and review criteria. Do not give it the drafting role's preferred answer or private rationale at first; disclose necessary context after its initial critique. This can reduce anchoring but does not guarantee independence.

A fluent exchange between two AI roles is not source verification. Confirm authorities and quotations separately. Never mark an objection resolved only because the prose has become more elegant. A fundamental evidential gap may require research or a narrower claim, not another rewrite.

## Required deliverables

Produce: revised draft; numbered review report; author response matrix; current unresolved-objection list; changed claim/source/decision/correction records; and a brief statement of what the cycle did and did not establish. Retain a record of important rejected objections. The human author decides the final position.
