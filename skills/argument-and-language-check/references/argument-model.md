# The argument model

One shared model of argument for the whole kit. `argument-and-language-check` uses it to diagnose and repair passages; `argument-mapping`, `academic-legal-drafting`, `manuscript-review` and `adversarial-writing-cycle` use the same vocabulary.

It combines four sources (see `REFERENCES.md` at the repository root):

- the claim–reason–evidence model of the University of Pittsburgh's Department of Communication guide, with its two tests for reasons and its tests for evidence;
- Bradley Dowden, *Logical Reasoning*, chapter 2 ("Claims, Issues, and Arguments"): standard form, indicator words, implicit premises and conclusions, validity and strength, and the difference between arguments, explanations and descriptions;
- Stephen Toulmin's layout of arguments (warrant, backing, qualifier, rebuttal), already used in the kit as "warrant";
- Stephanie Link, *Scientific Writing for Publication*, section 2, "Claim Structure and Organization": functional claims, the general-to-specific flow, synthesis rather than summary, and the positive-to-critical turn that opens a gap.

The model is a diagnostic aid, not a template every paragraph must display.

---

## 1. The parts

| Part | What it is | Test |
|---|---|---|
| **Issue** | The open question, stated neutrally: *whether* X. | Can a reasonable reader still take either side? |
| **Claim** (conclusion) | A statement capable of being true or false, or right or wrong, that the passage asks the reader to accept. | Is it arguable? Taste ("I find the judgment unpersuasive") is not a claim until reasons make it one. |
| **Reason** (premise) | A statement offered in support of the claim. | **Challenge test:** does it answer "why should I accept that?" **Because test:** does "[claim] *because* [reason]" read as a sensible sentence? |
| **Evidence** | What supports a reason: authority, data, instances, testimony. | Is it the right kind for the reason, and does it pass the tests in §3? |
| **Warrant** | The general principle that licenses the step from reason to claim. Often unstated. | If the warrant were said aloud, would the intended reader accept it? |
| **Backing** | Support for the warrant itself (a line of authority, a method, a theory). | Needed only where the warrant is contested. |
| **Qualifier** | How strongly the claim is put: *must*, *probably*, *arguably*, *in most cases*. | Does the strength match what the reasons and evidence can carry? |
| **Rebuttal** | The conditions under which the claim would not hold, and the strongest objection, answered. | Is the strongest objection met, not a weaker one? |

Two passing tests do not make an argument sound: a reason can pass the challenge and because tests and still be false or insufficient.

## 2. Kinds of claim

Different claims need different support. Name the kind before judging the support.

| Kind | Asks | Typical support in legal scholarship |
|---|---|---|
| **Fact** | What is or was the case? | Primary documents, data, findings of a court or inquiry (as evidence of what that body found) |
| **Definition** | What is X, or does X fall within category Y? | Text, structure and purpose; authority construing the term; scholarly usage |
| **Cause** | What produced X, or what will X produce? | Method capable of supporting causation; rival explanations excluded |
| **Doctrine** | What does the law require or permit? | Primary authority, its hierarchy, date, status and reasoning |
| **Value** | Is X good, legitimate, just, proportionate? | A stated evaluative criterion, then its application |
| **Policy** | What should be done? | A problem, a proposed measure, reasons it would work, costs, and why it beats the alternatives |

### Functional claims: what a claim does in the piece

The same claim can also be read for the work it does in the paper. Name the function when checking whether a paragraph earns its place.

| Function | Does | Typical frame |
|---|---|---|
| **Cause** | Explains where a problem comes from | X stems from / is attributable to Y |
| **Effect** | Shows why the problem matters ("so what?") | X results in / leads to Y |
| **Solution** | Proposes a measure, reading or test | Adopting X would address Y |
| **Best approach** | Argues one approach is better, on stated grounds | X is the better approach to Y because Z |
| **Limitation** | Marks where existing work, doctrine or authority stops | X does not account for Y |
| **Future direction** | Turns a limitation into the question the paper or later work answers | That gap calls for an inquiry into Y |

Limitation and future-direction claims work as a pair: the first critiques existing work, the second uses that critique to open the space the paper occupies. A paragraph whose only claim is "this topic matters" has no function yet.

A common fault is support of the wrong kind: a policy claim supported only by a value premise with no account of whether the measure would work, or a doctrinal claim supported by commentary instead of authority.

## 3. Kinds of evidence and their tests

| Kind | Tests |
|---|---|
| **Authority** (legislation, judgments, treaties, official decisions) | Right document and version; binding or persuasive for this question; what it holds as opposed to what it says in passing; later treatment. Use `source-verification` and `legal-authority-analysis`. |
| **Instances** (cases as examples, case studies, narratives) | Representative of the class claimed? Selected how? Counter-instances? |
| **Statistics and data** | Source, method, sample, period; does the measure capture what the claim is about? |
| **Testimony** (interviews, statements, official accounts) | Evidences that it was said. Does the speaker have first-hand knowledge? Corroborated? |
| **Expert opinion** (scholarship, expert reports) | Expertise on this specific question? Majority or outlier view? Read in the original, not at second hand? |

## 4. Reading an argument: standard form

To check a passage, rewrite its argument in standard form:

1. Find the claim. Conclusion indicators: *therefore, thus, so, hence, it follows that, accordingly*. Premise indicators: *because, since, given that, for, as shown by*. Indicators are clues, not proof: *since* and *so* also have non-argumentative uses.
2. Set aside **discount** material: clauses introduced by *although, even though, admittedly, while it is true that*. They acknowledge counter-considerations; they are neither premises nor the conclusion, but they show what the writer thinks must be answered.
3. List the premises, then the conclusion below a line. Replace pronouns with what they refer to. Remove repetition and rhetoric.
4. **Supply implicit premises** that the writer must be relying on. Use charity (the most plausible premise that would make the argument work) but not so much charity that a real gap is hidden. An implicit premise that is false or doubtful is a finding.
5. **Supply an unstated conclusion** only where it is clear what the writer wants the reader to conclude (fidelity). If it is not clear, that is itself a finding: the passage has no claim.
6. For a chain of reasoning, draw a tree: basic premises at the top, sub-conclusions in the middle, the main conclusion at the bottom.

## 5. Judging the step

- **Deductive form:** the step is *valid* if the conclusion must be true whenever the premises are true. Test by looking for a counterexample: a case in which every premise holds and the conclusion fails.
- **Inductive form:** the step is *strong* to the degree that the conclusion is probably true if the premises are true. Strength comes in degrees, so the qualifier must match it.
- A valid or strong step still fails if a premise is false or unknown. Check the premises, not only the step.

## 6. Arguments, explanations and descriptions

- A **description** says how things are.
- An **explanation** says why or how something came to be, taking the fact as given.
- An **argument** tries to persuade the reader that something is so.

*Because* appears in both explanations and arguments. The common fault in legal writing is a passage that *describes* authorities at length and then states a conclusion it never argued for, or that *explains* a court's reasoning and treats the explanation as a justification.

## 7. Organising claims across paragraphs

Single arguments have to be arranged into a line of reasoning.

- **General to specific.** An introduction usually narrows: the broad field (territory), then the specific problem or conflict (niche), then the paper's own question or thesis. A conclusion widens again.
- **Synthesis, not summary.** Summary reports what one source says. Synthesis groups sources to support the writer's own claim: "Although A and B both establish X, neither addresses Y." A run of "A held… B argued… C found…" is a list, not an argument.
- **The positive-to-critical turn.** Acknowledge what existing work or authority achieves, pivot with a contrastive connector, then state the limitation that creates the gap. The turn should be fair: the positive part must be what that work actually achieved.
- **Reverse outline.** To check organisation, write one sentence per paragraph stating its claim (not its topic), label each *general*, *narrowing* or *specific*, and find the sentence where the turn happens. Missing labels, a jump from general to specific, or no turn at all are findings.

## 8. Symptom → diagnosis → repair

| Symptom in the text | Diagnosis | Repair |
|---|---|---|
| A paragraph summarises sources and ends without a proposition | No claim; description, not argument | Add the topic claim; reorder so the sources support it |
| "Clearly", "it is evident", "undoubtedly" with nothing after | Assertion standing in for a reason | Supply the reason or soften the qualifier |
| Reason fails the because test | Non-sequitur or irrelevant reason | Replace the reason or restate the claim |
| The step depends on a principle the reader would dispute | Unstated, contested warrant | State the warrant and give backing |
| One case cited for a general rule | Unrepresentative instance; hasty generalisation | Narrow the claim or add the line of authority |
| A key term changes meaning between premise and conclusion | Equivocation | Fix one meaning; define it in the glossary |
| Conclusion goes further than any premise ("all", "always", "must") | Overclaim; qualifier too strong | Match the qualifier to the support |
| Objection answered is a weak version of the opposing view | Strawman | State the strongest version, then answer it |
| Argument is that a rule is good because it is the rule | Circularity (begging the question) | Supply an independent reason |
| "Since A follows B, B caused A" | Post hoc causal claim | Identify the mechanism; exclude rival causes |
| Authority's description of facts treated as the facts | Source evidences its own making, not the events | Attribute: "the commission found that…" |
| Counter-consideration raised with *although* and never answered | Discount left hanging | Answer it, or say why it does not defeat the claim |
| "A held… B argued… C found…" with no claim of the writer's own | Summary in place of synthesis | Group the sources under the writer's claim; say what they jointly show and what they miss |
| Introduction states the topic's importance, then the thesis, with nothing between | No niche; missing positive-to-critical turn | Add the limitation in existing work that the thesis answers |
| Paragraph's claim is "X is important" or "X raises issues" | No functional claim | Say what X causes, why it matters, what should be done, or where existing work stops |
| "What the law says" used to prove "what institutions do" | Text-to-practice inference | Add evidence of practice, or restate as a claim about design |
