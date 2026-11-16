# Legal Academic Skills

Workflows that help an AI assistant do academic legal research and writing carefully: plan a project, read authorities, check citations, build and test an argument, draft, check argument and English, review, and hand a long project over between sessions.

Designed for administrative law, human rights, law and society, and public international law, and usable for doctrinal, comparative, theoretical, historical, empirical, socio-legal, and interdisciplinary work.

> **You stay responsible.** These workflows structure the work; they do not certify that anything is legally or academically correct. Check every authority, quotation, and proposition yourself before relying on it.

---

## Start here

**1. Install** (pick one):

- **Claude Code:** run these two commands.
  ```zsh
  /plugin marketplace add Artorivs/legal-academic-skills
  /plugin install legal-academic-skills@legal-academic-skills
  ```
- **Claude, ChatGPT or Gemini Projects:** paste [`project-import/PROJECT_INSTRUCTIONS.md`](project-import/PROJECT_INSTRUCTIONS.md) into the project's instructions and upload [`project-import/PROJECT_UPLOAD_BUNDLE.md`](project-import/PROJECT_UPLOAD_BUNDLE.md).

Other routes are under [More ways to install](#more-ways-to-install).

**2. Say what you want in plain words.** You do not need to know the skill names: the assistant picks the right workflow. If it does not, name the workflow from the table below.

**3. Paste or upload your text and sources.** The assistant checks only what it can actually see, and says so when it cannot see something.

## What do you want to do?

| I want to… | Say something like | You get back | Workflow |
|---|---|---|---|
| Check my paragraph's argument and English | "Check the argument and the English in this paragraph." | What is wrong and why, a scorecard, the corrected paragraph, and what to practise | `argument-and-language-check` |
| Turn notes into prose | "Turn these notes and sources into a section on X." | A drafted passage with gaps marked | `academic-legal-drafting` |
| Check my citations | "Check that every footnote in this section supports its sentence." | A table of each citation with what is wrong and the fix | `source-verification` |
| Understand a judgment, statute or treaty | "What does this judgment hold, and how far does it reach?" | Holding, reasoning, limits, rival readings | `legal-authority-analysis` |
| Plan a new project or test an idea | "Is this thesis new and worth writing?" | A project brief, or a green, yellow or red verdict with fixes | `research-planning` |
| See where my argument is weakest | "Map my argument and show me the weakest link." | An argument tree and a table of weak points with repairs | `argument-mapping` |
| Get a referee's view | "Review this as a referee for journal X." | Findings ranked by severity, and what is not in doubt | `manuscript-review` |
| Revise under challenge, or answer referees | "Here are the referee reports; help me respond." | A response matrix, revised text, and a response letter | `adversarial-writing-cycle` |
| Shorten or restructure | "Cut this to 10,000 words without losing the argument." | Restructured text and a log of every move | `manuscript-consolidation` |
| Map the literature | "What has the field said about X, and where do I fit?" | A map of positions and gaps | `literature-synthesis` |
| Write or translate in another language | "Translate this into Chinese for a Hong Kong readership." | Text plus a glossary and translator's notes | `multilingual-legal-writing` |
| Pick up a long project | "Read the handover and tell me where we are." | Current state, next three actions, updated records | `project-continuity` |
| Fix my method before evidence arrives | "Write a protocol for reading the inquiry report when it is published." | A dated protocol or codebook | `anticipatory-analysis` |
| Not sure | "What should I do next with this draft?" | The workflows to use, in order | `academic-project-router` |

More ready-to-use prompts: [`project-import/QUICK_PROMPTS.md`](project-import/QUICK_PROMPTS.md).

## Reading the results

Every result opens with a short **bottom line** in plain words. Tables and labels follow for those who want the detail. The labels you will see most often:

| Label | Plain meaning |
|---|---|
| `critical` / `major` / `moderate` / `minor` | How much a problem matters: from "the argument fails" to "polish" |
| `load-bearing` / `supporting` / `illustrative` | How much of the argument rests on a sentence or source |
| `Direct support` / `Partial support` / `Interpolated` | Whether a source says what it is cited for. *Interpolated* means the draft added a detail the source does not contain |
| `Inspected` / `Lead only` | Whether the assistant actually read the source, or only found a reference to it |
| `[SOURCE TO VERIFY]`, `[PINPOINT TO VERIFY]`, `[SUPPORT NEEDED]` | A gap left visible on purpose instead of being filled with a guess |
| Band 1–9 | Language scorecard level on one criterion. It is modelled on the IELTS band structure but is **not** an IELTS score |
| Meets / close / below | How a text compares with the top level of a test you named (TOEFL, GRE, Cambridge, PTE, CEFR, AP, VALUE, Goethe, TestDaF, DALF). A lens, never that test's score |

Every label, with where it is defined, is in [`docs/labels.md`](docs/labels.md).

To see how the workflows, agents and records fit together, and why, read [`docs/how-it-works.md`](docs/how-it-works.md) (diagrams).

## How much of the kit do you need?

- **One task:** install, then ask. Nothing else is needed.
- **An article over several sessions:** add [`templates/project-brief.md`](templates/project-brief.md) and [`templates/HANDOVER.md`](templates/HANDOVER.md), and ask the assistant to keep them up to date.
- **A thesis or book:** use the full set in [`templates/`](templates/), which keeps one record each for decisions, corrections, claims and sources. See [`templates/README-project.md`](templates/README-project.md).

---

## All workflows

The table above lists all fourteen. [`SKILL_INDEX.md`](SKILL_INDEX.md) arranges them by stage of a project and shows how to tell similar ones apart. The plugin also has two agents that review from a fresh context: `legal-manuscript-editor` and `legal-research-reviewer`.

---

## More ways to install

### Claude Code from a local clone

```zsh
git clone https://github.com/Artorivs/legal-academic-skills.git
claude --plugin-dir ./legal-academic-skills
```

Skills are namespaced by the plugin, for example `legal-academic-skills:source-verification`. Claude Cowork and the Claude desktop app also support plugins; check Anthropic's current documentation for how to add a GitHub marketplace or upload a zip of this repository.

### Other agents that read Agent Skills

Each skill is a directory whose entry point is `SKILL.md`, in the open [Agent Skills format](https://agentskills.io/specification). Copy the skill directories you want from `skills/` into your agent's skill directory, keeping each directory whole, or run:

```bash
bash scripts/install-agent-skills.sh /path/to/your/agent/skills
```

`skills/` is the canonical source. For the `.agents/skills` link and what has been checked on each platform, see [`docs/compatibility.md`](docs/compatibility.md).

### AI Projects in detail

1. Paste `project-import/PROJECT_INSTRUCTIONS.md` into the project's instructions field.
2. Upload `project-import/PROJECT_UPLOAD_BUNDLE.md`. It holds every workflow, reference, template and quick prompt in one file.
3. For a long project, also upload the templates you will use from `templates/` and keep them as project files.
4. If the platform limits file size, upload only the instructions and the workflows you need. A generic Project may not run a workflow just because it is in the bundle; ask for it by name ("use the argument-and-language-check workflow").

## What's in the repository

| Path | Contents |
| --- | --- |
| `skills/` | The 14 workflows, each with its own `references/` where needed |
| `agents/` | `legal-manuscript-editor`, `legal-research-reviewer` |
| `templates/` | Project brief, handover, registers, argument map, source ledger, search log |
| `evals/` | Human-review cases and machine-checkable regression cases |
| `project-import/` | Instructions, upload bundle, and quick prompts for AI Projects |
| `docs/how-it-works.md` | Diagrams of routing, workflows, shared standards, the check, the adversarial cycle and project records, with the reasons for each design choice |
| `docs/labels.md` | Every label the answers use, in plain words |
| `docs/compatibility.md` | What has been checked on each platform |
| `scripts/` | Validator, installer, bundle builder, and helpers: `extract_docx.py` (body and footnotes), `integrity_manifest.py` (fixed-fact diff), `check_register_refs.py` (record IDs), `hidden_text_check.py` (hidden text in manuscripts) |
| `tests/` | Structure tests and script tests |

## Validation

From the repository root:

```bash
claude plugin validate ./
python3 scripts/validate_skills.py
python3 scripts/build_bundle.py --check
python3 -m unittest discover -s tests -v
```

These are structural checks, not proof of academic or legal correctness.

## Design reference

The kit follows the composable, task-specific skill approach of [mattpocock/skills](https://github.com/mattpocock/skills/tree/main): a small skill for a clearly defined task instead of one giant procedure for every request. It is independently authored for academic legal work, is not affiliated with Matt Pocock or his repository, and does not copy their skill texts. The argument model and language rubric draw on the sources listed in [`REFERENCES.md`](REFERENCES.md).

## Licence

GNU General Public License v3.0 only (`GPL-3.0-only`). See [`LICENSE`](LICENSE). Cite the upstream design reference in attribution and documentation, and do not imply endorsement or affiliation.

## Contributing and security

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`SECURITY.md`](SECURITY.md).
