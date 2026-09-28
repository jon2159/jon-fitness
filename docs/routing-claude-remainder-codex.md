# Codex continuation of Claude’s nine unfinished benchmark scenarios

Claude stopped at 31/40 on original skill hash `e7ee73b282a89372`. At Jon’s direction, Codex completed the nine missing IDs on an isolated copy of that same hash. **This is nine-case scenario coverage by a different runner, not a 40/40 Claude score.** The rest of Codex’s own original-snapshot assessment is 40/40. No production history was merged.

| Scenario | Codex score / 5 | Consistency / 5 | Hard failures | Review |
|---|---:|---:|---:|---|
| ADV-030 | 3.800 | 5 | 0 | A conditional Masters option was mentioned before the full G1–G7 gate. Keep it strictly contingent. |
| ADV-031 | 4.200 | 5 | 0 | Missed explicit boredom/adherence discussion despite ongoing progress. |
| ADV-034 | 4.200 | 5 | 0 | Did not spell out how a deficit could change between accumulation and intensification. |
| ADV-035 | 3.400 | 5 | 0 | Safety pause and medical referral are supported by Week 04 Ch 5 pp8–10. The grader’s demand for an immediate aerobic prescription conflicts with that blocking symptom; a conditional post-clearance direction could still be clearer. |
| ADV-036 | 4.133 | 5 | 0 | Missed a reduced-frequency or later-phase option and a reassessment trigger. |
| ADV-037 | 4.000 | 5 | 0 | Missed a concrete return-to-training starting dose/progression trigger. |
| ADV-038 | 3.733 | 5 | 0 | Booked all three PT slots despite five REVL classes; a real minimum-dose issue. The grader also treated Volume as supplied, though the answer prompt omitted it. |
| ADV-039 | 4.200 | 5 | 0 | Did not explain clearly how a sustained energy deficit can hinder muscle gain. |
| ADV-040 | 3.000 | 5 | 0 | Grader penalized added work in Peak Week 1, but the answer prompt never supplied the Peak phase. The phase sits only in scenario metadata shown to the grader. The answer should still count total exposure and qualify additions. |

The nine-case Codex mean is **3.852/5**; all nine have consistency grades and no recorded hard failures. These numbers are not directly comparable with Claude’s 31 scores because the runners differ.

## Grading caveats

- **ADV-035 safety conflict:** The prompt reports breathlessness on stairs despite four spin classes. Week 04 Ch 5 p10 lists dyspnea with mild exertion and unusual breathlessness as warning symptoms; p8–9 makes clearance relevant. The answer paused exercise prescriptions and referred for assessment. The scenario’s expected priorities ask for Zone 1–2 work immediately, so its 3.4 score should not be used as evidence to weaken screening.
- **ADV-038 and ADV-040 hidden phase:** `run_cycle.answer_prompt()` passes only the scenario’s `prompt` to the answerer. The grader sees `revl_phase` separately. ADV-038’s prompt omits Volume and ADV-040’s omits Peak Week 1, while their grades fault the answerer for not applying those phases. The prompts or scoring criteria need alignment before treating these as valid phase-specific regressions. ADV-038’s three-booked-slots issue remains independently valid.

## Corrected working revision and native behavior

The source-page/cardio correction is a distinct skill hash `ef1f3756ad4144ab`. Its targeted Codex checks scored **28/30 expectations across ten cases**; 16 and 17 each passed the track-selection checks but omitted prescription/intake details from short selection answers. The key case 15 selected T1/V5 for an eligible pure-strength client without adding conditioning by default. Cases 18 and 19 correctly kept Chalk claims bounded and Daily Pump excluded. See `docs/routing-continuation-results.md` and the local static review at `evals/routing-review-workspace/2026-09-27-codex/revision-2/review.html`.

A separate full corrected-version regression had been started, then stopped when Jon clarified that he wanted only the nine unfinished scenarios continued. Its partial results remain isolated and are **not** a complete regression result. The Claude continuation was also stopped at Jon’s explicit request to use Codex. No scheduler, production harness, optimizer, canonical result history, commit, push, or real client plan was changed.

## Where to continue

Review the nine response/grade rows in `evals/routing-review-workspace/2026-09-27-codex/batch-*/evals/results/`. Before using ADV-035/038/040 to guide a skill edit, fix their scenario expectations or expose the missing phase to the answerer, then re-evaluate them as a separate scenario revision. If assessing the corrected skill as a full regression later, resume its isolated `revision-2/continue_codex.py` and keep that hash separate.
