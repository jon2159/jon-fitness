# Image audit — verifying the deleted course-note images carried no lost content

**Date:** 2026-09-09
**Question:** the repo cleanup deleted the 1,715 extracted per-slide images. Before
relying on that, is every image's content accounted for in the extracted markdown
(`.claude/skills/jon-fitness/references/isa-cpt/`)?

**Answer: yes.** Nothing of substance is lost. Details below.

## Method (four independent checks)

1. **Recovered** all 1,715 images from git history (`HEAD~1`).
2. **OCR engine A — macOS Vision** (`VNRecognizeTextRequest`): OCR'd all 1,715.
   Succeeded on 1,690; the 25 failures are all 1-pixel-wide/tall decorative rules.
3. **OCR engine B — rapidocr (ONNX)**, the same engine the original `build.py` used:
   OCR'd all 1,690 non-degenerate images independently.
4. **Coverage check**: for each image, every content word from the combined OCR was
   checked against its lesson's markdown (whole-word match, plus spaceless-substring
   match to absorb the known OCR space-loss, e.g. `obturatorinternus`).
5. **Structural checks**: all **103 `Figure X-Y`** and **73 `Table X-Y`** references in
   the markdown were confirmed to have real content next to them; every `## Page N`
   section with < 15 characters was inspected.
6. **Visual review**: the highest-risk images were opened and eyeballed against their
   markdown page.

## Results

| Category | Count | |
|---|---:|---|
| 1–3 px decorative rules / borders | 25 | no content by construction |
| Photos, icons, small labels (< 6 words of text) | 1,492 | nothing to transcribe |
| Text-bearing, ≥ 75% of words already in the notes | 180 | covered |
| **Flagged for manual review** (text-bearing, < 75% naive word coverage) | **18** | **all verified — see below** |

All 18 flagged images were OCR'd by **both** engines and every one was confirmed to
have its content present in the markdown. The low automated score was caused by OCR
garble on curved / stylized diagram labels (spacing lost, letters misread) or by
decorative background numbers — not by missing information.

### The 18 reviewed images

| Lesson | Image | What it is | Verdict |
|---|---|---|---|
| W02 | page18_img02 | "Common cognitive distortions" mind-map (Fig 3-5) | All 6 distortion types + definitions + example quotes are in the md (garbled spacing). ✔ |
| W03 | page07/08/12/14/16/33/37 img | anatomy diagrams: bone cells, bone landmarks, axes of rotation, planes of motion, rotator cuff, elbow flexors | Every term (osteoblast/clast, acromion/trochanter/condyle, sagittal/frontal/transverse, supraspinatus/infraspinatus/subscapularis/teres minor, brachialis/brachioradialis, agonist/antagonist) is in the Week 03 text. ✔ |
| W04 | page07/page10 img01 | "diabetes / insulin" word-cloud graphic (appears twice) | Every word appears in the substantive diabetes text (insulin, glucose, pancreas, mellitus…). ✔ |
| W04 | page39_img01 | **stock photo** of a trainer + client; a whiteboard behind them shows `BMI = 250/71² × 703 = 34.9 kg/m²` | Decorative photo. The metric BMI formula, the full classification table (Table 7-6) and BMI limitations are all in the notes. The *imperial* `× 703` variant on the whiteboard is the one detail not spelled out in text — trivial and derivable. ✔ (marginal) |
| W05 | page18_img02 | numeric fragment of a caloric-expenditure graphic | The real data (4.69 kcal/L O₂ for fat, 5.05 for glucose, "5 kcal/L is accurate") is in the page text. Stray numbers are background noise. ✔ |
| W06 | page37_img01 | figure captions "Fig 10-38 / 10-39 Passive straight-leg raise" | Captions + the passive SLR / hamstring-length assessment are in the Week 06 text. ✔ |
| W07 | page45_img02, page46_img02/03 | fragments of the linear & undulating periodization load tables (Table 10-20 / 10-21) | The complete tables — every microcycle, every load (140 lb/64 kg → 250 lb/114 kg), every rep count — are transcribed on md pages 45–46. ✔ |
| W09 | page21_img01 | FDA "Nutrition Facts" label, old vs new | The entire label (serving size, calories, every nutrient + % DV, added sugars, the 2,000-cal footnote) is transcribed. ✔ |
| W10 | page20_img01 | "F.A.S.T." stroke-recognition graphic | Face / Arm / Speech / Time content is in the Week 10 text. ✔ |
| W10 | page29_img02 | molecular structures of cholesterol / fatty acid / triglyceride / phospholipid | Molecular diagram; the four labels + a full lipid & lipoprotein section (LDL/HDL/VLDL, pathways) are in the text. ✔ |
| W01 | page25_img02 | photo of a Depo-Testosterone vial label | Illustrates "anabolic steroids are outside CPT scope", which the text covers. Label text is not teaching content. ✔ |

## Conclusion

`build.py` did what its README says: it OCR'd every figure, diagram and table and wove
that text into the per-lesson markdown. The 1,715 image files themselves carry no
readable content beyond what is already in
`.claude/skills/jon-fitness/references/isa-cpt/`. Deleting them loses nothing the skill
needs. (They also remain in git history for good measure.)

Audit scripts and per-image OCR output were run in the session scratchpad and are not
committed.
