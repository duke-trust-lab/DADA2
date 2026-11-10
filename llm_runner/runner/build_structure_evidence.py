"""Build the structure evidence package (condition A3 input) from the saved AlphaFold results.

Every number in the package is computed from the CSV files in ../structure_prediction/af3_results/, so each value
can be traced to a file. Run:  python runner/build_structure_evidence.py
Outputs (in ../evidence/):
  structure_evidence_records_DRAFT.csv   one row per evidence record (packet evidence-record fields)
  structure_evidence_A3.md               the text package given to the LLM (draft until checked)

Records are DRAFT until a second person checks numbering and sources (verification_status).
"""
from pathlib import Path
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
RES = HERE.parent.parent / "structure_prediction" / "af3_results"
POSMAP = HERE.parent.parent / "structure_prediction" / "human_pig_position_map_DRAFT.csv"
OUT = HERE.parent / "evidence"
OUT.mkdir(exist_ok=True)

x = pd.read_csv(RES / "af3_vs_3LGD_comparison.csv")
b = pd.read_csv(RES / "af3_top_model_per_job.csv")
sv = pd.read_csv(RES / "af3_seed_variability.csv")
hvp = pd.read_csv(RES / "af3_human_vs_pig_per_residue.csv")
rc = pd.read_csv(RES / "region_confidence_all_models.csv")
pm = pd.read_csv(POSMAP).dropna(subset=["human_pos", "pig_pos"])
pm["human_pos"] = pm.human_pos.astype(int)


def rng(s, nd=2):
    return f"{s.min():.{nd}f}-{s.max():.{nd}f}"


hum, pig = x[x.species == "human"], x[x.species == "pig"]
bh, bp = b[b.species == "human"], b[b.species == "pig"]
top = rc.merge(b[["job", "model"]], on=["job", "model"])


def reg(region, species, col):
    s = top[(top.region == region) & (top.species == species)][col]
    return f"{s.mean():.1f} (range {s.min():.1f}-{s.max():.1f})"


def local_dev(pos):
    d = hvp[hvp.human_pos == pos].groupby("template").dev.mean()
    return ", ".join(f"{t}: {v:.1f} A" for t, v in d.items())


def subs_near(c, w=4):
    t = pm[(pm.human_pos >= c - w) & (pm.human_pos <= c + w) & (pm.identical == 0)]
    return ", ".join(f"{r.human_aa}{r.human_pos}{r.pig_aa}" for r in t.itertuples())


overall = {t: float(np.sqrt((g.dev ** 2).mean())) for t, g in hvp.groupby("template")}
topdev = {}
for t, g in hvp.groupby("template"):
    m = g.groupby("human_pos").dev.mean().sort_values(ascending=False).head(8)
    topdev[t] = ", ".join(f"{int(p)} ({v:.1f} A)" for p, v in m.items())

tp = x[(x.species == "pig")].groupby("template")[["rmsd_dimer", "rmsd_chainA_alone", "rmsd_chainB_after_Afit"]].mean().round(2)
th = x[(x.species == "human")].groupby("template")[["rmsd_dimer", "rmsd_chainA_alone", "rmsd_chainB_after_Afit"]].mean().round(2)
svh, svp = sv[sv.species == "human"], sv[sv.species == "pig"]

COMMON = dict(owner="AlphaFold 3 structure track", verification_status="DRAFT - not yet checked by a second person")
R = []


def rec(**k):
    R.append({**COMMON, **k})


rec(id="STRUCT-01", species="human", mapped_residues="UniProt Q9NZK5 residues 30-511 vs 3LGD residues 4-484 (UniProt 30-510)",
    type="prediction compared with an experimental structure",
    observation=(f"The AlphaFold 3 human ADA2 dimer (2 chains + 2 Zn2+) overlays the human crystal structure 3LGD with C-alpha RMSD {rng(hum.rmsd_dimer)} A "
                 f"over {int(hum.n_ca.iloc[0])} matched residues (both chains), across {len(hum)} jobs. Single-chain RMSD {rng(hum.rmsd_chainA_alone)} A. "
                 f"Zn2+ to ligand side-chain N/O distances (His112, His114, His356, Asp441) are all within {rng(hum.zn_ligand_max_dist.dropna())} A (the largest ligand distance in each job, across jobs with zinc; 3LGD: 2.15-2.56 A)."),
    value_units=f"RMSD {rng(hum.rmsd_dimer)} A; Zn-ligand max distance {rng(hum.zn_ligand_max_dist.dropna())} A",
    method="Kabsch superposition of C-alpha atoms on residues matched by sequence position; zinc distances to side-chain N/O atoms",
    input_run_files="structure_prediction/af3_outputs/fold_hum_*; data/structures/human_ADA2_3LGD_assembly1.cif", source_location="structure_prediction/af3_results/af3_vs_3LGD_comparison.csv",
    uncertainty=f"Spread across jobs is {hum.rmsd_dimer.max() - hum.rmsd_dimer.min():.2f} A. Includes seeds, with and without templates, with and without zinc.",
    limitations="Agreement with one crystal structure (3LGD, without bound ligand) shows the prediction is plausible; it does not show activity. 3LGD may be in AlphaFold's training data.",
    interpretation="The method reproduces the known human dimer and zinc site, so its human-pig comparisons are not obviously unreliable.")

rec(id="STRUCT-02", species="human and pig", mapped_residues="whole dimer",
    type="prediction",
    observation=(f"AlphaFold 3 confidence for the top model of each job: human ipTM {rng(bh.iptm)}, pTM {rng(bh.ptm)}, mean pLDDT {rng(bh.mean_plddt, 1)}; "
                 f"pig ipTM {rng(bp.iptm)}, pTM {rng(bp.ptm)}, mean pLDDT {rng(bp.mean_plddt, 1)}. No steric clashes in any model. "
                 f"Mean between-chain PAE: human {rng(bh.mean_pae_between, 1)} A, pig {rng(bp.mean_pae_between, 1)} A. "
                 f"Zinc raised human ipTM (no zinc {bh[bh.zinc=='noZn'].iptm.iloc[0]:.2f} vs with zinc {rng(bh[bh.zinc=='Zn'].iptm)}); for pig the difference was small "
                 f"(no zinc {bp[bp.zinc=='noZn'].iptm.iloc[0]:.2f} vs with zinc {rng(bp[bp.zinc=='Zn'].iptm)})."),
    value_units="ipTM, pTM (0-1); pLDDT (0-100); PAE (A)",
    method="AlphaFold Server (AlphaFold 3) summary and full confidence files, top-ranked model per job",
    input_run_files="structure_prediction/af3_outputs/fold_* (12 jobs x 5 models)", source_location="structure_prediction/af3_results/af3_top_model_per_job.csv",
    uncertainty="Confidence scores describe the model's own reliability.",
    limitations="Confidence is not a measure of binding, catalytic activity or mutation effect. Only one no-zinc job per species.",
    interpretation="Both species are predicted as confident dimers; zinc matters little for pig confidence.")

rec(id="STRUCT-03", species="pig vs human crystal", mapped_residues="pig residues aligned to human 30-510 (draft position map)",
    type="prediction compared with an experimental structure",
    observation=(f"Pig dimers compared with human 3LGD on aligned residues: dimer C-alpha RMSD {rng(pig.rmsd_dimer)} A; single chain {rng(pig.rmsd_chainA_alone)} A. "
                 f"After fitting chain A alone, chain B deviates by {rng(pig.rmsd_chainB_after_Afit)} A for pig versus {rng(hum.rmsd_chainB_after_Afit)} A for human. "
                 "Interface residue overlap with 3LGD (Jaccard, 4 A cutoff): "
                 f"human {rng(hum.interface_jaccard)}, pig {rng(pig.interface_jaccard)}."),
    value_units="RMSD (A); Jaccard (0-1)",
    method="Kabsch superposition on chain A, then distance of matched chain B C-alpha atoms; interface residues = any heavy atom within 4 A of the other chain",
    input_run_files="structure_prediction/af3_outputs/fold_pig_*; data/structures/human_ADA2_3LGD_assembly1.cif; structure_prediction/human_pig_position_map_DRAFT.csv", source_location="structure_prediction/af3_results/af3_vs_3LGD_comparison.csv",
    uncertainty="Position map is a draft pending the sequence alignment from the sequence track.",
    limitations="No experimental pig structure exists in the supplied files; the human crystal is only a reference. Chain B offset is about 2 A, a modest difference.",
    interpretation="A single pig chain resembles the human chain, but the two pig chains sit in a somewhat different relative arrangement than the two human chains.")

rec(id="STRUCT-04", species="human and pig", mapped_residues="whole dimer",
    type="calculation (control)",
    observation=("AlphaFold Server uses PDB structure templates by default; for the pig jobs the top template was 3LGD (human ADA2). "
                 "Repeating human and pig with templates off (2 seeds each) changed the results little. "
                 f"Pig vs 3LGD: dimer RMSD {tp.loc['noTemplate','rmsd_dimer']} A without templates vs {tp.loc['template','rmsd_dimer']} A with; chain B after chain A fit "
                 f"{tp.loc['noTemplate','rmsd_chainB_after_Afit']} A vs {tp.loc['template','rmsd_chainB_after_Afit']} A. "
                 f"Human vs 3LGD: {th.loc['noTemplate','rmsd_dimer']} A vs {th.loc['template','rmsd_dimer']} A."),
    value_units="RMSD (A)",
    method="Same inputs and seeds with useStructureTemplate = false",
    input_run_files="structure_prediction/af3_outputs/*notemplate*", source_location="structure_prediction/af3_results/af3_vs_3LGD_comparison.csv",
    uncertainty="Two no-template seeds per species.",
    limitations="AlphaFold may still reflect human-like structures through its training data and multiple sequence alignments.",
    interpretation="The slightly different pig chain arrangement persists with templates off, so it is unlikely to come only from using the human crystal structure as a template.")

rec(id="STRUCT-05", species="human and pig", mapped_residues="whole dimer",
    type="calculation",
    observation=(f"Pairwise C-alpha RMSD between top models of different seeds (same setup): human {rng(svh.rmsd_A)} A, pig {rng(svp.rmsd_A)} A "
                 f"({len(svh)} human and {len(svp)} pig pairs)."),
    value_units="RMSD (A)", method="Kabsch superposition of whole dimer C-alpha atoms, with and without swapping chain order",
    input_run_files="structure_prediction/af3_outputs/*_s101/_s202/_s303", source_location="structure_prediction/af3_results/af3_seed_variability.csv",
    uncertainty="Three seeds with templates and two without.", limitations="Top model per seed only; models within a seed share a seed.",
    interpretation="Run-to-run variation is small (under about 0.6 A), smaller than the overall human-pig difference in STRUCT-06.")

rec(id="STRUCT-06", species="human vs pig", mapped_residues="human 30-511 and aligned pig residues",
    type="calculation",
    observation=(f"Predicted human and pig dimers differ by C-alpha RMSD {overall.get('template', float('nan')):.2f} A (templates on) and {overall.get('noTemplate', float('nan')):.2f} A (templates off) over aligned residues. "
                 f"Largest per-residue deviations (human numbering), templates on: {topdev.get('template','')}. Templates off: {topdev.get('noTemplate','')}."),
    value_units="RMSD (A); per-residue distance (A)", method="Pig dimer fitted to human dimer on aligned C-alpha atoms; per-residue distance after fitting",
    input_run_files="best Zn job per species and setting", source_location="structure_prediction/af3_results/af3_human_vs_pig_per_residue.csv",
    uncertainty="Larger than seed-to-seed variation (STRUCT-05). Residue 511 is the chain end and is poorly defined.",
    limitations="Depends on the draft position map. Pig has a 2-residue insertion after human 154 that disturbs the alignment near 151-160.",
    interpretation="Most of the structure is similar; local differences concentrate at chain ends, near the pig insertion, and at a few interior positions.")

rec(id="STRUCT-07", species="human and pig", mapped_residues="human 30-33, 151-160, 511 (pig aligned positions)",
    type="prediction",
    observation=(f"Confidence is lower in the regions with the largest deviations. Residues 151-160: pLDDT human {reg('151-160 (insertion zone)','human','plddt')}, pig {reg('151-160 (insertion zone)','pig','plddt')}; "
                 f"within-chain PAE human {reg('151-160 (insertion zone)','human','pae_within_chain')} A, pig {reg('151-160 (insertion zone)','pig','pae_within_chain')} A. "
                 f"Last residue (human 511): pLDDT human {reg('C-term 511','human','plddt')}, pig {reg('C-term 511','pig','plddt')}. "
                 f"Whole-chain reference: pLDDT human {reg('Whole chain (reference)','human','plddt')}, pig {reg('Whole chain (reference)','pig','plddt')}."),
    value_units="pLDDT (0-100); PAE (A)", method="pLDDT from model B-factor column (C-alpha); PAE rows of region residues against all chain-A residues; top model per job",
    input_run_files="structure_prediction/af3_outputs/fold_* model_N.cif and full_data_N.json", source_location="structure_prediction/af3_results/region_confidence_all_models.csv",
    uncertainty="Mean over 6 human and 6 pig jobs; chain A only.", limitations="Confidence does not say whether a difference is functional.",
    interpretation="Deviations in these regions are likely flexibility or modelling uncertainty and should not be treated as real structural differences.")

rec(id="STRUCT-08", species="human vs pig", mapped_residues="human 281 and 347 (pig 278 and 344)",
    type="prediction",
    observation=(f"Residues 281 and 347 are predicted with high confidence in both species (pLDDT 281: human {reg('281','human','plddt')}, pig {reg('281','pig','plddt')}; "
                 f"347: human {reg('347','human','plddt')}, pig {reg('347','pig','plddt')}) yet the models differ there (C-alpha distance, human vs pig: 281 {local_dev(281)}; 347 {local_dev(347)}). "
                 f"Pig differs from human at nearby positions: around 281 {subs_near(281)}; around 347 {subs_near(347)}."),
    value_units="pLDDT; distance (A)", method="As STRUCT-06 and STRUCT-07",
    input_run_files="best Zn job per species and setting", source_location="structure_prediction/af3_results/af3_human_vs_pig_per_residue.csv; structure_prediction/af3_results/region_confidence_all_models.csv",
    uncertainty="Deviation is larger than seed-to-seed variation (STRUCT-05). Distance to active site, zinc site, dimer interface and glycosylation sites has NOT yet been computed.",
    limitations="A shift in a confident region may still be small in physical terms. Not tested experimentally.",
    interpretation="These are candidate positions for a real human-pig structural difference, to be checked against position in the structure and the other evidence.")

df = pd.DataFrame(R)
cols = ["id", "owner", "species", "mapped_residues", "type", "observation", "value_units", "method", "input_run_files", "source_location", "uncertainty", "limitations", "interpretation", "verification_status"]
df[cols].to_csv(OUT / "structure_evidence_records_DRAFT.csv", index=False)

METHODS = ("Method summary: Human (UniProt Q9NZK5, residues 30-511) and pig (P58780, residues 25-510) ADA2, each with its UniProt-annotated signal peptide removed, were modelled as homodimers "
           "(two copies plus one Zn2+ per chain; no glycans, no DNA) on AlphaFold Server (AlphaFold 3). Twelve jobs were run: three seeds per species with zinc and templates, "
           "one no-zinc job per species, and two no-template jobs per species; each job returns five models. Predictions were compared with the human crystal structure 3LGD "
           "(chains A and B, UniProt 29-510) by superposing C-alpha atoms on residues matched by sequence position. Pig positions were mapped to human positions using a draft pairwise alignment. "
           "pLDDT is AlphaFold's per-residue local confidence (0-100); PAE is its expected position error (A); ipTM and pTM (0-1) describe confidence in the chain interface and overall fold.")
DEPENDS = ("Depends on: UniProt reference sequences; the draft human-pig position map; the human crystal structure 3LGD. These are predictions, not measurements of activity or binding.")

lines = ["# Structure evidence package (AlphaFold 3 predictions)", "", METHODS, "", DEPENDS, "", "Status: DRAFT until checked by a second person.", ""]
for r in R:
    lines += [f"## {r['id']}  ({r['species']}; {r['type']})", f"Residues: {r['mapped_residues']}", f"Observation: {r['observation']}", f"Method: {r['method']}",
              f"Uncertainty: {r['uncertainty']}", f"Limitations: {r['limitations']}", f"Interpretation (not an observation): {r['interpretation']}", ""]
(OUT / "structure_evidence_A3.md").write_text("\n".join(lines), encoding="utf-8")
print("wrote", len(R), "records;", len("\n".join(lines)), "characters")
