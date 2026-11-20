# surface_findings.py  (version 2)
# Turn APBS output (.pqr + .dx) into a per-residue SURFACE potential table,
# so the results can be written up as text findings.
#
# Usage (in the terminal):
#   python surface_findings.py human.pqr human_150.dx human_150
# Output: human_150_residues.csv (sorted from most positive to most negative)
#
# Idea (kept simple):
#   1. Read the coordinates of every atom from the .pqr file
#   2. For each atom, take a point 3 Å further out (away from the protein center)
#   3. Keep the point ONLY if it is really in the water (no other atom too close).
#      This throws away buried atoms, whose values are not surface potentials.
#   4. Read the potential at the kept points and average per residue (units: kT/e)
#      Residues with no kept points are buried and are left out.

import sys
import numpy as np
import pandas as pd
from scipy.spatial import cKDTree

pqr_file = sys.argv[1]
dx_file = sys.argv[2]
label = sys.argv[3]

OFFSET = 3.0       # how far out from the atom we look (Å)
MIN_GAP = 2.5      # the point must be at least this far from every atom (Å)

# ---------- 1. Read the .dx potential grid ----------
origin = None
spacing = []
shape = None
values = []
with open(dx_file) as f:
    for line in f:
        if line.startswith("object 1"):
            shape = [int(x) for x in line.split()[-3:]]
        elif line.startswith("origin"):
            origin = np.array([float(x) for x in line.split()[1:4]])
        elif line.startswith("delta"):
            spacing.append(max(float(x) for x in line.split()[1:4]))
        elif line[0].isdigit() or line[0] == "-":
            values.extend(float(x) for x in line.split())
grid = np.array(values).reshape(shape)
spacing = np.array(spacing)

def potential_at(point):
    # Return the potential at the grid point closest to this point
    i, j, k = np.round((point - origin) / spacing).astype(int)
    i = min(max(i, 0), shape[0] - 1)
    j = min(max(j, 0), shape[1] - 1)
    k = min(max(k, 0), shape[2] - 1)
    return grid[i, j, k]

# ---------- 2. Read the atoms from the .pqr file ----------
rows = []
with open(pqr_file) as f:
    for line in f:
        if line.startswith("ATOM") or line.startswith("HETATM"):
            parts = line.split()
            # pqr format: ATOM serial atom_name res_name [chain] res_num x y z charge radius
            x, y, z = float(parts[-5]), float(parts[-4]), float(parts[-3])
            res_num = parts[-6]
            res_name = parts[3]
            chain = parts[4] if len(parts) == 11 else "-"
            rows.append([chain, res_name, res_num, x, y, z])
atoms = pd.DataFrame(rows, columns=["chain", "res_name", "res_num", "x", "y", "z"])

# ---------- 3. Make one point outside each atom, keep only points in the water ----------
xyz = atoms[["x", "y", "z"]].values
center = xyz.mean(axis=0)
directions = xyz - center
directions = directions / np.linalg.norm(directions, axis=1, keepdims=True)
points = xyz + OFFSET * directions

tree = cKDTree(xyz)
nearest_distance, _ = tree.query(points)
atoms["in_water"] = nearest_distance >= MIN_GAP

# ---------- 4. Read the potential at the kept points ----------
pots = []
for p, ok in zip(points, atoms["in_water"]):
    if ok:
        pots.append(potential_at(p))
    else:
        pots.append(np.nan)
atoms["potential"] = pots

# ---------- 5. Average per residue, sort, and save ----------
surface = atoms[atoms["in_water"]]
table = surface.groupby(["chain", "res_name", "res_num"], as_index=False).agg(
    potential=("potential", "mean"),
    n_points=("potential", "size"),
)
table["potential"] = table["potential"].round(2)
table = table.sort_values("potential", ascending=False)
table["condition"] = label
table.to_csv(label + "_residues.csv", index=False)

n_total = atoms.groupby(["chain", "res_num"]).ngroups
print("Residues on the surface:", len(table), "of", n_total)
print("Top 15 most positive residues (" + label + "):")
print(table.head(15).to_string(index=False))
print("Top 5 most negative residues:")
print(table.tail(5).to_string(index=False))
