# Metodologi Penelitian - Molecular Docking HRV 2R06

## 📖 Daftar Isi
1. [Overview](#overview)
2. [Target Protein](#target-protein)
3. [Persiapan Protein](#persiapan-protein)
4. [Persiapan Ligand](#persiapan-ligand)
5. [Docking Protocol](#docking-protocol)
6. [Analisis Hasil](#analisis-hasil)

---

## Overview

Penelitian ini menggunakan pendekatan **structure-based virtual screening** untuk mengidentifikasi potensi inhibitor natural untuk Human Rhinovirus 2R06 (HRV 2R06). Metodologi melibatkan:

1. **Preparasi Struktur** - Cleaning dan optimisasi struktur kristal
2. **Grid Preparation** - Definisi binding site
3. **Molecular Docking** - Simulasi pose binding dengan AutoDock Vina
4. **Scoring & Ranking** - Evaluasi binding affinity (ΔG)
5. **Interaction Analysis** - Karakterisasi mekanisme binding

---

## Target Protein

### Informasi Umum
- **Nama**: Human Rhinovirus 2R06
- **PDB ID**: 2R06
- **Struktur**: Crystal structure (X-ray diffraction)
- **Resolusi**: [Masukkan dari PDB file]
- **Sumber**: RCSB Protein Data Bank (https://www.rcsb.org/structure/2R06)

### Karakteristik Struktur
- **Total atoms**: [N] atoms
- **Protein chains**: [A, B, C, ...]
- **Het groups**: [Cofactor/substrates]
- **Missing residues**: [Jika ada]

### Active Site
- **Lokasi**: [Deskripsi berdasarkan literatur]
- **Residues kunci**: 
  - HIS181 - Hydrogen bonding
  - TRP200 - π-π stacking
  - LEU85, MET92 - Hydrophobic pocket

---

## Persiapan Protein

### 1.1 Download & Initial Inspection
**Software**: UCSF Chimera / PyMOL

**Steps**:
```
1. Download 2R06.pdb dari RCSB PDB
2. Buka di Chimera/PyMOL
3. Periksa struktur:
   - Identify chains
   - Check missing residues
   - Examine ligands & cofactors
```

### 1.2 Protein Cleaning
**Software**: UCSF Chimera

**Steps**:
```
1. Remove crystallographic water molecules (HOH)
   - IMPORTANT: Jangan hapus water yang terlibat dalam H-bonds
   
2. Remove heteroatoms (kecuali yang essential):
   - Hapus crystallographic buffers (MES, PEG, dll)
   - Keepkan cofactors penting untuk binding
   
3. Remove alternative conformations
   - Pilih konformation dengan occupancy tertinggi
   
4. Add missing atoms/loops (jika needed):
   - Modeller atau server predictions
```

**Perintah Chimera**:
```
# Buka file
open 2R06.pdb

# Remove water
delete solvent

# Remove heteroatoms selektif
delete ligand  # atau het tidak penting lainnya

# Check struktur
info atoms
```

### 1.3 Protonation & Charges
**Software**: AutoDockTools / Chimera

**Steps**:
```
1. Add polar hydrogens
   - Essential untuk H-bond calculations
   
2. Assign Gasteiger partial charges
   - Automated charge calculation
   - Penting untuk elektrostatis interactions
   
3. Validate charges:
   - Total charge harus masuk akal
   - Check pH effect (biasanya pH 7.4)
```

**Perintah Chimera**:
```
# Add hydrogens
addh

# Verify struktur
Tools > Structure Editing > Dock Prep
```

### 1.4 Format Conversion
**Software**: AutoDockTools

**Steps**:
```
1. Konversi PDB → PDBQT
   - PDBQT = PDB + Atom types + Charges
   
2. AutoDockTools preprocessing:
   - Launch ADT
   - Load 2R06_cleaned.pdb
   - Edit > Hydrogens > Add Polar Only
   - Edit > Charges > Compute Gasteiger Charges
   - File > Save > Save as PDBQT
```

**Output**: `2R06_prepared.pdbqt`

---

## Persiapan Ligand

### 2.1 Sumber Senyawa
**Database senyawa tanaman obat lokal**:
- PubChem (https://pubchem.ncbi.nlm.nih.gov/)
- ChemSpider (https://www.chemspider.com/)
- Traditional Medicine Database
- Literatur publikasi senyawa bioaktif

**Format input**: SDF, MOL2, PDB, SMILES

### 2.2 3D Coordinate Generation
**Software**: PyRx / RDKit

**Untuk SMILES strings**:
```python
from rdkit import Chem
from rdkit.Chem import AllChem

# Buat molecule dari SMILES
smiles = "CC(=O)Oc1ccccc1C(=O)O"  # Aspirin sebagai contoh
mol = Chem.MolFromSmiles(smiles)

# Add hydrogens
mol = Chem.AddHs(mol)

# Generate 3D coordinates
AllChem.EmbedMolecule(mol, randomSeed=42)
AllChem.UFFOptimizeMolecule(mol)

# Simpan sebagai SDF
writer = Chem.SDWriter("compound_001.sdf")
writer.write(mol)
writer.close()
```

### 2.3 Ligand Preparation
**Software**: PyRx atau AutoDockTools

**PyRx Workflow**:
```
1. Launch PyRx
2. File > Import Ligands > pilih SDF/MOL2
3. Select ligand
4. Tools > Prepare Ligand
   - Automatically:
     * Add polar hydrogens
     * Assign charges
     * Identify rotatable bonds
     * Detect aromatic carbons
5. File > Save > PDBQT format
```

**Manual (AutoDockTools)**:
```
1. Open ADT
2. Ligand > Choose > pilih file ligand
3. Edit > Hydrogens > Add Polar Only
4. Edit > Charges > Compute Gasteiger
5. Ligand > Torsion > Detect Rotatable Bonds
6. Ligand > Output > Save as PDBQT
```

### 2.4 Ligand Validation
**Check**:
- ✅ Proper valence (bonds, charges)
- ✅ 3D structure reasonable (no clashing atoms)
- ✅ Rotatable bonds correctly identified
- ✅ Aromatic rings properly defined

**Tools**: PyMOL, UCSF Chimera

---

## Docking Protocol

### 3.1 Grid Preparation
**Software**: AutoDockTools (ADT)

**Langkah-langkah**:

#### A. Define Grid Center
```
1. Open 2R06_prepared.pdbqt di ADT
2. Identify active site:
   - Literasi-based (dari publikasi)
   - Ligand binding site (dari homolog structure)
   - Pocket prediction tools
   
3. Define center coordinates (X, Y, Z):
   - Gunakan ADT: Grid > Macromolecule > Set Map Types
   - Set center point di active site
   - Biasanya: pusat di bekalan ligand asli atau pocket
```

**Example coordinates**:
```
Center X: 45.3 Å
Center Y: 52.1 Å
Center Z: 48.7 Å
```

#### B. Set Grid Dimensions
```
Grid size recommendations:
- Small ligand (MW < 250): 20 × 20 × 20 Ų
- Medium ligand (250-350): 24 × 24 × 24 Ų
- Large ligand (MW > 350): 30 × 30 × 30 Ų

Standard untuk penelitian ini: 25 × 25 × 25 Ų

Memastikan:
- Grid cukup besar untuk cover binding site
- Grid tidak terlalu besar (computational cost)
```

#### C. Generate Grid
```
ADT: Grid > Output > Output GPF File
Filename: docking_grid.gpf

File akan berisi:
- Grid center coordinates
- Grid spacing (0.375 Å default)
- Atom types untuk scoring
- Ligand file reference
```

### 3.2 AutoDock Vina Docking
**Software**: PyRx (GUI wrapper untuk AutoDock Vina)

**Vina Algorithm**:
- Fast & accurate molecular docking
- Semi-flexible docking (protein rigid, ligand flexible)
- Scoring function based on:
  - Van der Waals interactions
  - Hydrogen bonding
  - Desolvation penalty
  - Torsional penalty

**PyRx Docking Workflow**:

```
1. Launch PyRx
2. File > Set Working Directory
3. File > Import Ligands > pilih semua PDBQT ligand
4. File > Import Receptor > 2R06_prepared.pdbqt
5. Docking > Set Parameters:
   - Exhaustiveness: 8 (balance speed vs accuracy)
   - Number of poses: 10 (untuk sampling poses)
   - Energy range: 3 kcal/mol (filter results)
6. Click "Dock" button
7. Results otomatis tersimpan
```

**Advanced: Command line Vina**
```bash
# Manual Vina execution
vina \
  --receptor 2R06_prepared.pdbqt \
  --ligand compound_001.pdbqt \
  --center_x 45.3 --center_y 52.1 --center_z 48.7 \
  --size_x 25 --size_y 25 --size_z 25 \
  --num_modes 10 \
  --energy_range 3 \
  --out results/compound_001_docked.pdbqt
```

### 3.3 Output Interpretation

**Docking produces**:
1. **DLG file** (Docking Log):
   - Detailed docking information
   - Binding energies untuk semua poses
   - RMSD values
   
2. **PDBQT files**:
   - Koordinat ligand dalam berbagai poses
   - Ranking by predicted binding affinity

**Example output**:
```
Mode 1  (Binding energy: -8.5 kcal/mol, RMSD: 1.23 Å)
Mode 2  (Binding energy: -8.2 kcal/mol, RMSD: 1.50 Å)
Mode 3  (Binding energy: -7.9 kcal/mol, RMSD: 2.10 Å)
...
Mode 10 (Binding energy: -6.5 kcal/mol, RMSD: 5.00 Å)
```

---

## Analisis Hasil

### 4.1 Binding Affinity Analysis
**Tool**: Python scripts (pandas, matplotlib)

**Metrics**:

#### A. ΔG (Gibbs Free Energy)
```
Interpretation:
ΔG < -9.0 kcal/mol  → Very strong binding (inhibitor potensial)
ΔG -7.0 to -9.0     → Strong binding (moderate inhibitor)
ΔG -5.0 to -7.0     → Weak-moderate binding
ΔG > -5.0           → Weak/no binding
```

#### B. Ki (Inhibition Constant)
```
Relationship: ΔG = -RT × ln(Ki)
where: R = 1.987 cal/mol·K, T = 298 K (25°C)

Ki = exp(ΔG/RT)  [in Molar]

Example:
ΔG = -8.5 kcal/mol → Ki ≈ 0.8 µM → Strong inhibitor
ΔG = -6.0 kcal/mol → Ki ≈ 50 µM → Moderate inhibitor
```

#### C. RMSD (Root Mean Square Deviation)
```
RMSD < 2.0 Å      → Reproducible pose (good cluster)
RMSD 2.0-3.0 Å    → Acceptable variation
RMSD > 3.0 Å      → Outlier pose

RMSD mengukur stabilitas pose docking
```

### 4.2 Interaction Analysis
**Software**: Discovery Studio Visualizer / PyMOL

**Tipe Interaksi yang dianalisis**:

#### A. Hydrogen Bonds
```
Kriteria:
- D-A distance < 3.5 Å
- D-H-A angle > 120°
- Donor: N, O dengan H
- Acceptor: N, O dengan lone pair

Importance: Utama untuk specificity & affinity
```

#### B. Hydrophobic/Van der Waals Contacts
```
Kriteria:
- Distance: 3.5-4.0 Å
- Non-polar atom interactions
- Lipophilic binding pocket

Importance: Driving force untuk binding
```

#### C. Aromatic Interactions
```
- π-π stacking (parallel/T-shaped)
- π-alkyl interactions
- Cation-π interactions

Distance: 4.5-5.5 Å (untuk aromatic-aromatic)
```

#### D. Electrostatic/Ionic
```
- Salt bridges
- Cation-anion pairs
- Distance: < 3.5 Å

Penting jika active site ionizable
```

### 4.3 Scoring & Ranking

**Aggregated scoring approach**:

```
Composite Score = w1×ΔG + w2×H-bonds + w3×Hydrophobic + w4×RMSD

Dengan weights:
- w1 = 0.5 (ΔG adalah primary metric)
- w2 = 0.2 (H-bond quality)
- w3 = 0.2 (Hydrophobic burial)
- w4 = 0.1 (Pose reproducibility)
```

**Selection Criteria**:
1. Top binding affinity (ΔG)
2. Favorable interaction profile
3. Drug-likeness (Lipinski rules)
4. Structural novelty

---

## Quality Control & Validation

### Positive Control
```
Docking known inhibitor (dari literatur)
Hasil: harus mendapat ΔG << -7.0 kcal/mol
Validate protocol bekerja
```

### RMSD Analysis
```
- Cluster analysis: group poses dengan RMSD < 2.0 Å
- Best cluster: usually paling likely biologically relevant
```

### Consensus Scoring
```
Jika mungkin: gunakan multiple docking engines
- AutoDock Vina
- AutoDock4
- Glide
Cross-validate rankings
```

---

## Statistical Analysis

### Affinity Distribution
```
Mean ΔG, SD, Median
Identify outliers (very strong atau sangat weak binders)
```

### Correlation Analysis
```
ΔG vs:
- Molecular weight
- LogP (lipophilicity)
- H-bond donors/acceptors
- Number rotatable bonds
```

---

## References untuk Protocol

1. **Docking**: Morris et al. 2009, Trott & Olson 2010
2. **Scoring**: Leung et al. 2021 (review)
3. **Validation**: Agarwal et al. 2010
4. **Local medicinal compounds**: [Insert relevant publications]

---

*Last Updated: May 23, 2024*
