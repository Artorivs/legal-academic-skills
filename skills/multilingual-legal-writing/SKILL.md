---
name: multilingual-legal-writing
description: "Write, revise, or translate scholarship in any language other than British English or between languages, and use foreign-language sources, keeping legal meaning and the terminology of the right legal system, not just the right language."
---

# Multilingual Legal Writing

A language is not a jurisdiction. French may mean France, Belgium, Switzerland, Quebec, or an international court; Chinese may mean the PRC, Hong Kong, Taiwan, or Macau; Spanish, Portuguese, German, and Arabic each span several legal systems. Translate legal effect within a legal system, not words within a language.

## Intake

Before translating or revising, establish:

- source language and the legal system the source belongs to;
- target language, variety, and script, and the legal system and readership the text is for;
- genre and purpose (article, abstract, quotation in a footnote, translated source for analysis, referee response);
- the citation style of the target venue.

If the source or target legal system is unclear and the choice changes terminology, ask. Never infer the legal system from the language alone. Use British English for English unless instructed otherwise.

Then read the language pack in `references/languages/` for each language involved, if one exists. If none does, work from `references/languages/_template.md` and say that no checked pack was available.

## Build the glossary first

For anything longer than a page, list the defined terms, terms of art, institution names, and recurring concepts, and fix one rendering for each before translating. Show the list to the author for long or high-stakes texts, and record agreed choices in the project glossary. Inconsistent rendering of a term across a text is the most common serious failure.

Give each term an equivalence band:

- `E` **established:** a recognised equivalent exists in the target system and is used in the same sense.
- `D` **drift-prone:** a documented equivalent exists but its scope or effect differs (for example, *recours pour excès de pouvoir* and judicial review).
- `N` **no equivalent:** use an explanatory rendering and keep the original term in brackets or italics at first use.

## Preserve legal meaning

- Keep the force of modal terms, burdens, standards, exceptions, legal statuses, and causal or normative claims. Do not turn "may" into "must", a criticism into a holding, a possibility into a finding, or a proposal into current law.
- Never raise the certainty of a source in translation. If the source hedges, the translation hedges.
- Keep names of courts, statutes, and institutions in their official form, with a translation at first use where the readership needs it. Use an official translation where one exists and say so; label unofficial translations of titles as such.
- Do not translate a quotation and present it as the original wording. Quote the original and translate it, or translate and mark it "(author's translation)".
- Where a treaty or statute has several equally authentic language versions, check the other versions before resting an argument on the wording of one.
- Keep numbers, dates, article and paragraph numbers, case names, and citations identical across versions. Compare them before and after; if the repository's `scripts/integrity_manifest.py` is available, use it.

## Scholarly prose

Prefer natural, connected analysis in the target language to literal transfer of syntax. Follow the register of legal scholarship in the target readership, not that of legislation, judgments, or official documents. Avoid that language's formulaic AI prose (each pack lists common tells). Choose terminology by the specified legal system and readership, not by political or linguistic stereotype.

## Working with foreign-language sources

When a source is in a language the author does not read, translate only the passages the argument relies on, mark each translation as such, and keep the original text available for checking. Prefer an official or published translation where one exists, and record which was used. Treat a machine or AI translation of a load-bearing passage as provisional until a reader of the language has checked it.

## Output

Provide the text, then translator's notes:

- the glossary, with equivalence bands;
- terms with no equivalent and the rendering chosen;
- ambiguities in the source that change legal meaning, flagged rather than resolved;
- passages that need review by a reader qualified in the language and legal system, with at least one listed for any high-stakes text.

Do not present stylistic preference as a rule of law. This skill does not produce certified or sworn translations.
