---
name: argument-and-language-check
description: "Check a passage, abstract, or short section for the quality of its argument (claim, reasons, evidence, warrant, objections) and its language (task, coherence, vocabulary, grammar): find the problems, score them, correct the text, and show how to improve. For a full referee-style report on a whole manuscript, use manuscript-review."
---

# Argument and Language Check

Sense what is wrong, say why, fix it, and show the writer how to avoid it next time. Works on anything from a paragraph to a short section, in a draft by the author or by the model itself.

The two references hold the standards:

- `references/argument-model.md`: the parts of an argument, kinds and functions of claim, kinds of evidence, standard form, validity and strength, organising claims across paragraphs, and a symptom-to-repair table.
- `references/language-rubric.md`: a nine-band scorecard on four criteria (task and position; coherence and cohesion; lexical resource; grammatical range and accuracy), modelled on the structure of the IELTS Writing band descriptors and rewritten for legal scholarship.
- `references/rubric-crosswalk.md`: the writing criteria of TOEFL, GRE, Cambridge, PTE, the CEFR grid, AP English Language, the AAC&U VALUE rubric, Goethe-Zertifikat, TestDaF and DALF, mapped to the kit's criteria.

## Before starting

If no text was supplied (only a placeholder or a description), ask for the passage in one line and stop, answering in the same line any direct question the user asked (for example, about exam scores; see *Output*).

## Choose the depth and scope

Decide from the request and the length of the text; do not ask.

| Depth | Use when | Gives |
|---|---|---|
| **Quick** | The text is one paragraph or shorter, or the user says "quick", "just fix", or "improve the English" | Bottom line, up to three findings, corrected passage |
| **Standard** | The text is several paragraphs, or the user asks to "check", "assess" or "score" it | Everything in *Output* |
| **Teaching** | The user wants to learn, or says they write in a second language | Standard, plus each recurring pattern with a rule and two corrected examples from the text |

Lens: if the user names a test or framework (TOEFL, GRE, Cambridge, PTE, CEFR, AP, VALUE, Goethe, TestDaF, DALF), score the language with that rubric's own criterion names and scale from `rubric-crosswalk.md` instead of the default four, and say that the result is a lens, not that test's score. For a text in French or German with no lens named, use the DALF C1 or Goethe-Zertifikat C1 criteria; for another language with no test listed, use the CEFR grid.

Scope: "the English", "grammar", "language" → **language only**. "The argument", "the reasoning", "the logic" → **argument only**. Otherwise both. Depth sets which parts appear; scope then removes the parts that do not apply. State depth and scope in a few words at the top, so the user can ask for another.

**Keep it in proportion.** Excluding the corrected passage, aim for about 150 words at quick depth and no more than about 600 at standard depth, whatever the length of the text; for a long text, report the most damaging findings and say how many lesser ones were left out. Say each problem once: the scorecard gives the band and the fix, and the findings do not repeat it.

## 1. Sense: read the passage as argument

1. Say in one sentence what the passage is for (its job in the larger piece, if known).
2. Rewrite its argument in standard form (`argument-model.md` §4): premises above the line, claim below, implicit premises added and marked *[implicit]*. Supply only the implicit premises the conclusion actually needs, at most two or three; an implicit premise must be one the writer is plausibly relying on, not a weakness invented to be criticised.
3. Name the kind of claim (§2) and the kind of each piece of evidence (§3).
4. Check each part with its test: the claim is arguable; each reason passes the challenge and because tests; evidence is the right kind and passes its tests; the warrant would be accepted by the intended reader or is backed; the qualifier matches the support; the strongest objection is met.
5. Judge the step: valid or strong, and how strong. Look for a counterexample.
6. Check whether the passage argues at all, or only describes or explains (§6), and whether it synthesises sources or only summarises them (§7).
7. For a section or introduction of several paragraphs, make a reverse outline (§7): one line per paragraph stating its claim and function, labelled general, narrowing or specific, with the positive-to-critical turn located. Where a paragraph makes several distinct claims, or the paragraphs are one or two sentences long, outline sentence by sentence instead. In an introduction, a missing turn means the thesis has no stated gap to fill: report it as a finding and mark the place in the corrected text.

Do not verify sources here. Where a finding depends on what an authority says, mark it `[SUPPORT TO CHECK]` and point to `source-verification`. Do not assess support from memory.

## 2. Sense: read the passage as language

Score each criterion in `language-rubric.md` on its nine bands, with one short quoted phrase that decided the score. Errors that change legal meaning (a wrong modal, the scope of a negation, *and* for *or*) weigh more than errors of form.

For a language other than British English, apply the same criteria with the relevant pack in the `multilingual-legal-writing` skill.

## 3. Diagnose

List findings in order of what most damages the passage. For each: the quoted words, the problem in plain terms, its effect on the reader, and the repair. Use the symptom table in `argument-model.md` §8 for argument faults. Keep each finding to two or three lines.

Before reporting, cut any finding the author could dismiss in one sentence, and any that a serious scholar would be embarrassed to press (the sustainability test of `manuscript-review`).

## 4. Correct

Give the complete corrected passage, not fragments. Rules:

- Keep the author's position: its direction and subject stay the same. Where the support is too thin for the claim as stated, narrow the scope or the qualifier ("all tribunals" to "tribunals deciding rights"; "must" to "should") and say so. Never strengthen a claim, and never reverse it. If no honest narrowing is available, keep the claim, mark it, and say what support it needs.
- Keep quotations, citations, pinpoints, numbers and dates exactly as they were.
- Supply a missing reason or warrant only where the passage's own material supports it; otherwise insert `[REASON NEEDED: …]` or `[SUPPORT NEEDED: …]`. When more than two `NEEDED` markers are needed (`[SUPPORT TO CHECK]` markers do not count), the passage is not ready for correction: give the corrected language, keep the markers, and list what the author must supply.
- Write in the kit's style: British English by default; connectives that state the real relation instead of "Moreover… Furthermore… In addition"; no "first… second… third…" enumeration; cross-references only where the reader needs them (the full rules are in `academic-legal-drafting`).

## 5. Improve

End with what to practise: the two or three patterns most worth fixing across the writer's other work, each with one rule and, in teaching depth, two corrected examples from this text.

## Output

1. **Bottom line** in two sentences: the passage's main strength and the one change that would improve it most.
2. **Argument** in standard form (and the reverse outline, for a multi-paragraph text), with the kind of claim and whether the step is valid or how strong it is. No separate table of parts: each problem goes in the findings.
3. **Language scorecard**: one row per criterion with the band, one quoted phrase, and the fix.
4. **Findings**, most damaging first, argument and language together; each two or three lines.
5. **Corrected passage.**
6. **For you to decide or check**: only what the author must supply, choose or verify.
7. **What to practise**: two or three patterns.

Quick depth: 1, 4 (up to three findings) and 5, plus the claim and its main reason in one line when the argument is in scope. Within any depth, language only drops 2 and 6; argument only drops 3 and 7.

**If asked for an IELTS, TOEFL, GRE or other exam score:** say plainly that this check cannot give one and its bands do not convert to one, because it uses the rubric's structure with its own descriptors for legal writing, and only an official examiner can award an exam band. Then offer the check itself.

## Limits

A score is a structured judgment, not a measurement, and never an IELTS or other exam score. A passage can score well and still rest on a source that does not say what it is cited for. Fluency is not soundness.
