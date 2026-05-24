# Panduan Penggunaan - Step-by-Step Workflow

## 📋 Daftar Isi
1. [Persiapan Awal](#persiapan-awal)
2. [Protein Preparation](#protein-preparation)
3. [Ligand Preparation](#ligand-preparation)
4. [Grid Preparation](#grid-preparation)
5. [Molecular Docking](#molecular-docking)
6. [Analysis & Visualization](#analysis--visualization)

---

## Persiapan Awal

### Step 1: Setup Project

```bash
# Clone repository (jika pertama kali)
git clone https://github.com/your-username/hrv-2r06-molecular-docking.git
cd hrv-2r06-molecular-docking

# Atau jika sudah clone, update
git pull origin main

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# atau: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r scripts/requirements.txt
```

### Step 2: Download Required Data

```bash
# Download PDB structure dari RCSB PDB
# Option A: Command line
pip install biopython
python scripts/download_pdb.py --pdb-id 2R06 --output data/protein/

# Option B: Manual
# 1. Visit https://www.rcsb.org/structure/2R06
# 2. Click "Download" > PDB Format
# 3. Save ke data/protein/2R06.pdb

# Option C: Command line wget/curl
cd data/protein/
wget https://files.rcsb.org/download/2R06.pdb
cd ../..

# Verify download
ls -lh data/protein/2R06.pdb  # Should show file size
```

### Step 3: Organize Ligand Data

```bash
# Struktur folder untuk ligand
mkdir -p data/ligands/natural_compounds
mkdir -p data/ligands/ligands_prepared

# Menempatkan senyawa ke folder
# Bisa dari:
# 1. PubChem (download SDF files)
# 2. ChemSpider (download MOL2)
# 3. Literatur (struktur dari publikasi)

# Contoh struktur:
data/ligands/
├── natural_compounds/
│   ├── compound_001.sdf      # SMILES atau MOL format
│   ├── compound_002.pdb
│   └── compound_catalog.csv  # Spreadsheet dengan metadata
└── ligands_prepared/
    └── (akan diisi oleh scripts)
```

### Step 4: Create Ligand Catalog

**File: `data/ligands/ligands_catalog.csv`**

```csv
ID,Name,Source,Plant_Name,SMILES,MW,LogP,HBD,HBA,File
001,Curcumin,PubChem,Curcuma longa,CC1=C(C(=O)C(=C1O)C=CC2=CC(=C(C=C2)O)OC)O,368.38,3.97,3,6,compound_001.sdf
002,Quercetin,PubChem,Multiple,O1C=C(O)C2=C1C=C(O)C(O)=C2O,302.24,1.78,5,7,compound_002.sdf
003,Kaempferol,PubChem,Allium cepa,O1C=C(O)C2=C1C=C(O)C(O)=C2,286.24,1.38,4,6,compound_003.sdf
...
```

---

## Protein Preparation

### Step 1: Open Protein di Chimera

```bash
# Launch UCSF Chimera
chimera

# Atau buka dari GUI:
# Applications > UCSF Chimera > Chimera
```

**Dalam Chimera:**

```
1. File > Open
2. Navigate ke data/protein/2R06.pdb
3. Click Open
4. Struktur protein muncul di viewer (3D)
```

### Step 2: Inspect & Clean Protein

**Chimera Commands:**

```chimera
# Show sequences
Tools > Sequence > Sequence Viewer

# Remove crystallographic waters
select water
delete selected

# Remove ligands/heteroatoms (jika perlu)
select heteroatom & ~protein & ~nucleic
delete selected

# Check for missing atoms
Tools > Sequence > Alignment > Check for missing loops
```

### Step 3: Add Hydrogens & Prepare

**Using Dock Prep (built-in Chimera tool):**

```chimera
# Prep untuk docking
Tools > Structure Editing > Dock Prep

# Window muncul dengan options:
# - ✓ Add hydrogens
# - ✓ Add charges (Gasteiger)
# - ✓ Merge non-polar hydrogens
# - ✓ Delete water/ligands

# Click "Apply" untuk apply semua
# Click "Write Pdb..." untuk save
# Nama: 2R06_prepared.pdb (di data/protein/)
```

**Alternative: AutoDockTools**

```bash
# Launch ADT
adt

# Dalam ADT:
# 1. File > Open > Select 2R06.pdb
# 2. Edit > Hydrogens > Add Polar Only
# 3. Edit > Charges > Compute Gasteiger Charges
# 4. File > Save > Save as PDBQT
#    Nama: 2R06_prepared.pdbqt
```

### Step 4: Run Preparation Script

```bash
# Automated preparation (optional)
python scripts/01_protein_preparation.py \
    --input data/protein/2R06.pdb \
    --output data/protein/2R06_prepared.pdbqt \
    --method chimera

# Atau gunakan skrip yang lebih simple:
python scripts/simple_prep.py --protein 2R06.pdb
```

### Step 5: Verify Prepared Protein

```bash
# Open di PyMOL untuk verify
pymol

# Dalam PyMOL:
# File > Open > 2R06_prepared.pdbqt
# Color > C-alpha trace untuk visualisasi
# Verify: struktur intact, hidrogens added, no clashes
```

---

## Ligand Preparation

### Step 1: Generate 3D Coordinates (if needed)

**For SMILES strings:**

```bash
# Run Python script
python scripts/02a_smiles_to_3d.py \
    --input data/ligands/ligands_catalog.csv \
    --output data/ligands/natural_compounds/ \
    --format sdf
```

**Script content (02a_smiles_to_3d.py):**

```python
#!/usr/bin/env python
"""Convert SMILES to 3D SDF files"""

import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem
import os

def smiles_to_3d(smiles, output_file):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return False
    
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol, randomSeed=42)
    AllChem.UFFOptimizeMolecule(mol)
    
    writer = Chem.SDWriter(output_file)
    writer.write(mol)
    writer.close()
    return True

# Read catalog
df = pd.read_csv('data/ligands/ligands_catalog.csv')

# Generate 3D structures
for idx, row in df.iterrows():
    output = f"data/ligands/natural_compounds/{row['File']}"
    smiles = row['SMILES']
    
    success = smiles_to_3d(smiles, output)
    status = "✓" if success else "✗"
    print(f"{status} {row['ID']}: {row['Name']}")
```

### Step 2: Prepare Ligands dengan PyRx

```bash
# Launch PyRx
pyrx

# Dalam PyRx GUI:
# 1. File > Set Working Directory > Choose project folder
# 
# 2. File > Import Ligands
#    - Navigate ke: data/ligands/natural_compounds/
#    - Select ALL: Ctrl+A
#    - Click "Open"
#
# 3. Ligands list muncul di sidebar kiri
#
# 4. Select semua ligands (Ctrl+A)
#
# 5. Tools > Prepare Ligands (all selected)
#    - Dialog muncul untuk preprocessing options
#    - Settings default usually OK
#    - Click "Prepare"
#
# 6. Wait untuk processing selesai (progress bar)
#
# 7. Prepared ligands otomatis saved sebagai PDBQT
#    - Format: compound_001.pdbqt
#    - Lokasi: PyRx working directory (set step 1)
#
# 8. File > Export > Hasil ada di folder yang dipilih
```

### Step 3: Batch Preparation Script

```bash
# Automated preparation untuk semua ligands
python scripts/02_ligand_preparation.py \
    --input_dir data/ligands/natural_compounds \
    --output_dir data/ligands/ligands_prepared \
    --method pyrx

# Script akan:
# 1. Scan semua files di input_dir
# 2. Konversi ke PDBQT format
# 3. Assign Gasteiger charges
# 4. Identify rotatable bonds
# 5. Save ke output_dir
```

### Step 4: Verify Ligands

```bash
# Check prepared ligands
ls -lh data/ligands/ligands_prepared/

# Verify di PyMOL
pymol data/ligands/ligands_prepared/compound_001.pdbqt
# Struktur 3D harus terlihat reasonable, no overlapping atoms

# Check properties
python scripts/check_ligand_properties.py \
    --input data/ligands/ligands_prepared/
```

---

## Grid Preparation

### Step 1: Open Protein & Define Active Site

**Using AutoDockTools:**

```bash
# Launch ADT
adt

# Dalam ADT:
# 1. File > Open > Load 2R06_prepared.pdbqt
# 2. Struktur muncul di viewer
```

### Step 2: Identify Binding Site

**Option A: Berdasarkan Literatur**

```
HRV 2R06 active site (dari penelitian):
- Location: Canyon antara VP2 dan VP3
- Center: X=45.3, Y=52.1, Z=48.7 Å
- Size: ~25 Å³ grid cukup
```

**Option B: Gunakan Pocket Prediction Tools**

```bash
# Atau gunakan online tools:
# - fpocket (https://mobyle.rpbs.univ-paris-diderot.fr/cgi-bin/portal.py)
# - CASTp (http://sts.bioe.uic.edu/castp/)
# Upload protein, dapatkan koordinat binding pocket
```

### Step 3: Set Grid Center

**Dalam ADT:**

```
ADT Menu:
1. Grid > Macromolecule > Set Map Types
2. Dialog: "Grid Parameters"
3. Masukkan center coordinates:
   - Center X: 45.3
   - Center Y: 52.1
   - Center Z: 48.7

4. Set grid size (grid spacing 0.375 Å default):
   - Number of points X: 25
   - Number of points Y: 25
   - Number of points Z: 25
   
   (25 × 0.375 = 9.375 Å per dimension)

5. Click "Set Grid Center"
6. Grid visualization muncul (wireframe box di viewer)
7. Adjust jika perlu drag corner
```

### Step 4: Generate Grid

```
ADT Menu:
1. Grid > Output > Output GPF File
2. Dialog: Save As
3. Nama: docking_grid.gpf
4. Lokasi: data/reference/
5. Click Save

File generated berisi:
- Grid coordinates
- Atom types
- Spacing parameters
```

### Step 5: Verify Grid

```
# Buka file grid untuk inspect
cat data/reference/docking_grid.gpf

# Contoh output:
npts 25 25 25          # Grid dimensions
gridfld protein.maps   # Output maps
spacing 0.375          # Grid spacing
center_x 45.3          # Center coordinates
center_y 52.1
center_z 48.7
```

---

## Molecular Docking

### Step 1: Run Docking dengan PyRx

```bash
# Launch PyRx
pyrx

# Dalam PyRx GUI:
# 1. Set Working Directory (project root)
# 2. File > Import Ligands > semua PDBQT di ligands_prepared/
# 3. File > Import Receptor > 2R06_prepared.pdbqt
# 
# 4. Docking > Select Docking Engine > AutoDock Vina
#    (Vina recommended: cepat & akurat)
#
# 5. Docking > Configure > Set Parameters:
#    - Exhaustiveness: 8 (default, balance speed vs accuracy)
#    - Number of modes: 10 (generate 10 poses)
#    - Energy range: 3 kcal/mol (filter results)
#    - Center X, Y, Z: 45.3, 52.1, 48.7
#    - Box size X, Y, Z: 25, 25, 25
#
# 6. Check: "Run Docking"
#    - PyRx akan run Vina untuk setiap ligand
#    - Progress bar menunjukkan status
#    - Waktu: 2-10 menit per ligand (tergantung size)
#
# 7. Results:
#    - Pose PDBQT files
#    - Scoring values ΔG
#    - Listing di PyRx window
#
# 8. File > Export Results
#    - Save docking results
#    - Pdb format atau CSV output
```

### Step 2: Command Line Docking (Advanced)

```bash
#!/bin/bash
# Batch docking script

RECEPTOR="data/protein/2R06_prepared.pdbqt"
LIGAND_DIR="data/ligands/ligands_prepared"
RESULTS_DIR="results/docking_results"
OUTPUT_DIR="${RESULTS_DIR}/poses"

mkdir -p $OUTPUT_DIR

# Loop semua ligands
for LIGAND in $LIGAND_DIR/*.pdbqt; do
    LIGAND_NAME=$(basename $LIGAND .pdbqt)
    
    echo "Docking: $LIGAND_NAME"
    
    vina \
        --receptor $RECEPTOR \
        --ligand $LIGAND \
        --center_x 45.3 --center_y 52.1 --center_z 48.7 \
        --size_x 25 --size_y 25 --size_z 25 \
        --num_modes 10 \
        --energy_range 3 \
        --out $OUTPUT_DIR/${LIGAND_NAME}_docked.pdbqt \
        --log $RESULTS_DIR/${LIGAND_NAME}_docking.dlg
    
    echo "✓ Complete: $LIGAND_NAME"
done

echo "All docking complete!"
```

**Run script:**

```bash
chmod +x scripts/batch_docking.sh
bash scripts/batch_docking.sh
```

### Step 3: Monitor Progress

```bash
# Check docking results
ls -lh results/docking_results/

# Count completed jobs
ls results/docking_results/*.dlg | wc -l

# Check specific result
cat results/docking_results/compound_001_docking.dlg | grep "Binding energy"
```

---

## Analysis & Visualization

### Step 1: Extract Binding Affinity

```bash
# Run analysis script
python scripts/04_results_analysis.py \
    --input_dir results/docking_results/ \
    --output results/binding_affinity/

# Script akan:
# 1. Parse .dlg files
# 2. Extract ΔG values
# 3. Calculate Ki
# 4. Sort by affinity
# 5. Generate CSV output
```

**Output: `results/binding_affinity/affinity_summary.csv`**

```csv
Compound,Mode,ΔG_kcal/mol,RMSD_lb,RMSD_ub,Ki_uM
compound_001,1,-8.5,0.000,0.000,0.784
compound_001,2,-8.2,1.523,2.145,1.087
compound_002,1,-7.9,0.000,0.000,1.534
...
```

### Step 2: Interaction Analysis

```bash
# Analyze ligand-protein interactions
python scripts/05_interaction_analysis.py \
    --protein data/protein/2R06_prepared.pdbqt \
    --ligand_dir results/docking_results/ \
    --output results/interaction_analysis/

# Generate files:
# - hydrogen_bonds.csv
# - hydrophobic_contacts.csv
# - all_interactions_summary.json
```

### Step 3: Visualize Top Compounds

```bash
# Launch PyMOL
pymol

# Dalam PyMOL:
# 1. File > Open > data/protein/2R06_prepared.pdbqt
# 2. File > Open > results/docking_results/compound_001_docked.pdbqt
# 3. Show > Cartoon (untuk protein)
# 4. Show > Sticks (untuk ligand)
# 5. Color by element
# 6. Zoom active site: zoom compound_001
# 7. Tools > Analysis > Distances untuk H-bonds
# 8. File > Save > Session untuk save visualization
#    Nama: figures/top_compound_complex.pse
```

### Step 4: Generate Publication Figures

```bash
# Create interaction diagrams
python scripts/create_interaction_diagrams.py \
    --results results/docking_results/ \
    --top_n 5 \
    --output figures/interaction_diagrams/

# Generates:
# - 2D interaction diagrams per compound
# - Ligand-protein contact maps
# - Publication-ready PNG files
```

### Step 5: Statistical Analysis

```bash
# Jupyter notebook untuk analysis
jupyter notebook notebooks/04_Binding_Affinity_Analysis.ipynb

# Dalam notebook:
# - Load affinity data
# - Plot distributions
# - Statistical tests
# - Correlation analysis
# - Identify outliers
```

---

## Workflow Integration

### Complete Pipeline (One Command)

```bash
# Run full workflow
python scripts/00_complete_workflow.py \
    --protein_id 2R06 \
    --ligand_dir data/ligands/natural_compounds \
    --grid_center 45.3 52.1 48.7 \
    --grid_size 25 25 25

# Steps executed automatically:
# 1. Download & prepare protein
# 2. Prepare ligands
# 3. Define grid
# 4. Run docking
# 5. Analyze results
# 6. Generate reports
```

### Resumable Workflow

```bash
# Jika proses terputus, resume dari checkpoint:
python scripts/00_complete_workflow.py \
    --resume \
    --start_from docking  # Resume from docking step
```

---

## Output Organization

```
results/
├── docking_results/
│   ├── compound_001_docking.dlg
│   ├── compound_001_docked.pdbqt
│   ├── compound_002_docking.dlg
│   └── ...
├── binding_affinity/
│   ├── affinity_summary.csv          # Main results
│   ├── top_10_compounds.xlsx
│   └── affinity_distribution.png
├── interaction_analysis/
│   ├── hydrogen_bonds.csv
│   ├── hydrophobic_contacts.csv
│   └── all_interactions.json
└── visualizations/
    ├── top_5_compounds_pymol.pse
    ├── interaction_diagrams/
    └── ligand_protein_complex.png
```

---

## Quick Reference Commands

```bash
# Activate environment
source venv/bin/activate

# Download protein
wget https://files.rcsb.org/download/2R06.pdb -O data/protein/2R06.pdb

# Prepare protein
python scripts/01_protein_preparation.py

# Prepare ligands
python scripts/02_ligand_preparation.py

# Run docking
bash scripts/batch_docking.sh

# Analyze
python scripts/04_results_analysis.py

# Visualize
pymol
jupyter notebook
```

---

**Next Steps:**

- Baca METHODOLOGY.md untuk detail protokol
- Baca RESULTS_INTERPRETATION.md untuk interpretasi hasil
- Lihat notebooks untuk analysis examples

**Last Updated:** May 23, 2024
