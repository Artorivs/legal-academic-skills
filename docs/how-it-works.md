# How the kit works

Diagrams of how the kit works, in six parts, each with the reasoning behind its design. GitHub renders the diagrams; elsewhere, paste a block into [mermaid.live](https://mermaid.live).

1. [From request to workflow](#1-from-request-to-workflow)
2. [The workflows across a project](#2-the-workflows-across-a-project)
3. [Shared standards](#3-shared-standards)
4. [Inside the argument-and-language check](#4-inside-the-argument-and-language-check)
5. [The adversarial cycle](#5-the-adversarial-cycle)
6. [Project records](#6-project-records)

---

## 1. From request to workflow

```mermaid
flowchart TD
    U["You: a request in plain words<br/>plus your text and sources"] --> R{"Does one workflow<br/>obviously fit?"}
    R -- yes --> W["That workflow"]
    R -- "no, or several kinds of work" --> AR["academic-project-router<br/>picks the fewest workflows, in order"]
    AR --> W
    W --> A{"Can it see the<br/>sources it needs?"}
    A -- yes --> D["Does the work"]
    A -- no --> Q["Marks the gap<br/>[SOURCE TO VERIFY]<br/>and does only what it safely can"]
    D --> O["Answer: plain bottom line first,<br/>then detail and labels"]
    Q --> O
    O --> C{"A choice only<br/>you can make?"}
    C -- yes --> DQ["One question,<br/>recommendation first"]
    C -- no --> E["Done; records updated<br/>if the project keeps them"]
    DQ --> E
```

**Why.**
- *You should not have to learn the kit.* Requests are in plain words; the router exists for the cases where the fit is unclear, not as a step every request must pass through.
- *Small skills, used sparingly.* Running every check on every request wastes attention and buries the result. The router's rule is "the smallest set that does the job".
- *Gaps are shown, not filled.* A guessed citation looks exactly like a real one, so the kit marks what it could not see instead of completing it.
- *Bottom line first.* The labels are for checking the work; the decision you need to make should not be hidden under them.
- *You decide.* Substantive choices are put to the author one at a time, with a recommendation, so nothing important is decided by default.

---

## 2. The workflows across a project

```mermaid
flowchart TD
    PC["project-continuity<br/>reads and updates the handover<br/>at the start and end of every session"]
    PLAN["<b>Plan</b><br/>research-planning<br/>literature-synthesis<br/>anticipatory-analysis"]
    READ["<b>Read and verify</b><br/>legal-authority-analysis<br/>source-verification"]
    BUILD["<b>Build and write</b><br/>argument-mapping<br/>academic-legal-drafting<br/>multilingual-legal-writing"]
    CHECK["<b>Check</b><br/>argument-and-language-check"]
    TEST["<b>Test</b><br/>manuscript-review<br/>adversarial-writing-cycle"]
    FIN["<b>Finish</b><br/>manuscript-consolidation<br/>then source-verification again"]
    PC -.-> PLAN
    PLAN --> READ --> BUILD --> CHECK
    CHECK -->|"problems found"| BUILD
    CHECK -->|"passage holds"| TEST
    TEST -->|"objections to fix"| BUILD
    TEST -->|"argument holds"| FIN
```

The two agents give a second opinion from a fresh context:

```mermaid
flowchart LR
    LRR["agent: legal-research-reviewer"] --> RP2["research-planning"] & LAA2["legal-authority-analysis"] & SV2["source-verification"] & AM2["argument-mapping"] & MR2["manuscript-review"]
    LME["agent: legal-manuscript-editor"] --> ALD2["academic-legal-drafting"] & MC2["manuscript-consolidation"] & MR3["manuscript-review"] & SV3["source-verification"] & MLW2["multilingual-legal-writing"]
```

**Why.**
- *One skill, one kind of work.* Each skill says where it stops and which neighbour to use instead (see "Telling similar skills apart" in `SKILL_INDEX.md`), so two skills never compete for the same request.
- *Verification sits before drafting and again before submission.* Citations are cheapest to fix before prose is built on them, and must be rechecked after consolidation moves them.
- *The check loops back into drafting.* A passage is not finished because it reads well; it is finished when its argument and language pass the check.
- *Agents defer to skills.* They hold no procedures of their own, so a fix to a skill reaches the agents automatically. Their value is independence: a reviewer that has not seen the drafter's reasoning is less anchored by it.
- *Continuity is not a stage.* It runs whenever a session starts or ends, at any stage.

---

## 3. Shared standards

```mermaid
flowchart TB
    subgraph STD["Defined once"]
        AMOD["Argument model<br/>claim · reason · evidence · warrant<br/>qualifier · rebuttal · functional claims"]
        LRUB["Language rubric<br/>4 criteria × 9 bands<br/>+ lenses for 10 other tests"]
        PROSE["Prose rules<br/>British English · no 'first, second'<br/>needed cross-references only"]
        LABELS["Label vocabulary<br/>access · status · level · support · salience"]
        SEV["Severity scale<br/>critical · major · moderate · minor"]
    end
    AMOD --> ALC["argument-and-language-check"] & AM["argument-mapping"] & ALD["academic-legal-drafting"] & MR["manuscript-review"] & AWC["adversarial-writing-cycle"]
    LRUB --> ALC & MR
    PROSE --> ALD & MC["manuscript-consolidation"] & MR & ALC
    LABELS --> SV["source-verification"] & MR & TPL["templates"]
    SEV --> MR & AWC
```

**Why.** If two skills used different words for the same fault, a finding from a review could not be traced to a fix in drafting. Each standard lives in one file (the argument model and rubric in `argument-and-language-check/references/`, the prose rules in `academic-legal-drafting`, the labels in `source-verification`, the severity scale in `manuscript-review`) and the other skills point to it. Changing a standard is a change in one place.

---

## 4. Inside the argument-and-language check

```mermaid
flowchart TD
    IN["Your passage + your wording"] --> T{"Any text?"}
    T -- no --> ASK["Ask for it in one line"]
    T -- yes --> DEP{"Depth and scope"}
    DEP -->|"one paragraph, 'quick', 'fix the English'"| QK["Quick"]
    DEP -->|"several paragraphs, 'check', 'score'"| ST["Standard"]
    DEP -->|"'teach me', second-language writer"| TE["Teaching"]
    QK & ST & TE --> S1["Sense the argument<br/>standard form · implicit premises<br/>kind and function of claim<br/>reverse outline for sections"]
    QK & ST & TE --> S2["Sense the language<br/>band per criterion<br/>with one quoted phrase"]
    S2 -.->|"test named,<br/>or not English"| LENS["Test lens<br/>that test's criteria<br/>meets · close · below"]
    LENS -.-> DG
    S1 & S2 --> DG["Diagnose<br/>symptom → cause → repair<br/>cut what fails the sustainability test"]
    DG --> CO["Correct<br/>same position, narrowed if unsupported<br/>citations and numbers untouched<br/>[SUPPORT NEEDED] where it must be"]
    CO --> IM["Improve<br/>2–3 patterns to practise"]
    IM --> OUT["Bottom line · findings · corrected text"]
```

**Why.**
- *Sense, diagnose, correct, improve* is the order a good tutor works in: a correction without a diagnosis teaches nothing, and a diagnosis without a correction leaves the writer stuck.
- *Depth follows the text.* A three-sentence paragraph does not need a seven-part report; trial runs showed that without a budget, the check produced a thousand words for three sentences.
- *Standard form exposes what prose hides.* Writing premises above a line shows the unstated warrant and the claim that goes further than its reasons.
- *The rubric borrows a structure, not a score.* Four criteria from a widely used writing assessment give a familiar frame, but the descriptors are rewritten for legal writing, so the bands are never presented as an exam result.
- *One scorecard, many lenses.* Every check scores the same four criteria. A named test changes only how the result is reported: under that test's criteria, against its top level, with no number on its scale, because a number would read as an official score. The lens file is read only when a test is named, so ordinary checks stay short.
- *The writer's position is protected.* The check may narrow an overclaim; it never replaces or strengthens the thesis, and never changes a citation.

---

## 5. The adversarial cycle

```mermaid
sequenceDiagram
    autonumber
    participant D as Drafting scholar
    participant R as Adversarial reviewer
    participant A as Author
    participant T as Retest reviewer
    D->>R: Draft, with claims and sources visible
    R->>R: Objections, filtered by the sustainability test
    R->>A: Numbered objections with severity
    A->>D: Accept / partly / reject with reasons
    D->>T: Revised text linked to objection IDs
    T->>T: Resolved? New weaknesses? Own errors?
    T-->>D: Unresolved items
    Note over D,T: Repeat up to the cycle limit,<br/>stop early when revision stops helping
    T->>A: Revised text, response matrix, open objections
```

**Why.** Separate roles reduce the pull towards agreeing with oneself. The reviewer must attack the strongest version of the claim, the author must answer every material objection, and the retest must admit when an objection was wrong. The cycle ends at a limit or when revision stops helping, not when the reviewer is satisfied, because a model can always be talked into agreement.

---

## 6. Project records

```mermaid
flowchart TB
    H["HANDOVER.md<br/>where things stand · read first"]
    B["project-brief.md<br/>question · thesis · scope"]
    DR["decision-register<br/>D-001…"]
    CR["correction-register<br/>C-001…"]
    CL["claim-register<br/>CL-001…"]
    AMAP["argument-map<br/>chain and weakest links"]
    SL["source-ledger<br/>SRC-001…"]
    AL["adversarial-cycle-log<br/>objections"]
    DRAFT["draft.md and findings-*.md"]

    H -->|"points to"| B & DR & CR & CL & SL & AL
    CL --> AMAP
    CL -->|"supported by"| SL
    DRAFT -->|"cites by ID"| CL & SL
    DR -->|"changes"| DRAFT
    CR -->|"corrects"| DRAFT
    AL -->|"may add"| DR & CR
```

**Why.**
- *The files are the memory.* A new session or a different model cannot see earlier chats; it can read files.
- *One home per record.* A decision written in two places will eventually say two different things. Other files point to the record by ID.
- *Corrections are kept, not erased.* A project that claims a careful method must be able to show its own errors and how they were found.
- *The handover routes; it does not duplicate.* It says where things are and what comes next, and is checked against the files before anyone relies on it (`scripts/check_register_refs.py`).
- *Use only what the project needs.* A single task needs none of this; an article needs the brief and handover; a thesis needs the full set (`templates/README-project.md`).
