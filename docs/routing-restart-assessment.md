# Evaluation restart assessment — 27 September 2026

A fresh manual evaluation is justified and has been started. Restarting unattended nightly
execution is a separate decision; no scheduler has been resumed or installed.

## Verified records

- Canonical `evals/results/REPORT.md` and history end at cycle 22 (`provenance-redesign`),
  2026-09-19T16:36:59Z. Later program-library, trained-evidence, folder and routing changes
  were not represented by a later saved canonical cycle.
- Cycle 1 is labelled `baseline`; cycles 2–4 are labelled `nightly`. There are three
  explicitly nightly-labelled cycles in these records, rather than four.
- Cycle 17's benchmark trend row contains four scored benchmark cases. It is separate
  from the recent isolated 4/40 run stopped by Claude's account limit.
- `launchctl list` shows Daily Pump loaded, with no running PID at inspection, and no
  `com.jonfitness.nightly-eval` job. Cloud pause state was supplied by Jon and was not
  independently checked through the cloud service.
- A fresh minimal Claude CLI check returned OK during this assessment. A minimal probe succeeded once, but the CLI subsequently hit its monthly spend limit again. The stated reset is 2026-09-28 00:50 Asia/Singapore; no Claude process is active.

## Coverage needed after the source additions

The generated library includes generic hybrid goals, but its prompts do not explicitly
mention T2/T5, program-library routing, trained-population evidence, Chalk or Daily Pump.
That does not establish that they are never exercised; it does mean the existing 40-case
benchmark alone is insufficient to demonstrate the newly added paths.

The assessment therefore uses:

1. All 40 existing adversarial benchmark cases on the final Markdown skill hash
   `e7ee73b282a89372`, via Claude (switched at Jon's explicit instruction), with independent answer,
   rubric-grade and consistency turns.
2. Ten final-state targeted cases, native eval IDs 10–19, via independent Claude answer
   and reference-aware evaluator turns. These cover track prerequisites, two-day schedules,
   REVL peak stacking, preserving custom plans, evidence versus exact implementation rules,
   eligible pure strength peaks, T2, T5, Chalk limits and Daily Pump exclusion.
3. Four of those Claude targeted checks (IDs 16–19) specifically cover the new-source routes.

All results remain in isolated local workspaces, separate from canonical nightly history
and optimizer input. Exact source patch, snapshots, prompts, outputs, scores and continuation
commands are linked in `docs/routing-clarification-handoff.md`. Codex was stopped at 24/40 cases; those archived results are not evidence
of Claude behavior. No directly comparable baseline has been run for the final state.

Daily Pump is still on hold as a usable reference: capture infrastructure is not an analyzed
program foundation. Tests check that the coach does not import it prematurely. Chalk remains
supplemental observed material, not proof of program superiority.

## Before unattended nightly execution resumes

- Confirm the cloud checkout contains the source state intended for evaluation. Current
  clarification edits are local and uncommitted, so a cloud pull cannot obtain them yet.
- Review manual failures and incomplete checks; obtain a complete Claude benchmark if the
  intended production runner remains Claude. Do not add up older or different-runner scores.
- Review partial-run handling: `run_cycle.py` returns 0 if any selected case scores;
  `nightly.sh` uses the exit status before continuing to optimization/commit/push. A partially
  scored cycle can therefore be treated as successful. This was observed in the earlier
  isolated attempt. The scripts have not been changed in this assessment.
- Reconcile schedules if using the local fallback: the plist still specifies three fires
  (22:35, 02:35, 06:35), whereas current cloud documentation specifies two, after previous
  usage-window collisions. No launch agent was installed or changed.
- Preserve guarded optimizer requirements, including a clean tree and existing regression
  and category-improvement checks. Do not use alternative-runner rows as production results.

## Result status

Claude scored 31/40 final-state benchmark cases (mean 4.20/5), with 2 rubric hard-failure
rows for incorrect pinpoint course citations (ADV-007 and ADV-016). It completed 9/10 targeted
grades. T2 routing passed in targeted case 16, but the answer omitted conditioning-experience
and placement questions. Case 13 omitted some evidence applicability limits. Targeted case 15
has an answer saved but no independent grade. These results are partial and do not establish
that the final skill is ready for unattended scheduling.

The CLI has no running process and reports the next monthly spend reset at 2026-09-28 00:50
Asia/Singapore. Resume using the Claude-only commands in the handoff after reset. No changes
were made to the scheduler, canonical history, or optimizer.
