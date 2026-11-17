# Hypotheses from the formal runs (A0 and A3)

Written for: the medical and lab team reviewing the model's hypotheses.

These are hypotheses written by an AI model (`gpt-6-astra`), not findings about ADA2. Nothing here shows that pig ADA2 behaves in any of these ways. Each one is a suggestion with an experiment that could support or reject it.

## What was run

| | A0 | A3 |
|---|---|---|
| Model was given | The question and shared background (CTX-01 to CTX-11: literature, definitions, lab expertise, equipment and facilities) | The same, plus the AlphaFold 3 structure results (STRUCT-01 to STRUCT-08) |
| Runs | 3 (r1, r2, r3) | 3 (r1, r2, r3) |
| Hypotheses returned | 2, 2, 3 | 3, 3, 3 |

Prompt `v1.0`, reasoning effort medium, same settings in every run. The runs were done on 2026-11-17 in random order. Every run completed, and no run cited an evidence ID it was not given. A1 (sequence), A2 (surface) and A4 (all three) have not been run, because the sequence and surface evidence are not ready.

**Question the model was asked:** which differences between human and pig ADA2 could explain the reported lower activity of pig ADA2 on free adenosine, and what other functions might pig ADA2 keep?

## The four ideas, and how often each appeared

| Idea | A0 | A3 |
|---|---|---|
| **1. The protein was prepared or assayed differently.** The gap may come from how much working protein was in the tube, not from different chemistry. | 3 of 3 | 3 of 3 |
| **2. Pig ADA2 prefers other substrates and keeps DNA-related activity.** It may be poor on free adenosine but still bind DNA or convert deoxyadenosine inside DNA. | 3 of 3 | 3 of 3 (in r1 and r2 it is combined with idea 3, in r3 it is a separate hypothesis) |
| **3. A few sequence differences near human positions 281 and 347 change how the enzyme handles its substrate.** | 0 of 3 | 3 of 3 |
| **4. The two chains sit in a slightly different arrangement in pig.** This arrangement could change catalysis while leaving binding intact. | 1 of 3 (as "altered assembly", with no structure data) | 2 of 3 (r1 and r2) |

**What this tells us:**
- **Ideas 1 and 2 do not depend on the structure data.** They appear in every run, with or without it.
- **Idea 3 appears only with the structure data (A3).** It comes from STRUCT-08, the regions where the human and pig predictions differ.
- **Idea 4 is partly from the structure data.** The structure results (STRUCT-03 and STRUCT-04) show a modest, template-independent chain offset in pig. A0 also proposed an assembly difference once, without that evidence.

## What each idea proposes and how it would be tested

**1. Preparation or assay differences** (confidence "low" in four runs, "moderate" in two)
- **Claim:** pig ADA2 may only look less active because less of it was folded, processed, zinc-loaded or assembled in the tested sample, or because the assay conditions differed.
- **Test:** check the actual construct sequences, then make human and pig protein side by side in the same system. Measure protein amount, processing, glycosylation, folding, assembly and zinc content alongside adenosine-to-inosine activity across substrate concentrations.
- **Would weaken it:** the gap persists across independent preparations when those factors are matched, or fixing an identified defect does not restore activity.

**2. Altered substrate preference with DNA-related activity kept**
- **Claim:** pig ADA2 may be poor on free adenosine yet still bind DNA or convert deoxyadenosine inside DNA.
- **Test:** compare free adenosine, free deoxyadenosine, DNA binding and deoxyinosine formation within DNA as separate readouts. Confirm that any product came from the DNA and that the DNA stayed intact.
- **Would weaken it:** pig loses DNA-related activity as much as free-adenosine activity, or DNA binding is not detected while the human control works. Binding without editing would show kept interaction but not kept catalysis.

**3. Sequence differences near positions 281 and 347 (A3 only)**
- **Claim:** local differences near these two regions change how substrate is handled while the overall fold stays intact.
- **Test:** after checking the alignment, map the two regions relative to the active site, zinc site, dimer interface and glycosylation sites. Swap the regions between human and pig, then compare activity, folding and assembly.
- **Would weaken it:** well-folded swaps change nothing, or any change is explained by folding, zinc or assembly. The model notes that these regions' distance to the active site has not been computed.

**4. Different chain arrangement in pig**
- **Claim:** the two chains sit slightly differently in pig, which may change catalysis while leaving DNA or partner binding available.
- **Test:** measure assembly across a protein-concentration series, then use a solution measurement of the chain arrangement if both proteins are dimers with different activity.
- **Would weaken it:** a sensitive readout shows no arrangement difference, or activity is explained entirely by how much intact dimer is present.

## How the runs compared

| Run | Hypotheses (confidence) |
|---|---|
| A0 r1 | 1 preparation (moderate), 2 substrate preference (low) |
| A0 r2 | 1 preparation (low), 2 substrate preference (low) |
| A0 r3 | 1 preparation (low), 2 substrate preference (low), 3 assembly (low) |
| A3 r1 | 1 preparation (low), 2 local sequence plus DNA kept (low), 3 chain arrangement (low) |
| A3 r2 | 1 preparation (low), 2 local sequence plus DNA kept (low), 3 chain arrangement (low) |
| A3 r3 | 1 preparation (moderate), 2 local sequence (low), 3 DNA kept (low) |

- **Same repeats do not give identical answers.** Wording, ordering and confidence labels move between repeats of the same condition. The "moderate" label appears in one A0 run and one A3 run, and the rest are "low".
- **Confidence labels are the model's own rating.** They do not measure how likely a hypothesis is to be correct.
- **The number of hypotheses (two or three) is the model's choice.** The task allows up to three.

## What to keep in mind when reading these

- **Evidence records have not been double-checked.** A second person still needs to verify the CTX and STRUCT records against their sources.
- **The AlphaFold results are predictions.** The chain-arrangement difference in pig comes from predicted structures and has no experimental support.
- **Pig comparisons use the UniProt pig sequence.** It may not match the lab's actual construct.
- **Feasibility is not checked.** The model had the lab context (CTX-07 to CTX-11), but the team should confirm that each proposed experiment can be run.
- **Citations are only checked for existence.** The check confirms the model cited IDs it was given. It does not confirm that it described each record correctly. Read each hypothesis against its cited records.

## Where to find the details

Each run folder (for example `formal_A3_r1_20261117T005705_01_d0a9/`) holds:

| File | Contents |
|---|---|
| `output.md` | The full hypotheses, readable, with the context the model was given. Headings are the JSON keys |
| `output.json` | The same hypotheses as data |
| `input.txt` / `input.json` | The exact text sent to the model |
| `response_raw.json` | The full API response |
| `run.json` | Settings, hashes, token counts and status |

`run_log.csv` has one row per run. `plan_*.json` records the random run order and the settings. Each hypothesis in `output.md` also has the evidence IDs it cited, a possible alternative explanation, what outcome would be expected if it were true, controls and feasibility, and the next decision.
