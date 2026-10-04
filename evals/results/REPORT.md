# jon-fitness — evaluation performance history

_Auto-written by `evals/run_cycle.py`. 320 trained-distribution runs, 0 generalization, 0 wildcard, across 27 cycles._

## Scoreboard — cycle 27 vs 26

| Metric | Current | Previous | Trend |
|---|--:|--:|:-:|
| Overall (trained) | 3.87 | 3.82 | ↑ |
| Goal alignment | 4.01 | 3.94 | ↑ |
| Load management | 3.90 | 3.92 | → |
| Recovery | 3.82 | 3.80 | → |
| Individualisation | 3.79 | 3.61 | ↑ |
| Programming quality | 3.69 | 3.71 | → |
| Safety | 4.08 | 4.03 | ↑ |
| Consistency (0-5) | 3.43 | 3.41 | → |
| Benchmark overall | 3.87 | 3.82 | ↑ |
| Generalization overall | — | — | — |
| **Hard failures (count)** | **1** | 4 | ↑ |

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
| 23 | 20260928T070006Z | 3 | **4.27** | 4.33 | 4.50 | 4.67 | 4.33 | 3.67 | 4.67 | 3.00 | post-citation-nutrition-fix-verify |
| 24 | 20260928T070841Z | 1 | **4.67** | 5.00 | 5.00 | 4.00 | 5.00 | 4.00 | 5.00 | 5.00 | post-citation-nutrition-fix-verify |
| 25 | 20260928T161340Z | 17 | **4.25** | 4.41 | 4.25 | 4.21 | 4.24 | 4.03 | 4.18 | 4.59 | post-fix-full-benchmark |
| 26 | 20260928T211711Z | 40 | **3.82** | 3.94 | 3.92 | 3.80 | 3.61 | 3.71 | 3.73 | 4.03 | post-fix-full-benchmark |
| 27 | 20261004T115536Z | 36 | **3.87** | 4.01 | 3.90 | 3.82 | 3.79 | 3.69 | 3.92 | 4.08 | regr-poor_decision_hierarchy |

## Latest cycle — weakest dimensions

| Dim | Name | Mean |
|---|---|--:|
| J | progression | 3.61 |
| K | individualisation | 3.72 |
| B | training_specificity | 3.75 |
| D | volume_management | 3.75 |
| H | recovery_compatibility | 3.75 |
| I | exercise_selection | 3.78 |

## Latest cycle — failure categories

| Category | n |
|---|--:|
| poor_decision_hierarchy | 10 |
| insufficient_individualisation | 6 |
| poor_context_interpretation | 2 |
| excessive_rigidity | 1 |
| poor_load_management | 1 |
| missing_knowledge | 1 |

## Latest cycle — most-hit traps

- (1×) Partially writes an 'aggressive' high-volume plan: the default is a full three-session plan, and the stated phase is Build, so by the response's own table it should be cut to about half
- (1×) Partially: prescribes a multi-movement upper-body hypertrophy session rather than a single intervention, though it is low-fatigue and not full-body
- (1×) Partly declined the 'make it harder' request, but replaced it with a plan that adds near-failure effort on the last set, which is a mild form of making sessions harder
- (1×) Asking so many questions that nothing is actionable for tomorrow (partially: long list of question codes S1–S4, S8, P1, P3, P13, P4, P18, X4 plus four 'settle first' items, and the session plan branches into many conditional cases)
- (1×) Partially prescribes a new 6-week block before the diagnosis answers are in, rather than waiting for the answers
- (1×) Mostly accepted machines-only: free-weight exposure is optional, vague and late, with no real transition plan
- (1×) Mild: weighted pull-ups and chin-ups 4x3-5 in both sessions add pulling on top of 4 climbing days, though volume is low and intensity is strength-oriented rather than hypertrophy-range
- (1×) Calling it the 'Russian Squat protocol' (the response uses 'Russian squat protocol' throughout, including in the suggested client line, instead of 'Russian protocols')

## Hard failures in the latest cycle

- **ADV-034** — Possible: it says the deficit should be 'moderate during the wave's hard weeks'. This is a qualitative band, not a calorie or macro target, so it likely does not breach the hard failure. It is borderline.

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
| 23 | 3 | 4.27 |
| 24 | 1 | 4.67 |
| 25 | 17 | 4.25 |
| 26 | 40 | 3.82 |
| 27 | 36 | 3.87 |

## Consistency contradictions — latest cycle

- **ADV-001** — "Place the squat days away from his hinge-led and densest mixed REVL days" and "Run the Masters 2-day variant on the squat only" are given as the default plan, yet the recommendation also says "I haven't opened `russian-strength-program.md` this turn" and has not verified that a Masters 2-day squat-only variant exists or fits. The plan is specific about structure but unsupported on the protocol.
- **ADV-001** — "I'm assuming your client's week matches the captured programme" is used as the basis for the firm statement "Weeks 2–3 of Peak are testing" and "a 1RM barbell deadlift", then "it would be negative this week" is asserted about recovery with no recovery data. Later it asks for sleep, stress and soreness "over the past two weeks". The recovery claim is stated as fact before the data are gathered.
- **ADV-001** — "One light technique primer on the squat" and "No heavy squat or hinge near his REVL testing day" sit alongside "Ask whether he's testing a squat in Peak week 3". The recommendation does not say what happens to the squat primer if a squat test is imminent. This is a minor gap, not a direct conflict.
- **ADV-002** — The plan says "Lower body is already saturated" and "Extra heavy lower-body volume is the fastest way to stall her," yet PT 3 prescribes leg extension and leg curl at 3 × 10–12 each, plus it is a third PT session adding more lower-body volume. The "no barbell" and "different quality" framing doesn't justify this against the stated saturation, though it is gated and labelled "drop it first."
- **ADV-002** — The opening claims the course budget is "2–3 hard sessions per muscle group per week" and that REVL "already spends that on her lower body," but the plan still gives all three PT sessions at "Full plan" volume with PT 3 loading legs. The 8-session rule then says to shorten PT 3 to 30 min or convert it to mobility, which undercuts the 'full' PT 3 as written.
- **ADV-002** — The plan asserts "Because she won't drop a class, the PT hours become the hypertrophy lever" and describes REVL's group format as unable to give "direct arm, rear-delt or side-delt work" as fact, while also admitting the REVL schedule and her actual week are unconfirmed. It states that 'Horizontal pulling' and 'carries' are under-served from a 'keyword count' lower bound. That is a weak basis for building PT 1 around a 'biggest gap'.
- **ADV-002** — The 12–20 weekly sets figure is cited as general knowledge, but the plan never totals the weekly sets per muscle group across PT 1–3 (e.g. back ≈ 13 sets, chest ≈ 7, quads 3). It doesn't show that most muscles reach that dose, so the 'most aggressive' framing and the dose rationale don't line up.
- **ADV-002** — Rear delts, biceps, triceps, laterals, calves and chest each appear in only one PT session per week. That is below the course's '2–3 hard sessions per muscle group per week' budget that the plan itself cites at the top.
- **ADV-003** — "Soreness means changing the pattern, not stopping" under PT sessions is reasonable, but "Don't add loaded squat or hinge work... Don't add leg volume on top of REVL" sits alongside the claim that "Her body is adapting well, so there's no reason to deload yet", stated as a conclusion to tell the client even though the recommendation admits it doesn't know the REVL phase, week, RPE, or total session count. The reassurance is firmer than the evidence it has gathered.
- **ADV-003** — "REVL trains squat and hinge on most sessions in every phase" is stated as a fact about the programme, then hedged in the same bullet as "my inference", so it is not clear whether it is supported.
- **ADV-003** — "Rising lifts point to adaptation, not breakdown" is stated fairly strongly. Rising performance can coexist with accumulating fatigue (functional overreaching), and the recommendation only partly allows for this through the RPE check.
- **ADV-003** — "REVL's Deload is week 7 and is already built in" is stated as fact, while the same answer says the phase and week are unknown and that course material was not re-verified this turn. It is an unsupported specific.
