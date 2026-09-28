# Routing clarification review — 27 September 2026

`git pull --ff-only origin main` succeeded: already up to date. No commits or pushes were made.

## Changes

- Track suggestions now depend on intake, eligibility, total days, existing classes and recovery.
- Experienced custom clients consult relevant research without automatically importing a program.
- Screening and course-specific population rules retain precedence. External findings and coach judgement are labelled separately.
- Russian autoregulation text distinguishes research support for RPE/RIR from exact triggers and load reductions. Coleman does not directly test the specified reduced-load microcycle.
- The shared engine now explicitly requires a client need for optional activities, accounts for existing activity, and avoids adding off-day cardio as standard.
- Six reusable fictional, read-only cases were added to the native skill eval set (IDs 10–15). Matching files in the local installed `.agents` copy were updated only when they matched the committed baseline.

## Model checks completed before the final shared-table edit

| Case | Observed behavior | Limitations |
|---|---|---|
| 10: PBs + conditioning, two total days | Chose two-day Masters instead of four-day Hybrid | Eligibility items still described as unknown; suggested optional off-day activity |
| 11: novice, size + strength | Chose Foundations rather than T5 | Screening caveat appears after the provisional prescription |
| 12: REVL Peak + PBs | Rejected stacking a Russian peak; asked about actual classes | Overstated lower-body exposure before knowing attendance details |
| 13: working custom plan | Kept plan; skipped waves, sprints and extra sessions | Assumed clearance and quoted course values without opening source pages |
| 14: evidence for exact thresholds | Distinguished study findings from coach-set triggers and reductions | Added further coach-chosen guidance; only reference summaries consulted |
| 15: eligible pure strength peak | Allowed T1 V5 | Added off-day cardio as standard, contrary to the no-default-additions expectation |

Independent response-only grading completed for cases 10–14, passing all 15 stated expectations, with the concerns above. This does not verify tool retrieval or course citation accuracy. Case 15's independent grading failed due to the account limit; manual review found the default-cardio failure.

## Broader benchmark and final-state validation

The standard 40-scenario benchmark was attempted as four independent 10-scenario batches, each retaining separate answer and grader turns. Only 4 distinct scenarios were scored before Claude CLI began failing. The CLI then explicitly reported: “You've hit your monthly spend limit.” This is an incomplete run, not a regression pass, and no comparison demonstrating improvement is claimed.

The final shared-table clarification was added after those responses exposed the default-cardio issue. It has NOT been verified by a fresh model run because the monthly spend limit blocks further calls. Fresh targeted runs and a complete 40-scenario benchmark remain necessary.

Validation completed: `git diff --check`, valid eval JSON with unique IDs, installed-copy parity for changed files. All model runs used isolated repository copies; real client files and canonical nightly results were untouched. Transcripts, grader output and partial benchmark logs are in the adjacent ignored review workspace.
