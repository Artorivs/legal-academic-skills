# Changelog

Notable changes to this project are recorded here. Follow a consistent release format and link releases to their tags where available.

## 0.1.0 Unreleased - 2024-06-10

### Added

- Supplemental compatibility guidance for plugin and portable skill distribution.
- Legal and academic research quality-control reference.
- Initial citation-fidelity, adverse-authority, and manuscript-integrity evaluation cases.
- Basic skill structure tests and a standard-library validation script.
- GitHub Actions workflow for structural validation.
- Contribution and security reporting guidance.

### Notes

- These additions are starter materials and have not been validated against every existing skill or target platform.

## 0.1.1 — 2024-06-11

### Added

- Initial plugin and marketplace manifests (.claude-plugin/).
- Initial agents/: legal-manuscript-editor, legal-research-reviewer.

## 0.1.2 — 2024-06-19

### Changed

- README now leads with plugin installation.
- .agents/skills is now symlinked to skills/

### Removed

- Root `.plugin` stub (unrecognised by Claude Code and out of date).
- README-SUPPLEMENTAL.md.

## 0.3.0 — 2026-11-16

Easier to start with, and a new workflow for checking and improving argument and language.

### Added

- `argument-and-language-check`: finds, scores, corrects and teaches. Argument checked in standard form against a shared argument model (claim, reason, evidence, warrant, backing, qualifier, rebuttal; kinds of claim and evidence; validity and strength; a symptom-to-repair table). Language scored on four criteria in nine bands, modelled on the structure of the IELTS Writing band descriptors and rewritten for legal scholarship. Functional claims, general-to-specific organisation, synthesis over summary and the positive-to-critical turn, from Link's *Scientific Writing for Publication*. Quick, standard and teaching depths.
- `docs/how-it-works.md`: Mermaid diagrams of routing, the workflows across a project, shared standards, the argument-and-language check, the adversarial cycle and project records, each with its design rationale.
- `argument-and-language-check`: a rubric crosswalk to TOEFL, GRE, Cambridge C1/C2, PTE, the CEFR written assessment grid, AP English Language, the AAC&U VALUE rubric, Goethe-Zertifikat C1, TestDaF and DALF C1, usable as scoring lenses (never as official scores), with a separate register-and-genre row where those rubrics have one.
- Evaluation case 05 and automated cases for the new workflow.
- Test that the installer refuses to overwrite the canonical skills.

### Changed

- README leads with a three-step start, a "What do you want to do?" table in plain words, a guide to reading the labels, and how much of the kit each size of project needs. Install detail moved lower.
- Quick prompts regrouped by goal, each naming its workflow so it works in Projects that do not load skills.
- Project instructions, router and `project-continuity`: the author need not name workflows; every answer opens with a plain bottom line; author decisions are asked one at a time with a recommendation first.
- `argument-mapping`, `academic-legal-drafting`, `manuscript-review` and `adversarial-writing-cycle` use the shared argument model; drafting self-checks before delivering; review can score language with the rubric.
- `SKILL_INDEX.md` names the five most-used workflows; `templates/README-project.md` says which templates each size of project needs.

### Fixed

- `scripts/install-agent-skills.sh` no longer deletes the canonical skills when run with its old default target, `.agents/skills`, which is a symlink to `skills/`. It now takes a target directory and refuses the canonical one.

## 0.2.0 — 2026-11-03

Consolidates overlapping skills (15 → 13) and adds new methods. Invocations of removed skill names must be updated; see "Renamed and merged".

### Renamed and merged

- `citation-audit` merged into `source-verification` (now with a source mode and a manuscript mode).
- `critical-peer-review` and `final-manuscript-audit` merged into the new `manuscript-review` (desk review, peer review, pre-submission audit).
- `bilingual-legal-writing` renamed `multilingual-legal-writing` and generalised to any language pair, with per-language packs (Chinese, French, and a template).

### Added

- `source-verification`: access modes; no-source verification queue; claim salience; `Interpolated` and `Quotation inaccurate` support labels; Existence / Content / Paragraph verification levels; document-identity checks; bibliographic metadata rule. One label vocabulary now shared with the templates.
- `manuscript-review`: sustainability filter for findings; rhetorical-fairness labels; hidden-text screen for third-party manuscripts; one severity scale (`critical`, `major`, `moderate`, `minor`) used across the kit.
- `research-planning`: mode for assessing an existing thesis (novelty, nonobviousness, utility, soundness; preemption map; claim-type tests).
- `adversarial-writing-cycle`: external-reviews mode for referee reports and response letters; reviewer applies the `manuscript-review` filter.
- `manuscript-consolidation`: fixed-fact protection; relegation-to-footnotes mode for word limits.
- `legal-authority-analysis`: ambiguity families for legislative and treaty text; institution-pack template.
- `literature-synthesis`: fairness labels and multilingual search record.
- `project-continuity`: disk-versus-claim check and record-consistency check.
- `anticipatory-analysis`: rules for writing coding questions for bodies of decisions or legislation.
- Scripts (standard library only): `extract_docx.py`, `integrity_manifest.py`, `check_register_refs.py`, `hidden_text_check.py`, `build_bundle.py`.
- Evaluations: seeded-error case; machine-checkable regression cases with `evals/check_output.py`.

### Changed

- Agents now defer to the skills instead of restating their procedures.
- Source ledger gains access mode, verification level, authority weight, and later treatment; claim register gains salience.
- `PROJECT_UPLOAD_BUNDLE.md` is now generated by `scripts/build_bundle.py` and includes skill reference files.
- Router covers `anticipatory-analysis`, which it previously omitted.
- Every skill description now states where the skill stops and which neighbouring skill to use instead; `SKILL_INDEX.md` adds a stage table and a "Telling similar skills apart" table, and the router uses the same boundaries.
- `academic-legal-drafting`: principles against numbered enumeration in prose (except the article's own principal proposed model) and against unnecessary cross-references; applied in `manuscript-consolidation`, `manuscript-review`, and the project instructions.
