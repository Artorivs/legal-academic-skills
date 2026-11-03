---
name: source-verification
description: "Verify legal, academic, empirical, and archival sources and test whether each supports the exact proposition it is cited for, either for one source before relying on it or across a whole manuscript's footnotes, quotations, pinpoints, and bibliography."
---

# Source Verification

Treat a citation as a claim requiring verification, not as proof in itself. A source can be authentic yet fail to support the proposition made from it, and a complete-looking footnote is not evidence of support.

## Choose the mode

- **Source mode:** one source, or a small set, before relying on it in research or drafting.
- **Manuscript mode:** every material proposition and footnote in a draft, including quotations, pinpoints, short forms, and bibliography.

Both modes use the same checks and the same labels.

## State the access mode first

Record which applies, per source:

- `live source`: retrieved in this session through search, a database, a connector, or a fetched page.
- `user-supplied source`: text, file, or extract supplied by the user.
- `source missing`: not available.

With no source, produce a verification queue only: the proposition, the citation, and the exact check needed. Never assess support, holdings, quotations, pinpoints, or current status from memory, however familiar the authority seems.

## Procedure

1. **Extract** each material proposition and its citation. Split compound sentences so each sub-claim is checked on its own; a sentence can be half right.
2. **Rate salience:** `load-bearing` (the argument turns on it), `supporting`, or `illustrative`. Spend effort in that order.
3. **Fix identity** before content. Disambiguate trial from appeal judgments, interlocutory from final decisions, merits from reparations or costs, admissibility from merits, original from consolidated or amended text, and an advance or provisional version from the final. Use `references/source-identity.md` for the per-type checklist.
4. **Choose the verification level the claim needs:**
   - `Existence`: the document, number, date, and issuing body are real and correctly stated.
   - `Content`: the source holds or says, in substance, what the draft says.
   - `Paragraph`: the cited paragraph or page contains the proposition.
   A pinpoint or a quotation requires `Paragraph`. If checking stopped short of the level the claim needs, soften the claim or flag it.
5. **Compare** the source passage and its context with the proposition. Record what the source expressly establishes, what inference the draft adds, and any contrary or qualifying material.
6. **Check quotations** character by character, including ellipses, brackets, emphasis, and omissions that change meaning.
7. **Check status and time:** subsequent history, appeal, overruling, amendment, repeal, treaty status, reservations, and version in force at the relevant date.
8. **Search for the best contrary authority or evidence** for each load-bearing proposition, not only for support.
9. **In manuscript mode, check form last:** footnote order, short forms, cross-references, repeated citations, and bibliography consistency. Apply OSCOLA or another style only when the user or target publication selects it; otherwise label the style provisional.
10. **Report** corrections ordered by risk: fabricated or wrong references first, then misleading support, then status problems, then form.

## Labels

Use separate fields; do not compress them into one score.

- **Source status:** `Inspected`, `Partly inspected`, `Lead only`, `Unavailable`, `Inauthentic/incorrect`.
- **Verification level reached:** `Existence`, `Content`, `Paragraph`.
- **Claim support:**
  - `Direct support`
  - `Partial support`: supports part; the draft overstates or omits a condition.
  - `Inference required`: the draft draws a step the source does not take.
  - `Interpolated`: the source exists and partly supports the claim, but the draft adds plausible detail the source does not contain. This is the characteristic failure of AI-assisted drafts; name the added detail.
  - `Quotation inaccurate`
  - `Contradicted`
  - `Not addressed`
  - `Not yet assessed`
- **Salience:** `load-bearing`, `supporting`, `illustrative`.
- **Confidence:** a short note on what remains uncertain.

`Not found` is not `Contradicted`. A failed search establishes only that the specified search did not find an item. Do not use `Verified` to mean that every interpretation based on the source is true; preserve disputed readings as disputed.

## Remediation follows salience

- Load-bearing and below standard: the argument cannot proceed on it. Repair, replace with a checked source, or narrow the thesis.
- Supporting and below standard: repair where practicable, or retain with a visible qualification.
- Illustrative and below standard: cut it rather than rebuild the argument around it.

Never silently substitute another authority without checking that it supports the same proposition.

## Output

For source mode, give a short record per source in the shape of `templates/source-ledger.md`.

For manuscript mode, use a table with columns: ID; passage/claim; salience; current citation; access mode; source status; level reached; claim support; proposed correction; remaining uncertainty. Then summarise dependency risk: arguments resting on unsupported or interpolated propositions, citations repeatedly misused for the same point, and authorities cited for the wrong doctrine.

## Non-negotiable rules

- Never invent a case, treaty article, statutory section, quotation, author, title, pinpoint, DOI, URL, date, volume, issue, page range, or other bibliographic detail.
- Never fill a metadata field the source did not return. An incomplete but accurate reference is better than a complete but false one. Leave a visible marker: `[SOURCE TO VERIFY]`, `[PINPOINT TO VERIFY]`, `[PAGES TO VERIFY]`, `[SUPPORT NEEDED]`.
- Do not imply that an original was read when only an abstract, search result, snippet, or secondary quotation was seen.
- Do not classify a source as supporting or contrary from its title or snippet alone.
- For substantial work, record search terms, databases, and the date searched.
