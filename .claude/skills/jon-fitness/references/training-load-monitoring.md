# Training load monitoring — quantifying "total load" instead of citing it

**Epistemic status: General knowledge**, same as `coaching-decision-framework.md` — outside
`references/isa-cpt/` entirely. Built because the eval harness found a specific pattern
across 5 scored scenarios (ADV-008, ADV-010, ADV-028, ADV-029, SC-0025): whenever a decision
turns on "is total weekly load too high," the response reaches for REVL's aggregate
movement-pattern percentages (`revl-class-integration.md` §5/§6) and states them as fact,
instead of asking the client for **their own numbers** and computing something concrete.
This file gives you that computation. **Same output rule as the coaching-decision framework:
use these methods, don't name the underlying studies in your response** — describe the
method in plain language, labeled "general knowledge, not the ISA course."

Use this **alongside**, not instead of, the ISA FITT-VP ceilings (Table 9-12 / 11-10) —
those set the qualitative structure (frequency per muscle group, rep/intensity bands); this
gives you a quantitative cross-check when a client can report their own sessions.

---

## 1. Session load — ask for it, don't infer it

**Method (Foster et al., session-RPE):** for any session — REVL class, PT session, a run, a
climbing session, anything — multiply the client's rating of how hard the *whole session*
felt (a single 0–10 rating, taken ~20–30 min after finishing, not mid-session) by the
session's duration in minutes:

```
session load = session RPE (0–10) × duration (minutes)
```

This produces an arbitrary but internally-consistent unit you can sum, average, and compare
across completely different activities — a 45-minute REVL class at RPE 7 (315) and a
20-minute finisher at RPE 9 (180) become comparable numbers instead of two things you can
only compare qualitatively. **You need the client's own RPE and duration for each session
to use this — do not estimate or assume an RPE on their behalf, and do not substitute
REVL's aggregate composition percentages as a stand-in for what this client's sessions
actually cost them.**

## 2. Weekly load, monotony, and strain

- **Weekly load** = sum of all session loads (REVL + PT + anything else) for the week.
- **Monotony** = the week's mean daily load ÷ the standard deviation of daily load across
  the week. High monotony means the load is similar day after day with no easier days built
  in — even at a moderate weekly total, that lack of variation is itself a load-management
  problem the FITT-VP frequency table doesn't directly capture.
- **Strain** = weekly load × monotony. This is the number most worth watching: two clients
  can have the same weekly load total, but the one training hard every single day (high
  monotony) carries substantially higher strain than the one with real light/hard contrast
  across the week.

**Practical use:** you rarely need the exact arithmetic to make a coaching decision — the
useful move is asking enough questions to *estimate* whether the week is monotonous (every
day similarly hard) or has real contrast (clear hard/easy pattern), and treating a
monotonous high-frequency week as higher-priority for a session-count or intensity
reduction than the same total spread with more contrast.

## 3. Trend over time — acute vs. chronic load

**Method:** compare the most recent week's load ("acute") to the rolling average of the
last ~4 weeks ("chronic"). A ratio meaningfully above 1 means this week is a real spike
relative to what the client has been adapted to; a ratio well below 1 means a genuine
easy/deload week.

**Important honesty note — this ratio is a heuristic, not a validated predictive
formula.** The specific numeric "sweet spot" bands sometimes quoted for this ratio in
applied sports-science circles carry real, publicly-debated methodological criticism
(statistical artifacts from the ratio-of-averages calculation, no established causal
mechanism, doesn't generalize cleanly across sports or individuals). **Do not quote a
specific safe/unsafe numeric threshold to a client or PT as if it's an established
fact** — you don't have the training-history data to compute it precisely in a
conversation anyway. Use the *concept* only: "this week is a large step up from what
you've been doing" is a legitimate, useful coaching statement; "your ratio is 1.6 so
injury risk is elevated by X%" is not something you can honestly claim.

## 4. Simple daily wellness screening

Complements the session-load numbers with how the client is actually feeling, cheaply:
rate sleep quality, fatigue, muscle soreness, and stress each on a simple 1–5 or 1–7 scale
(low = good, high = bad), summed into a single daily wellness score. A rising trend across
several days — even before performance visibly drops — is an early, low-cost warning sign
worth acting on before waiting for a missed lift or a bad session to make it obvious. This
is exactly the kind of information `revl-class-integration.md` §15's "screen readiness at
the start of every session" already asks for — this just gives it a simple, trackable
number instead of a one-off vibe check.

## 5. How this changes what you output

- When a scenario turns on "is this client's total load already too high," **ask for their
  actual sessions (activity, duration, felt-effort) for the last 1–2 weeks** before
  reaching for REVL's aggregate percentages. If they can give you even rough numbers, use
  §1–2 above to make the argument concrete ("that's roughly N sessions at a hard effort with
  no easy day in between") instead of citing what REVL's programme looks like *on average*.
- If the client can't give you numbers, say so plainly and fall back to the qualitative
  FITT-VP ceiling approach (`revl-class-integration.md` §12) — don't manufacture precision
  you don't have on either side (REVL's aggregate data or the client's actual load).
- Never present monotony, strain, or the acute:chronic ratio with a numeric threshold
  framed as an established safe/unsafe cutoff — present the *trend* ("stacking hard days
  with no contrast," "this week is a real step up") as the actionable finding.
- Label this whole approach "general knowledge, applied sports-science load-monitoring
  practice, not from the ISA course" whenever you use it — same discipline as
  `coaching-decision-framework.md`.
