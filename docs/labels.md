# Labels used in the kit's answers

Every answer opens with a plain bottom line. The labels below come after it, for checking the work. Each set of labels is defined in one skill, given in brackets, and every other skill and template uses the same words.

## How much a problem matters (`manuscript-review`)

| Label | Meaning |
|---|---|
| `critical` | An error of law, evidence or reasoning that defeats or materially misstates the thesis, or a submission blocker |
| `major` | Weakens the argument or contribution materially, but is not fatal |
| `moderate` | A real problem with a contained effect |
| `minor` | Polish, form or style |

## Sources (`source-verification`)

| Field | Labels | Meaning |
|---|---|---|
| Access mode | live source · user-supplied source · source missing | What the assistant could actually open |
| Source status | `Inspected` · `Partly inspected` · `Lead only` · `Unavailable` · `Inauthentic/incorrect` | Whether the source itself was read. *Lead only* means the assistant found only a reference to it |
| Level reached | `Existence` · `Content` · `Paragraph` | How far the check went |
| Claim support | `Direct support` · `Partial support` · `Inference required` · `Interpolated` · `Quotation inaccurate` · `Contradicted` · `Not addressed` · `Not yet assessed` | Whether the source says what it is cited for. *Interpolated* means the draft added a detail the source does not contain |
| Salience | `load-bearing` · `supporting` · `illustrative` | How much of the argument rests on the sentence or source |

`Not found` is not `Contradicted`: a failed search shows only that that search found nothing.

## Gaps left visible on purpose

A marker in the text shows something the assistant would otherwise have had to guess.

| Marker | Meaning |
|---|---|
| `[SOURCE TO VERIFY]` | The source's details could not be confirmed |
| `[PINPOINT TO VERIFY]`, `[PAGES TO VERIFY]` | The page or paragraph could not be confirmed |
| `[SUPPORT NEEDED]` | The claim has no adequate support yet |
| `[REASON NEEDED]` | A step in the argument has no stated reason |
| `[SUPPORT TO CHECK]` | A finding depends on what an authority says, and that has not been verified |

## Claims, theses and objections

| Field | Labels |
|---|---|
| Claim status | `ESTABLISHED` · `CONTESTED` · `PROVISIONAL` · `UNSUPPORTED` · `SUPERSEDED` |
| Treatment of other scholars (`literature-synthesis`, `manuscript-review`) | `fair` · `slanted` · `strawman` · `uncharitable` |
| Thesis verdict (`research-planning`) | `green` · `yellow` · `red` |
| Objection after retest (`adversarial-writing-cycle`) | `resolved` · `partly resolved` · `unresolved` · `withdrawn as mistaken` · `superseded` |

## Language (`argument-and-language-check`)

| Label | Meaning |
|---|---|
| Band 1–9 | The level on one criterion of the kit's scorecard. It is modelled on the IELTS band structure but is **not** an IELTS score and does not convert to one |
| `meets` · `close` · `below` | How the text compares with the top level of a test you named, such as TOEFL or DALF. This is a lens, never that test's score |
