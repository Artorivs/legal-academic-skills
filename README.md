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

Skills are namespaced by the plugin, for example `legal-academic-skills:citation-audit`. The plugin also provides two agents, `legal-manuscript-editor` and `legal-research-reviewer`.

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
| `skills/` | 15 independently loadable workflows (full index: [`SKILL_INDEX.md`](SKILL_INDEX.md)) |
| `agents/` | `legal-manuscript-editor`, `legal-research-reviewer` |
| `templates/` | Registers, argument map, source ledger, project brief, handover |
| `examples/` | Illustrative claim-evidence matrix and research log |
| `evals/` | Human-review cases: citation fidelity, adverse authority, manuscript integrity |
| `references/` | Legal research quality standards |
| `project-import/` | Instructions, upload bundle, and quick prompts for AI Projects |
| `docs/compatibility.md` | Platform and packaging notes |
| `scripts/`, `tests/` | Validator, installer helper, and structure tests |

## Included workflows

- `academic-project-router` — Choose and coordinate the appropriate academic legal research or writing workflow. Use when a task spans several kinds of work or the next step is unclear.
- `research-planning` — Design a rigorous research plan for academic legal work, including research questions, scope, method, source strategy, and manageable research stages.
- `source-verification` — Verify legal, academic, empirical, and archival sources and match each source to the precise proposition it supports. Use before relying on unfamiliar citations or adding authorities.
- `legal-authority-analysis` — Analyse cases, legislation, treaties, international legal materials, and administrative decisions with attention to authority, context, reasoning, limits, and competing readings.
- `literature-synthesis` — Synthesize legal and interdisciplinary scholarship into an analytical account of debates, methods, evidence, and contribution rather than a sequence of source summaries.
- `argument-mapping` — Map an academic legal thesis into linked claims, evidence, warrants, assumptions, counterarguments, and vulnerabilities before drafting or revising.
- `academic-legal-drafting` — Turn notes, sources, outlines, or rough prose into connected academic legal writing with a clear claim, developed reasoning, and careful source use.
- `adversarial-writing-cycle` — Run a repeatable draft–critique–response–revision–retest cycle to expose weaknesses in an academic legal argument and record unresolved objections.
- `critical-peer-review` — Review a legal academic manuscript as a rigorous peer reviewer, examiner, or editor and identify consequential weaknesses with specific remedies.
- `citation-audit` — Audit footnotes, pinpoint citations, quotations, bibliographies, and source-to-claim fit in a legal academic manuscript.
- `bilingual-legal-writing` — Draft, revise, or translate legal scholarship between English and Chinese while preserving doctrinal meaning, jurisdictional terminology, and register.
- `project-continuity` — Continue a long academic research project across sessions or models using stable records, explicit decisions, corrections, evidence gaps, and concise handovers.
- `manuscript-consolidation` — Consolidate a manuscript by removing repetition, improving structure and transitions, and preserving necessary evidence, qualifications, and argumentative steps.
- `final-manuscript-audit` — Perform the final substantive and editorial audit of an academic legal manuscript before submission or circulation.
- `anticipatory-analysis` — Create and apply a pre-specified protocol for analysing future events or incoming evidence without retrofitting the method to the outcome.

## Suggested use

- **Small task:** project instructions plus one relevant workflow.
- **Article drafting:** project instructions, project brief, argument map, claim/source ledger, and `academic-legal-drafting`.
- **Critical revision:** add `adversarial-writing-cycle` and its log; use a separate reviewer conversation or model where practical.
- **Long project:** keep a `HANDOVER.md`, stable IDs, decision/correction/claim/source registers, and refresh the handover at the end of each substantial session.
- **Submission:** use `citation-audit` and `final-manuscript-audit`, but retain human responsibility for legal correctness and final judgment.

## Validation

From the repository root:

```bash
claude plugin validate ./
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests -v
```

`claude plugin validate` checks the plugin and marketplace manifests. The Python validator checks skill folder names against frontmatter and confirms every skill has a description. These are structural checks, not proof of academic or legal correctness.

## Design reference

The kit takes inspiration from the composable, task-specific skill approach in [mattpocock/skills](https://github.com/mattpocock/skills/tree/main): use a small skill for a clearly defined task instead of loading one giant procedure for every request. This repository is independently authored for academic legal work. It is not affiliated with Matt Pocock or his repository, and it does not copy their individual skill texts. See [`REFERENCES.md`](REFERENCES.md).

## Licence

Released under the GNU General Public License v3.0 only (`GPL-3.0-only`). See [`LICENSE`](LICENSE). Cite the upstream design reference in attribution and documentation, and do not imply endorsement or affiliation.

## Contributing and security

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for contribution guidelines and [`SECURITY.md`](SECURITY.md) for how to report a concern.
