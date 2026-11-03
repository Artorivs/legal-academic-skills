# Legal Academic Skills

A skill kit for academic legal research and writing. It ships as a **Claude Code plugin**, as portable **Agent Skills** (`SKILL.md` workflows) for other runtimes, and as a consolidated **upload bundle** for AI Projects that do not natively load skills.

The kit is designed for administrative law, human rights, law and society, and public international law. It also supports doctrinal, comparative, theoretical, historical, empirical, socio-legal, and interdisciplinary work.

> **Human responsibility.** These workflows help structure research, drafting, and checking. They do not certify that any output is legally or academically correct. Verify every authority, quotation, and proposition yourself before relying on it.

## Choose your install route

### A. Claude Code plugin (recommended)

In Claude Code, add this repository as a marketplace and install the plugin:

```zsh
/plugin marketplace add Artorivs/legal-academic-skills
/plugin install legal-academic-skills@legal-academic-skills
```

Skills are namespaced by the plugin, for example `legal-academic-skills:source-verification`. The plugin also provides two agents, `legal-manuscript-editor` and `legal-research-reviewer`.

To try it from a local clone without installing:

```zsh
git clone https://github.com/Artorivs/legal-academic-skills.git
claude --plugin-dir ./legal-academic-skills
```

Claude Cowork and the Claude desktop app also support plugins; check Anthropic's current documentation for how to add a GitHub marketplace or upload a zip of this repository.

### B. Native Agent Skills (other runtimes)

Each skill is a directory whose entry point is `SKILL.md`, following the open [Agent Skills format](https://agentskills.io/specification). For an agent or runtime that follows this convention, copy the chosen skill directories from `skills/` into that runtime's documented skill directory (for example a project-local `.agents/skills/` or `.claude/skills/` location). Keep each skill directory intact.

- `skills/` is the canonical source.
- `.agents/skills` is a symbolic link to `../skills`, provided for tools that discover skills there. On Windows, Git may check it out as a plain text file unless symlink support is enabled; copy from `skills/` instead if that happens.
- `scripts/install-agent-skills.sh` is a helper for copying skills. Inspect it before running.

Runtime support varies. See `docs/compatibility.md` for notes.

### C. AI Project upload (ChatGPT Projects, Claude Projects, Gemini, or similar)

1. Add `project-import/PROJECT_INSTRUCTIONS.md` to the project's instruction field, if the platform offers one.
2. Upload `project-import/PROJECT_UPLOAD_BUNDLE.md` as the central project reference. It contains the project-wide rules, all workflows, templates, and quick prompts in one Markdown file.
3. For a long project, also upload the relevant working templates from `templates/` and maintain them as project files.
4. Start with a prompt from `project-import/QUICK_PROMPTS.md`.

If the platform has file limits, upload the instruction file and only the relevant workflow and template documents. A generic AI Project may not execute a workflow just because it is present in the bundle; invoke the workflow explicitly by name.

## What's included

| Path | Contents |
| --- | --- |
| `skills/` | 13 independently loadable workflows (full index: [`SKILL_INDEX.md`](SKILL_INDEX.md)) |
| `agents/` | `legal-manuscript-editor`, `legal-research-reviewer` |
| `templates/` | Registers, argument map, source ledger, project brief, handover |
| `examples/` | Illustrative claim-evidence matrix and research log |
| `evals/` | Human-review cases (citation fidelity, adverse authority, manuscript integrity, seeded errors) and machine-checkable regression cases |
| `references/` | Legal research quality standards |
| `project-import/` | Instructions, upload bundle, and quick prompts for AI Projects |
| `docs/compatibility.md` | Platform and packaging notes |
| `scripts/` | Validator, installer, bundle builder, and standard-library helpers: `extract_docx.py` (body and footnotes, chunking), `integrity_manifest.py` (fixed-fact diff), `check_register_refs.py` (record IDs), `hidden_text_check.py` (hidden text in manuscripts) |
| `tests/` | Structure tests and script tests |

## Included workflows

Not sure which skill fits? See the stage table and "Telling similar skills apart" in [`SKILL_INDEX.md`](SKILL_INDEX.md).

- `academic-project-router` — Pick and sequence the right skills when a request spans several kinds of work or the next step is unclear. Not needed when one skill obviously fits.
- `research-planning` — Plan a new project (question, provisional thesis, scope, method, sources, stages), or judge whether an existing thesis or article idea is novel, useful, sound, and worth pursuing. Use before research or drafting starts. For the step-by-step logic of a thesis already chosen, use argument-mapping.
- `literature-synthesis` — Map the scholarship on a question into positions, disagreements, methods, and gaps, and place the paper's contribution among them. For whether one specific thesis is already preempted, use research-planning.
- `source-verification` — Check that a source exists, is the right document and version, and supports the exact sentence it is cited for: one source before relying on it, or every footnote, quotation, pinpoint, and bibliography entry in a manuscript. For what an authority means or how far it reaches, use legal-authority-analysis.
- `legal-authority-analysis` — Interpret a case, statute, treaty, or administrative or international decision: what it holds, how it reasons, its binding force, limits, ambiguities, and competing readings. For whether a citation exists and supports a sentence, use source-verification.
- `argument-mapping` — Lay out the author's own thesis as linked claims, evidence, warrants, assumptions, and weakest links, before drafting or when restructuring, and keep the claim register. For a reader's judgment of a finished manuscript, use manuscript-review.
- `academic-legal-drafting` — Write or rewrite passages: turn notes, sources, and outlines into connected academic legal prose, or revise a paragraph or section. Holds the kit's prose rules on style, enumeration, and cross-references. For restructuring or cutting a whole manuscript, use manuscript-consolidation.
- `multilingual-legal-writing` — Write, revise, or translate scholarship in any language other than British English or between languages, and use foreign-language sources, keeping legal meaning and the terminology of the right legal system, not just the right language.
- `manuscript-review` — Give a one-off critical assessment of a manuscript as a desk editor, referee, examiner, or pre-submission auditor, with findings ranked by severity. Produces a report, not revised text. For repeated critique-and-revision rounds, or answering real referee reports, use adversarial-writing-cycle.
- `adversarial-writing-cycle` — Run rounds of critique, author response, revision, and retest until the argument holds, or work through real referee reports and draft the response letter. Produces revised text and a response matrix. For a single critical report, use manuscript-review.
- `manuscript-consolidation` — Restructure a whole manuscript or long section: remove repetition, reorder sections, standardise terms, fix transitions and cross-references, or meet a word limit by moving material to footnotes. For drafting or rewriting individual passages, use academic-legal-drafting.
- `project-continuity` — Resume or hand over a long project across sessions or models: read and update the handover and registers, check them against the files, and write a cold-start handover.
- `anticipatory-analysis` — Fix an analytical method before seeing the evidence, as a protocol for interpreting a future event or a codebook for coding many judgments, decisions, or statutes, then apply it without retrofitting.

## Suggested use

- **Small task:** project instructions plus one relevant workflow.
- **Article drafting:** project instructions, project brief, argument map, claim/source ledger, and `academic-legal-drafting`.
- **Critical revision:** add `adversarial-writing-cycle` and its log; use a separate reviewer conversation or model where practical.
- **Long project:** keep a `HANDOVER.md`, stable IDs, decision/correction/claim/source registers, and refresh the handover at the end of each substantial session.
- **Responding to referees:** use `adversarial-writing-cycle` in its external-reviews mode.
- **Submission:** use `source-verification` in manuscript mode and `manuscript-review` in pre-submission mode, but retain human responsibility for legal correctness and final judgment.

## Validation

From the repository root:

```bash
claude plugin validate ./
python3 scripts/validate_skills.py
python3 scripts/build_bundle.py --check
python3 -m unittest discover -s tests -v
```

`claude plugin validate` checks the plugin and marketplace manifests. The Python validator checks skill folder names against frontmatter and confirms every skill has a description. These are structural checks, not proof of academic or legal correctness.

## Design reference

The kit takes inspiration from the composable, task-specific skill approach in [mattpocock/skills](https://github.com/mattpocock/skills/tree/main): use a small skill for a clearly defined task instead of loading one giant procedure for every request. This repository is independently authored for academic legal work. It is not affiliated with Matt Pocock or his repository, and it does not copy their individual skill texts. Version 0.2.0 adapts some methods from other openly licensed legal skill collections (Apache-2.0 and MIT); each adaptation is attributed in the file where it appears and listed in [`NOTICE`](NOTICE) and [`REFERENCES.md`](REFERENCES.md).

## Licence

Released under the GNU General Public License v3.0 only (`GPL-3.0-only`). See [`LICENSE`](LICENSE). Third-party notices and licence texts for adapted material are in [`NOTICE`](NOTICE) and [`LICENSES/`](LICENSES/). Cite the upstream design reference in attribution and documentation, and do not imply endorsement or affiliation.

## Contributing and security

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for contribution guidelines and [`SECURITY.md`](SECURITY.md) for how to report a concern.
