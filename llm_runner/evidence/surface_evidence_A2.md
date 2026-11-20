# Surface evidence package (electrostatic surface potential calculations)

Method summary: The AlphaFold 3 top-ranked human (UniProt Q9NZK5, residues 30-511) and pig (P58780, residues 25-510) ADA2 dimer models (seed 101, templates on) were prepared with PDB2PQR at pH 7.4 and the electrostatic potential was calculated with APBS at ionic strengths of 0 M and 0.15 M. Per-residue surface potential (kT/e; positive means a more positive surface) was sampled 3 A outward from each atom, keeping only points at least 2.5 A from every atom, and averaged over chains A and B. Residues use UniProt numbering. Human and pig residues were paired with the human-pig residue correspondence from the sequence track.

Depends on: the AlphaFold 3 models from the structure track; the human-pig residue correspondence (draft). These are calculations, not measurements of DNA binding, glycosaminoglycan binding, specificity or activity. Zinc ions and glycans were not included in the calculation.

Status: DRAFT until checked by a second person.

## SURF-01  (human vs pig; calculation)
Residues: UniProt Human 30–511; pig 25–510 (all surface-sampled residues)
Observation: At 0.15 M, the human dimer has more strongly positive surface residues than the pig dimer. Human: 223 surface residues, mean +0.36 kT/e, 16 above +3 kT/e, 8 below −3 kT/e. Pig: 232 surface residues, mean +0.12 kT/e, 6 above +3 kT/e, 7 below −3 kT/e.
Value: Mean +0.36 vs +0.12 kT/e; residues > +3 kT/e: 16 vs 6
Method: PDB2PQR (pH 7.4; AMBER-type naming in .pqr) + APBS; per-residue surface potential sampled 3 Å outward from each atom, kept only if ≥2.5 Å from every atom; nearest grid point; averaged over chains A and B; surface_findings.py v2
Uncertainty: Counts depend on the +3 kT/e cut-off and on the surface-sampling rule; chain A and B values agree closely for the residues checked.
Limitations: pH 7.4 only; no zinc (removed by PDB2PQR) or glycans; approximate surface sampling.
Interpretation (not an observation): Positive potential is a possible interaction clue only; it does not measure DNA/GAG binding, specificity or activity.

## SURF-02  (human vs pig; calculation)
Residues: UniProt Human 30–50; pig 25–45
Observation: At 0.15 M, surface residues in this segment average +2.30 kT/e in human (17 residues) and +0.56 kT/e in pig (16 residues). Both species have 5 Lys/Arg here. Largest aligned differences: human Met44 +5.40 vs pig Met39 +0.69 kT/e; human Arg49 +2.24 vs pig Gln44 −0.57 kT/e (R→Q substitution).
Value: Region mean +2.30 vs +0.56 kT/e
Method: PDB2PQR (pH 7.4; AMBER-type naming in .pqr) + APBS; per-residue surface potential sampled 3 Å outward from each atom, kept only if ≥2.5 Å from every atom; nearest grid point; averaged over chains A and B; surface_findings.py v2
Uncertainty: Chain A/B: human Met44 +5.32/+5.47; pig Met39 +0.67/+0.71. Residues sampled at 5–18 points.
Limitations: Difference is not explained by Lys/Arg count alone (5 vs 5); cause not determined. Alignment stable for all positions.
Interpretation (not an observation): Positive potential is a possible interaction clue only; it does not measure DNA/GAG binding, specificity or activity.

## SURF-03  (human vs pig; calculation)
Residues: UniProt Human 389–400; pig 386–397
Observation: This is the most positive human surface region found. At 0.15 M, human surface residues here average +6.83 kT/e (5 residues) vs +0.45 kT/e in pig (5 residues). Human Arg395 is +11.19 kT/e; the aligned pig residue Trp392 is −0.57 kT/e, the largest human–pig difference among the 199 aligned positions sampled in both species (11.76 kT/e). Human His391 is +15.02 kT/e. Sequence differences in this segment: R395W, T396A, Y397D, S398A, K400R (human→pig).
Value: Region mean +6.83 vs +0.45 kT/e; Arg395 vs Trp392: +11.19 vs −0.57 kT/e
Method: PDB2PQR (pH 7.4; AMBER-type naming in .pqr) + APBS; per-residue surface potential sampled 3 Å outward from each atom, kept only if ≥2.5 Å from every atom; nearest grid point; averaged over chains A and B; surface_findings.py v2
Uncertainty: Few sample points (Arg395: 1–2 per chain; His391: 2 per chain). Chain A/B: Arg395 +10.33/+12.05; His391 +15.39/+14.64.
Limitations: His391 was assigned as positively charged (HIP) by PDB2PQR at pH 7.4; its value depends on that protonation choice. Pig His388 was not surface-sampled, so His391 has no pig comparison. Region chosen after inspecting the data (exploratory).
Interpretation (not an observation): Positive potential is a possible interaction clue only; it does not measure DNA/GAG binding, specificity or activity.

## SURF-04  (human vs pig; calculation)
Residues: UniProt Human 460–500; pig 457–497
Observation: At 0.15 M, surface residues average +0.71 kT/e in human (19 residues) and −0.33 kT/e in pig (21 residues). Three human Lys positions are non-positive residues in pig: K466T (human +5.62 vs pig +0.94 kT/e), K498E (+0.58 vs −3.47 kT/e), K499E (+1.03 vs −1.62 kT/e). Lys/Arg count in segment: human 8, pig 6; Asp/Glu: human 4, pig 6.
Value: Region mean +0.71 vs −0.33 kT/e
Method: PDB2PQR (pH 7.4; AMBER-type naming in .pqr) + APBS; per-residue surface potential sampled 3 Å outward from each atom, kept only if ≥2.5 Å from every atom; nearest grid point; averaged over chains A and B; surface_findings.py v2
Uncertainty: Chain A/B: human Lys466 +5.58/+5.67; pig Thr463 +0.72/+1.17; pig Glu495 −3.44/−3.50.
Limitations: Region boundaries chosen after inspecting the data (exploratory). Effect size per region is small compared with SURF-03.
Interpretation (not an observation): Positive potential is a possible interaction clue only; it does not measure DNA/GAG binding, specificity or activity.

## SURF-05  (human and pig; calculation)
Residues: UniProt Human His112, His114, His356, Asp441; pig His107, His109, His353, Asp438
Observation: Null result for species comparison: the only sampled ligand position is strongly negative in both species and similar (human His114 −20.34 kT/e; pig His109 −19.73 kT/e at 0.15 M). The other three ligand positions were not surface-sampled in either species.
Value: −20.34 vs −19.73 kT/e
Method: PDB2PQR (pH 7.4; AMBER-type naming in .pqr) + APBS; per-residue surface potential sampled 3 Å outward from each atom, kept only if ≥2.5 Å from every atom; nearest grid point; averaged over chains A and B; surface_findings.py v2
Uncertainty: Single sample point per chain; pig chain A/B −17.94/−21.51.
Limitations: The AlphaFold 3 input models contain one Zn2+ per chain, but PDB2PQR removed the zinc ions (no HETATM records in the .pqr). The active-site potential therefore lacks the metal's positive charge and is expected to be artificially negative. Treat as a preparation artifact, not a biological feature.
Interpretation (not an observation): No species difference observed; not evidence for or against any mechanism.

## SURF-06  (human and pig; calculation)
Residues: UniProt All surface residues; regions R1–R3
Observation: Changing ionic strength from 0 M to 0.15 M lowers potentials (median change human −1.69, pig −1.50 kT/e) but preserves the residue ranking (Spearman correlation 0.95 human, 0.97 pig). The human-more-positive direction holds at 0 M in all three regions: R1 +6.34 vs +2.48, R2 +11.91 vs +2.77, R3 +3.32 vs +1.03 kT/e.
Value: Spearman 0.95 / 0.97; median shift −1.69 / −1.50 kT/e
Method: PDB2PQR (pH 7.4; AMBER-type naming in .pqr) + APBS; per-residue surface potential sampled 3 Å outward from each atom, kept only if ≥2.5 Å from every atom; nearest grid point; averaged over chains A and B; surface_findings.py v2
Uncertainty: Only two ionic strengths tested.
Limitations: 0 M is unphysiological and used only as a robustness check.
Interpretation (not an observation): Robustness check, not a new biological observation.

## SURF-07  (human and pig; method note)
Residues: All
Observation: Calculations used pH 7.4 only, ionic strength 0 and 0.15 M, dimer models (chains A and B) with zinc removed during PDB2PQR preparation and no glycans. Structure files were renumbered to UniProt numbering with renumber_pqr.py (human +29, pig +24; coordinates unchanged, so the APBS maps still apply); the conversion matched every sampled residue (441/441 human, 460/460 pig). Only 199 aligned positions were surface-sampled in both species. Positions 151–156 and 509–510 (human) have uncertain alignment and were excluded from regional comparisons. Source structures: AlphaFold 3 top-ranked models (seed 101, templates on) from structure_prediction/shared_models/: HUM_ADA2_mature30-511_dimer_Zn_s101_model0.cif and PIG_ADA2_mature25-510_dimer_Zn_s101_model0.cif.
Method: PDB2PQR (pH 7.4; AMBER-type naming in .pqr) + APBS; per-residue surface potential sampled 3 Å outward from each atom, kept only if ≥2.5 Å from every atom; nearest grid point; averaged over chains A and B; surface_findings.py v2
Uncertainty: Surface sampling is approximate (nearest grid point, single outward direction); residues sampled at 1 point are less reliable.
Limitations: Second pH not tested. Zinc present in the source models was removed by PDB2PQR; a rerun with zinc kept would remove this limitation.
