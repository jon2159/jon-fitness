# REVL programming 2025 — frequency tables (Step 2)

Input: `source/revl_raw_data_2025.md` — **260 screenshots across Blocks 3 and 4 of 2025**
(130 / 130), read by two independent OCR engines. Produced by
`source/analyze_revl.py --blocks 4 5`.

> **Evidence quality.** Stylised posters over photos; both OCR engines misread digits and
> drop small print. **No specific load, %, rep count, tempo or cap here is fact** — treat
> every number as an approximate lower bound. Session/day/phase labels are inferred from
> folder and file names. Presence tables count *keyword presence per session*, not
> rep-weighted volume.

Written analysis and the 2025-vs-2026 comparison live in:
- `REVL Block 3 programming 2025/REVL Block 3 2025 — Analysis.md`
- `REVL Block 4 programming 2025/REVL Block 4 2025 — Analysis.md`
- `source/revl_2025_vs_2026_analysis.md`

---

Sessions analysed: 260  (Block 3 2025: 130, Block 4 2025: 130)

### Movement-pattern presence — share of all sessions

| Pattern | sessions | % |
|---|--:|--:|
| Squat (bilateral) | 172 | 66% |
| Hinge (bilateral) | 165 | 63% |
| Unilateral lower | 137 | 53% |
| Horizontal push | 142 | 55% |
| Vertical push | 109 | 42% |
| Horizontal pull | 74 | 28% |
| Vertical pull | 100 | 38% |
| Carry / loaded hold | 20 | 8% |
| Rotation / anti-rotation | 85 | 33% |
| Core / trunk (non-rot.) | 160 | 62% |
| Olympic / ballistic | 165 | 63% |
| Erg / machine cardio | 188 | 72% |
| Running / locomotion | 84 | 32% |
| Burpee / mixed metcon | 84 | 32% |

### Movement-pattern presence by session type (% of that type's sessions)

| Pattern | Perform Total (n=26) | Perform Lower (n=26) | Perform Upper (n=26) | Move Total (n=26) | Move Upper (n=26) | Move Lower (n=26) | Sweat Sprint (n=25) | Sweat Engine (n=25) | Sweat Team (n=25) | Complete (n=26) |
|---|---|---|---|---|---|---|---|---|---|---|
| Squat (bilateral) | 73% | 96% | 0% | 81% | 4% | 100% | 72% | 88% | 76% | 73% |
| Hinge (bilateral) | 100% | 96% | 4% | 100% | 8% | 100% | 56% | 56% | 44% | 69% |
| Unilateral lower | 81% | 96% | 0% | 81% | 4% | 100% | 16% | 72% | 40% | 35% |
| Horizontal push | 81% | 8% | 100% | 92% | 96% | 0% | 28% | 24% | 28% | 85% |
| Vertical push | 88% | 4% | 62% | 77% | 54% | 0% | 28% | 28% | 36% | 42% |
| Horizontal pull | 19% | 4% | 85% | 23% | 85% | 0% | 0% | 4% | 4% | 62% |
| Vertical pull | 58% | 27% | 73% | 23% | 73% | 8% | 28% | 36% | 36% | 19% |
| Carry / loaded hold | 4% | 23% | 8% | 8% | 0% | 12% | 8% | 8% | 4% | 4% |
| Rotation / anti-rotation | 27% | 35% | 46% | 15% | 81% | 85% | 0% | 0% | 0% | 38% |
| Core / trunk (non-rot.) | 81% | 96% | 31% | 100% | 88% | 81% | 36% | 40% | 40% | 19% |
| Olympic / ballistic | 77% | 77% | 15% | 69% | 38% | 62% | 84% | 88% | 76% | 50% |
| Erg / machine cardio | 27% | 31% | 8% | 88% | 73% | 96% | 100% | 100% | 100% | 100% |
| Running / locomotion | 4% | 0% | 0% | 8% | 0% | 12% | 100% | 80% | 64% | 54% |
| Burpee / mixed metcon | 15% | 4% | 8% | 31% | 12% | 23% | 80% | 64% | 72% | 12% |

### Movement-pattern presence by phase (% of that phase's sessions)

| Pattern | Volume (n=60) | Build (n=60) | Deload (n=20) | Peak (n=60) | Rebuild (n=60) |
|---|---|---|---|---|---|
| Squat (bilateral) | 70% | 65% | 75% | 58% | 68% |
| Hinge (bilateral) | 68% | 60% | 60% | 62% | 65% |
| Unilateral lower | 50% | 50% | 60% | 52% | 57% |
| Horizontal push | 55% | 60% | 50% | 47% | 58% |
| Vertical push | 52% | 40% | 30% | 47% | 33% |
| Horizontal pull | 23% | 30% | 30% | 27% | 33% |
| Vertical pull | 38% | 42% | 35% | 37% | 38% |
| Carry / loaded hold | 12% | 2% | 5% | 7% | 12% |
| Rotation / anti-rotation | 32% | 32% | 35% | 35% | 32% |
| Core / trunk (non-rot.) | 57% | 62% | 65% | 62% | 65% |
| Olympic / ballistic | 65% | 62% | 50% | 68% | 63% |
| Erg / machine cardio | 70% | 72% | 70% | 82% | 67% |
| Running / locomotion | 37% | 32% | 25% | 33% | 30% |
| Burpee / mixed metcon | 28% | 25% | 55% | 32% | 37% |

### Movement-pattern presence by weekday (% of that day's sessions)

| Pattern | Monday (n=52) | Tuesday (n=26) | Wednesday (n=52) | Thursday (n=26) | Friday (n=52) | Saturday (n=26) | Sunday (n=26) |
|---|---|---|---|---|---|---|---|
| Squat (bilateral) | 77% | 73% | 50% | 85% | 50% | 77% | 73% |
| Hinge (bilateral) | 100% | 46% | 52% | 65% | 52% | 46% | 69% |
| Unilateral lower | 81% | 58% | 50% | 31% | 50% | 42% | 35% |
| Horizontal push | 87% | 23% | 52% | 31% | 50% | 31% | 85% |
| Vertical push | 83% | 23% | 29% | 31% | 31% | 38% | 42% |
| Horizontal pull | 21% | 4% | 44% | 0% | 42% | 4% | 62% |
| Vertical pull | 40% | 31% | 50% | 35% | 40% | 38% | 19% |
| Carry / loaded hold | 6% | 15% | 12% | 0% | 10% | 4% | 4% |
| Rotation / anti-rotation | 21% | 0% | 58% | 0% | 65% | 0% | 38% |
| Core / trunk (non-rot.) | 90% | 31% | 92% | 46% | 56% | 42% | 19% |
| Olympic / ballistic | 73% | 85% | 58% | 85% | 38% | 77% | 50% |
| Erg / machine cardio | 58% | 100% | 52% | 100% | 52% | 100% | 100% |
| Running / locomotion | 6% | 92% | 0% | 88% | 6% | 65% | 54% |
| Burpee / mixed metcon | 23% | 85% | 8% | 62% | 15% | 73% | 12% |

### Prescription style by phase (% of that phase's sessions)

| Quality | Volume | Build | Deload | Peak | Rebuild |
|---|---|---|---|---|---|
| %1RM prescribed | 28% | 30% | 30% | 25% | 22% |
| RIR prescribed | 30% | 30% | 0% | 5% | 0% |
| RPE prescribed | 28% | 32% | 35% | 35% | 43% |
| Tempo / eccentric cue | 45% | 37% | 30% | 33% | 32% |
| EMOM / interval density | 75% | 78% | 70% | 55% | 68% |
| AMRAP / for-time | 100% | 100% | 100% | 100% | 100% |
| Partner / team format | 63% | 45% | 75% | 42% | 80% |
| Unbroken / max-effort | 32% | 43% | 30% | 35% | 38% |

### %1RM-looking tokens seen, by phase (raw OCR strings — approximate)

- **Volume:** `45-50-55-60`×12, `50-55-60-65`×12, `40`×12, `40-45-50-55`×6, `30-40`×4
- **Build:** `40`×30, `60-65-70-75`×12, `60-65-75-80-85`×12, `60-70-80-85-90`×12, `40-50`×6
- **Deload:** `40`×18, `40-45-50`×6
- **Peak:** `40`×24, `60-70-80-90-95-95`×12, `60-70-80-90-95-100`×9, `60-70-80-90-100`×8, `40-50`×4, `40-5`×2
- **Rebuild:** `40`×16, `40-50-60`×6, `40-45-50-50`×6, `30-40`×4

### Sessions per phase-week folder

| Folder | Block 3 2025 | Block 4 2025 |
|---|---|---|
| Volume Wk 1 | 10 | 10 |
| Volume Wk 2 | 10 | 10 |
| Volume Wk 3 | 10 | 10 |
| Build Wk 1 | 10 | 10 |
| Build Wk 2 | 10 | 10 |
| Build Wk 3 | 10 | 10 |
| Deload Wk 1 | 10 | 10 |
| Peak Wk 1 | 10 | 10 |
| Peak Wk 2 | 10 | 10 |
| Peak Wk 3 | 10 | 10 |
| Rebuild Wk 1 | 10 | 10 |
| Rebuild Wk 2 | 10 | 10 |
| Rebuild Wk 3 | 10 | 10 |

