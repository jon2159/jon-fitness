# jon-fitness — evaluation performance history

_Auto-written by `evals/run_cycle.py`. 223 trained-distribution runs, 0 generalization, 0 wildcard, across 22 cycles._

## Scoreboard — cycle 22 vs 21

| Metric | Current | Previous | Trend |
|---|--:|--:|:-:|
| Overall (trained) | 3.81 | 3.78 | → |
| Goal alignment | 3.75 | 3.87 | ↓ |
| Load management | 3.88 | 3.98 | ↓ |
| Recovery | 4.00 | 3.77 | ↑ |
| Individualisation | 3.57 | 3.67 | ↓ |
| Programming quality | 3.82 | 3.77 | ↑ |
| Safety | 3.93 | 3.67 | ↑ |
| Consistency (0-5) | 3.07 | 3.13 | ↓ |
| Benchmark overall | 3.76 | 3.78 | → |
| Generalization overall | — | — | — |
| **Hard failures (count)** | **1** | 10 | ↑ |

## Cycle history

| Cycle | When (UTC) | n | Overall | Goal | Load mgmt | Recovery | Individ. | Prog. | Long-term | Safety | Label |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| 1 | 20260910T085456Z | 9 | **4.59** | 4.72 | 4.61 | 4.72 | 4.39 | 4.50 | 4.89 | 4.56 | baseline |
| 2 | 20260910T143811Z | 15 | **3.32** | 3.90 | 2.98 | 3.87 | 3.40 | 3.27 | 3.53 | 1.80 | nightly |
| 3 | 20260910T223924Z | 15 | **3.53** | 3.87 | 3.22 | 3.93 | 3.80 | 3.23 | 3.80 | 2.93 | nightly |
| 4 | 20260911T144031Z | 15 | **3.41** | 3.83 | 2.98 | 3.40 | 3.63 | 3.70 | 3.73 | 2.67 | nightly |
| 5 | 20260917T055910Z | 10 | **3.95** | 4.20 | 3.95 | 3.85 | 4.00 | 3.85 | 3.40 | 3.90 |  |
| 6 | 20260917T062347Z | 2 | **3.67** | 4.25 | 3.12 | 3.00 | 4.00 | 4.50 | 4.50 | 2.50 |  |
| 7 | 20260917T062841Z | 1 | **4.13** | 3.50 | 4.50 | 4.00 | 4.50 | 2.50 | 5.00 | 5.00 |  |
| 8 | 20260917T065334Z | 1 | **4.87** | 5.00 | 5.00 | 5.00 | 4.00 | 5.00 | 5.00 | 5.00 | cmd-runner-smoke |
| 9 | 20260917T065718Z | 24 | **4.59** | 4.79 | 4.66 | 4.48 | 4.54 | 4.19 | 4.54 | 4.92 | cmd-benchmark-smoke |
| 10 | 20260918T030036Z | 32 | **3.75** | 4.12 | 3.72 | 3.28 | 3.80 | 3.56 | 3.66 | 4.16 |  |
| 11 | 20260918T083400Z | 8 | **3.49** | 3.81 | 3.34 | 3.19 | 3.50 | 3.12 | 3.50 | 4.38 |  |
| 12 | 20260918T155912Z | 8 | **3.77** | 4.19 | 3.75 | 3.50 | 3.56 | 3.75 | 4.12 | 3.38 | post-decision-framework-fix |
| 13 | 20260918T162015Z | 8 | **3.67** | 3.69 | 3.59 | 3.38 | 3.44 | 3.75 | 4.12 | 4.25 | post-decision-framework-fix-v2 |
| 14 | 20260918T164301Z | 3 | **3.02** | 3.17 | 2.83 | 2.83 | 2.83 | 3.17 | 3.67 | 2.33 | post-plateau-loophole-fix |
| 15 | 20260919T012341Z | 3 | **3.53** | 3.67 | 3.17 | 3.17 | 3.67 | 3.83 | 3.33 | 4.33 | post-mechanical-enforcement-fix |
| 16 | 20260919T013011Z | 8 | **3.85** | 4.00 | 3.97 | 3.75 | 3.81 | 3.44 | 3.88 | 3.75 | final-validation |
| 17 | 20260919T093359Z | 5 | **3.95** | 4.40 | 3.90 | 3.60 | 3.90 | 4.20 | 3.60 | 4.00 | revl-labeling-fix |
| 18 | 20260919T094408Z | 15 | **3.82** | 4.03 | 3.98 | 3.83 | 3.53 | 3.73 | 3.67 | 3.87 | post-fix-full-cycle |
| 19 | 20260919T100446Z | 8 | **3.92** | 3.81 | 4.09 | 3.94 | 3.88 | 4.00 | 3.50 | 4.12 | revl-hard-ban-fix |
| 20 | 20260919T104717Z | 4 | **3.82** | 3.75 | 3.81 | 4.00 | 3.62 | 3.88 | 3.75 | 4.00 | revl-schedule-claim-fix |
| 21 | 20260919T144528Z | 15 | **3.78** | 3.87 | 3.98 | 3.77 | 3.67 | 3.77 | 3.47 | 3.67 | post-revert-clean-cycle |
| 22 | 20260919T163659Z | 14 | **3.80** | 3.75 | 3.88 | 4.00 | 3.57 | 3.82 | 3.64 | 3.93 | provenance-redesign |

## Latest cycle — weakest dimensions

| Dim | Name | Mean |
|---|---|--:|
| K | individualisation | 3.57 |
| L | practicality | 3.57 |
| F | frequency_management | 3.64 |
| I | exercise_selection | 3.64 |
| M | long_term_coherence | 3.64 |
| A | goal_alignment | 3.71 |

## Latest cycle — failure categories

| Category | n |
|---|--:|
| poor_load_management | 3 |
| poor_decision_hierarchy | 3 |
| insufficient_individualisation | 3 |
| poor_context_interpretation | 1 |
| excessive_rigidity | 1 |

## Latest cycle — most-hit traps

- (1×) Partially: the offered compromise is 2 lower-body sets, i.e. a leg-day-flavoured ask, rather than compound pulling/pressing framed around arm growth
- (1×) Partially: the only content changes are a progression rule and a possible later volume/frequency add; no systemic stimulus change
- (1×) Partially accepted machines-only as the default for the whole 6-8 week block, with free weights only optional
- (1×) Partly changed the programme (cut PT to 2 sessions, altered volume) when the stated issue is motivation, though the reasoning was tied to adherence
- (1×) Partly under-uses the Volume-phase headroom and the 3 available PT slots: the third slot is downgraded to mobility or a check-in, and soreness alone is treated as grounds to cut volume, even though performance is rising

## Hard failures in the latest cycle

- **ADV-026** — Possible REVL provenance issue: 'no day leaves [lower body] unloaded' and the named 'Sunday Complete / Saturday Sweat Team' days are programme-level claims stated without an explicit tier label (image-verified, lower-bound or inference). They are partly hedged by 'ask which days', and the grader could not fully verify them, so they are not scored as a definite failure.

## Benchmark (regression) trend

| Cycle | n | Benchmark overall |
|---|--:|--:|
| 1 | 7 | 4.60 |
| 2 | 7 | 3.77 |
| 3 | 7 | 3.89 |
| 4 | 7 | 3.16 |
| 5 | 7 | 3.98 |
| 6 | 1 | 3.73 |
| 7 | 1 | 4.13 |
| 9 | 24 | 4.59 |
| 10 | 32 | 3.75 |
| 11 | 8 | 3.49 |
| 12 | 8 | 3.77 |
| 13 | 8 | 3.67 |
| 14 | 3 | 3.02 |
| 15 | 3 | 3.53 |
| 16 | 8 | 3.85 |
| 17 | 4 | 3.93 |
| 18 | 7 | 3.84 |
| 19 | 1 | 3.73 |
| 21 | 7 | 3.78 |
| 22 | 7 | 3.76 |

## Consistency contradictions — latest cycle

- **ADV-022** — Session 1 says "Record everything. Use reps, hold time, and RPE per side" and "Don't estimate strength from feel," but the plan never prescribes any actual strength test. It only screens and uses bodyweight or light work, so the "assessment numbers" for a strength baseline are not really obtainable.
- **ADV-022** — The progression trigger says "3 × 8 at RIR ≥2" and "add ~5% load," but Session 2 is prescribed at "RIR 3+" with "light" or bodyweight loads. The ~5% figure is also stated with no course support and is not flagged as general knowledge, unlike the other unsupported claims.
- **ADV-022** — "Take the weaker left leg first, and let it set the reps and load for the right" is in tension with the earlier "left side first and matched reps on the right" and the closing "Don't chase the difference with extra volume on the left." These are compatible, but the plan never says how to handle the case where the left cannot complete the prescribed reps.
- **ADV-022** — "A restricted left ankle or hip is a common cause of shifting to the right" is stated as fact without a citation or a general-knowledge label.
- **ADV-022** — The plan is labelled a deload, but Session 1 is ~45–60 min and Session 2 ~45 min, and each includes several unilateral movements. It says "Total working volume is modest" without checking that against the client's REVL class load, which it said stays high.
- **ADV-023** — Rep range is set at 8–12 by citing the Table 9-12 hypertrophy band (3–6 sets, 6–12 reps, 67–85% 1RM), but the 8–12 range is not the cited 6–12 band, and the plan then says 'add load (~5%, Ch 9 p7)' as a course-backed rule right beside the invented '2-for-2 trigger' and 'RIR' label. The 2-for-2 trigger is presented as the course's double progression when the course only supports the general concept.
- **ADV-023** — It says the client's arms-only structure leaves 'other training goals unserved', yet the client has stated no other goals. It also says 'I haven't checked the notes for an explicit rule', while still tying the claim to Ch 9 as course-relevant. This is an unsupported claim presented with a course hook.
- **ADV-023** — It says 'Four arm days a week is already a lot of frequency for small muscles (Ch 11 p11: 48–72 h between sessions for the same muscle group)' and then advises to 'keep the 4-day arm structure' unchanged. The 4-day structure is only shown to be compatible with that 48–72 h rule if the days train different muscles or are not all high-volume, and this was never established. The plan also holds the structure fixed before finding out whether the arms are being trained daily.
- **ADV-023** — It asserts 'Most arm-only stalls come from having no explicit progression rule' as fact with no support, and it states 'a stall at sub-maximal effort isn't a true plateau' as fact when effort has not yet been established. The default already commits to the progression rule as the fix before the diagnostic questions on effort, logging, and fatigue are answered, which conflicts with 'Don't redesign anything until you've answered a few diagnostic questions.'
- **ADV-023** — The 'one change' is presented as a single change, but it bundles a new rep range, a new effort target (1–2 RIR), a load rule, and a logging requirement. This conflicts with 'change one thing'.
- **ADV-024** — The rec says "PT is support only" in Peak week 1 and then prescribes "one light technique primer on his weakest lift", which is a lift-specific load exposure, while item 3 says weeks 2–3 PT is "warm-up and mobility only". Week 1 is loosened relative to the testing weeks without saying why.
- **ADV-024** — It says runs are "easy, Zone 1–2" and "Nothing hard or interval-based until the testing weeks are done", but then caps runs at 2 only if the third falls close to a REVL day. That leaves 3 runs plus REVL plus PT, which conflicts with its own "Above about 7 sessions, cutting the count is a legitimate default" (10+ sessions), and no session cut is actually made for the runs.
