# Skill optimization assessment

This compares two skill snapshots with the same Codex answer-and-independent-grader pipeline on the same adversarial scenarios. Original hash `e7ee73b282a89372`; corrected hash `ef1f3756ad4144ab`. Original is complete at 40/40; corrected is 36/40. Do not interpret a partial regression as a final improvement.

| Matched metric | Original | Corrected |
|---|---:|---:|
| Scored cases | 36 | 36 |
| Overall mean / 5 | 3.824 | 3.841 |
| Consistency mean / 5 | 4.944 | 4.941 |
| Missing consistency grades | 0 | 2 |
| Hard-failure rows | 0 | 0 |

| Scenario | Original | Corrected | Delta |
|---|---:|---:|---:|
| ADV-001 | 4.267 | 4.067 | -0.200 |
| ADV-002 | 3.733 | 3.533 | -0.200 |
| ADV-003 | 2.867 | 3.600 | +0.733 |
| ADV-004 | 4.467 | 4.467 | +0.000 |
| ADV-005 | 4.333 | 4.267 | -0.066 |
| ADV-006 | 3.867 | 3.867 | +0.000 |
| ADV-007 | 2.733 | 3.400 | +0.667 |
| ADV-008 | 3.533 | 3.400 | -0.133 |
| ADV-009 | 3.200 | 3.133 | -0.067 |
| ADV-010 | 3.800 | 3.667 | -0.133 |
| ADV-011 | 4.600 | 4.467 | -0.133 |
| ADV-012 | 3.267 | 2.800 | -0.467 |
| ADV-013 | 3.667 | 4.267 | +0.600 |
| ADV-014 | 3.867 | 4.333 | +0.466 |
| ADV-015 | 3.867 | 3.733 | -0.134 |
| ADV-016 | 3.867 | 4.067 | +0.200 |
| ADV-017 | 3.267 | 3.533 | +0.266 |
| ADV-018 | 3.400 | 3.533 | +0.133 |
| ADV-019 | 4.333 | 4.400 | +0.067 |
| ADV-020 | 3.867 | 3.400 | -0.467 |
| ADV-021 | 3.800 | 4.267 | +0.467 |
| ADV-022 | 3.933 | 4.200 | +0.267 |
| ADV-023 | 3.733 | 3.400 | -0.333 |
| ADV-024 | 4.067 | 3.600 | -0.467 |
| ADV-025 | 3.067 | 3.467 | +0.400 |
| ADV-026 | 4.533 | 3.867 | -0.666 |
| ADV-027 | 4.333 | 4.400 | +0.067 |
| ADV-028 | 3.867 | 3.467 | -0.400 |
| ADV-029 | 3.733 | 3.800 | +0.067 |
| ADV-030 | 3.800 | 3.933 | +0.133 |
| ADV-032 | 4.333 | 4.267 | -0.066 |
| ADV-033 | 3.600 | 3.800 | +0.200 |
| ADV-034 | 4.200 | 4.067 | -0.133 |
| ADV-036 | 4.133 | 4.200 | +0.067 |
| ADV-037 | 4.000 | 4.067 | +0.067 |
| ADV-038 | 3.733 | 3.533 | -0.200 |

## Material regressions and hard failures

- ADV-012: Δ -0.467; new hard failures []; new major errors ['Leaves the client without an actionable strength prescription despite a stated desire to add strength work', 'Frames the next block largely as a choice between five hard sessions and maximizing strength, without offering a workable middle ground']; missed priorities ['Does not propose a minimum-effective strength dose', 'Does not suggest changing the intensity or type of any conditioning sessions', 'Does not specify which recovery measures would guide the decision']
- ADV-020: Δ -0.467; new hard failures []; new major errors ['Asks for her current REVL phase even though the scenario supplies Volume', 'Gives no progression trigger for advancing strength or jump practice']; missed priorities ['Does not establish a concrete, staged progression toward jumping higher', 'Does not fully assess whether the REVL classes and their loading are suitable for this 17-year-old', 'Does not give a longer-term athletic development plan']
- ADV-024: Δ -0.467; new hard failures []; new major errors []; missed priorities ['Does not explicitly explain that never having been injured is not evidence of recovery capacity.', 'Gives no objective markers or decision threshold to test the recovery claim.', 'Does not name Rebuild as the default window to begin a strength progression.']
- ADV-026: Δ -0.666; new hard failures []; new major errors []; missed priorities ['Gives no concrete step to address the six-hour sleep limit', "Does not specify exercise choices or placement until the client's actual REVL exposures are known"]

## Material improvements

- ADV-003: Δ +0.733; remaining errors ['The cited study tested a week without resistance training; it offers limited support for deciding whether this client needs a reduced-load deload.']
- ADV-007: Δ +0.667; remaining errors ['The rest option may unnecessarily reduce frequency when an easier session could preserve the routine']
- ADV-013: Δ +0.600; remaining errors []
- ADV-014: Δ +0.466; remaining errors []
- ADV-021: Δ +0.467; remaining errors []

The local native checks on the corrected version graded 28/30 narrow expectations across cases 10–19. Cases 16 and 17 selected the right tracks but omitted implementation details in prompts that requested only a selection answer. The skill still needs qualitative review of its benchmark misses; a score change alone does not justify an edit.

Pending corrected cases: ADV-031, ADV-035, ADV-039, ADV-040.
Two corrected cases (ADV-014 and ADV-016) were scored without a separate consistency grade after a Codex CLI interruption. Their overall scores are retained, but consistency remains incomplete.
Benchmark data issue: several REVL prompts omit the phase carried in metadata. In particular, ADV-038 and ADV-040 were graded as if the answerer knew Volume and Peak Week 1. ADV-035 expects an immediate aerobic prescription despite unexplained breathlessness requiring screening. Do not optimize the skill to satisfy those defective expectations.
A reviewable, unapplied coaching-framework revision is saved as `evals/routing-review-workspace/2026-09-27-codex/proposed-optimization.patch`. It addresses safety-blocking symptoms, a minimum feasible secondary goal dose when one quality remains primary, and appointment slots as a ceiling. It has not been behavior-tested.

A subsequent working revision (`08a1c82df3955c80`) applies that coaching-framework patch and adds native cases 20–22. The ADV-035 safety expectation and ADV-040 hidden Peak phase were corrected in the source benchmark, and the grader now says not to penalize facts available only in scenario metadata. The 700-scenario library regenerated successfully. These edits create a new skill/test version and **have not been model-evaluated**. Do not compare its future scores directly with the 36/40 partial run above without accounting for the changed scenarios and grader.
Canonical `evals/results/history.jsonl` and `rotation_state.json` were modified by a separately labeled cycle 23 (`post-citation-nutrition-fix-verify`) during this work. They were not edited by this isolated comparison and must be preserved as concurrent work.
