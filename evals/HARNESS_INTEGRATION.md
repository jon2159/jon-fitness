# Generalization + grader-reliability harness — integration notes

New, self-contained modules added (no changes to existing files):

| File | What it is |
|---|---|
| `generate_generalization.py` | Builds `scenarios/generalization.json` — 40 **held-out** scenarios (8 novel goals × 5 structural contexts). Deterministic and stable. Reuses the structural axes from `generate_scenarios.py` but with goal/recovery/constraint vocabulary the training generator never emits, so it's disjoint by construction. Never used for optimization. |
| `wildcards.py` | `generate(n)` → a fresh `claude -p` turn (no skill in context) invents `n` brand-new tricky PT scenarios. Non-deterministic, disposable, exploratory. `--save` writes `results/wildcards/<ts>.json`. |
| `grader_reliability.py` | Self-consistency check. Freezes `grader_fixtures.json` from a real cycle transcript, re-grades each fixture K times, reports per-dimension + composite SD and rank stability → `results/GRADER_RELIABILITY.md`. |
| `grader_validity.py` | Calibration check vs Jon. Grades the human-scored `scenarios/gold/gold_responses.json` with the eval grader, reports MAE + bias per dimension and every ≥2-point disagreement → `results/GRADER_VALIDITY.md`. |
| `scenarios/gold/gold_responses.json` | 8 (scenario, response) pairs spanning the quality range. **Needs Jon to fill `human_scores` A–O before `grader_validity.py` can run.** |

## Remaining wiring (NOT yet applied — `run_cycle.py` / `optimize.py` were being edited by another session)

### 1. `run_cycle.py`

- Add a `set` field to every history row (default `"primary"`).
- After the primary loop, two extra passes, each tagged and written to history with its `set`:
  - `--generalization N` (nightly default 6): least-recently-run from `generalization.json`, tag `set="generalization"`.
  - `--wildcards N` (nightly default 3): `wildcards.generate(N)`, tag `set="wildcard"`, also dump prompts to `results/wildcards/`.
- **Consistency pass** (2nd grader call, `--no-consistency` to skip): after the rubric grade, an independent `claude -p` call that ONLY checks internal physiological coherence against the checklist in `rubric.md` → row fields `consistency_score` (0–5) and `contradictions` (list).
- `write_report()`: split the cycle table by `set`; add a **Current / Previous / Trend** metric block; show hard failures as a tracked **count**; add `consistency_score` and `grader_variance` rows (variance = latest `GRADER_RELIABILITY.md` mean composite SD).

### 2. `rubric.md`

Add a **"Training-science consistency"** section listing the contradictions the consistency pass flags (recovery poor but volume up; high local fatigue + another high-volume session for that area with no justification; hypertrophy volume added without checking REVL exposure; soreness treated as automatic rest signal; no soreness treated as ineffective training; Russian protocol added just because the client asked; BFT/REVL treated as always-reduce; theoretically good plan that doesn't fit the stated schedule).

### 3. `nightly.sh`

- `python3 evals/generate_generalization.py` alongside the scenario regen.
- `run_cycle.py … --generalization 6 --wildcards 3`.
- `grader_reliability.py --k 3` every Nth cycle (writes its own report).
- Guarded `optimize.py --apply`: also gate on the **generalization** composite not regressing by > tol (not just the benchmark).

### 4. `optimize.py`

`rows()` must exclude `set in ("generalization","wildcard")` from anything that drives a proposal — the optimizer sees primary + benchmark only. Generalization is a read-only scoreboard.

## Baseline

The first baseline cycle should run on the **current rubric/grader** (15-dim composite + benchmark + hard-failure count), i.e. before the consistency pass is wired in, so the consistency layer's effect on scores is measurable as a deliberate later change. Generalization can be scored from the first cycle since it doesn't alter the primary metric.
