# Interpretasi Hasil Molecular Docking

## 📖 Daftar Isi
1. [Binding Affinity](#binding-affinity)
2. [RMSD & Pose Quality](#rmsd--pose-quality)
3. [Interaction Analysis](#interaction-analysis)
4. [Scoring Functions](#scoring-functions)
5. [Validation & Quality Control](#validation--quality-control)
6. [Reporting Results](#reporting-results)

---

## Binding Affinity

### ΔG (Gibbs Free Energy)

**Definisi**: Energi Gibbs bebas dari binding
- Dihitung oleh docking engine (AutoDock Vina)
- **Satuan**: kcal/mol
- **Sign**: NEGATIF (exergonic = spontaneous)
- Semakin NEGATIF = semakin KUAT binding

### Interpretasi ΔG

```
ΔG Range           Binding Strength    Interpretation
─────────────────────────────────────────────────────────
< -9.0 kcal/mol    Very Strong         ★★★★★ Excellent inhibitor
-8.0 to -9.0       Strong              ★★★★ Good inhibitor
-7.0 to -8.0       Moderate            ★★★ Moderate inhibitor
-6.0 to -7.0       Weak-Moderate       ★★ Weak inhibitor
-5.0 to -6.0       Weak                ★ Very weak
> -5.0             No binding          ✗ Non-binder
```

### Contoh Interpretasi

| Compound | ΔG | Ki | Interpretation |
|----------|-----|------|-----------------|
| Curcumin | -8.5 | 0.78 µM | Potensial inhibitor, ΔG sangat negatif, afinitas tinggi |
| Quercetin | -7.2 | 8.5 µM | Moderate afinitas, perlu optimasi struktur |
| Kaempferol | -5.8 | 112 µM | Binding lemah, unlikely menjadi inhibitor |

---

## RMSD & Pose Quality

### RMSD (Root Mean Square Deviation)

**Definisi**: Deviasi posisi atom dalam docking poses
- Mengukur **variabilitas pose** dari multiple runs
- **Satuan**: Ångström (Å)
- **Lower RMSD** = lebih stabil pose

### RMSD Interpretation

```
RMSD Value         Meaning                 Quality
───────────────────────────────────────────────────────
< 1.0 Å           Excellent reproducibility    ★★★★★
1.0-2.0 Å         Good reproducibility         ★★★★
2.0-3.0 Å         Acceptable variation         ★★★
3.0-5.0 Å         High variation               ★★
> 5.0 Å           Poor reproducibility         ★
```

### Clustering Poses

**AutoDock Vina menghasilkan multiple modes**:

```
Mode 1 (Lowest energy): -8.5 kcal/mol, RMSD=0.00
  └─ Best binding pose (most favorable)

Mode 2: -8.2 kcal/mol, RMSD=1.50
  └─ Second best, similar pocket region

Mode 3: -7.9 kcal/mol, RMSD=2.10
  └─ Alternative binding mode, different region

Mode 4-10: ...
  └─ Increasingly unfavorable poses
```

**Quality Assessment**:
- Jika **Mode 1 & 2 RMSD < 2.0 Å** → Poses reproducible ✓
- Jika **Mode 1 jauh lebih negatif** → Clear binding ✓
- Jika **semua modes dalam range kcal/mol** → Non-specific ✗

---

## Interaction Analysis

### Tipe Interaksi Protein-Ligand

#### 1. Hydrogen Bonds (H-bonds)

**Karakteristik**:
- **Distance**: D-A < 3.5 Å (ideal: 2.8-3.2 Å)
- **Angle**: D-H-A > 120° (ideal: 150-180°)
- **Donor**: N-H, O-H groups
- **Acceptor**: Lone pair di N, O

**Importance**:
- Utama untuk **specificity**
- Kontribusi ~2-5 kcal/mol untuk binding
- **Highly specific** untuk senyawa yang engineered

**Contoh**:
```
HIS181 (Imidazole) ----[H-bond]---- Carbonyl O (Ligand)
Distance: 2.9 Å ✓
Angle: 165° ✓
→ Strong, specific interaction
```

#### 2. Hydrophobic/Van der Waals Contacts

**Karakteristik**:
- **Distance**: 3.5-4.0 Å (optimal untuk vdW)
- **Non-polar atoms**: C-C, C-H interactions
- **Lipophilic environment** dalam binding pocket

**Importance**:
- **Primary driving force** untuk binding
- Kontribusi ~0.5-1.5 kcal/mol per contact
- Kuantitatif: lebih banyak contacts = lebih kuat binding
- Less specific dibanding H-bonds

**Contoh**:
```
LEU85 (Alkyl side chain) ───[vdW]─── Aromatic ring (Ligand)
Distance: 3.8 Å ✓
→ Hydrophobic burial, favorable
```

#### 3. Aromatic Interactions

**π-π Stacking** (Aromatic-Aromatic):
```
TRP200 (Indole)        Ligand aromatic ring
     ╱                    ╲
(Parallel) Distance: 4.5-5.5 Å
     ╲                    ╱
(T-shaped) Angle: 60-90°

Contribution: ~1-2 kcal/mol
```

**π-alkyl Interactions**:
- Aromatic ring dengan alkyl chain
- Distance: 4.0-5.5 Å
- Weaker than π-π

#### 4. Electrostatic/Ionic Interactions

**Salt Bridges** (Cation-Anion):
```
ARG residue (positively charged) ─────[ionic]─── 
                                      (3.0-3.5 Å)
                                        Phosphate/Carboxylate group
```

**Kondisi**:
- Penting hanya jika **active site ionizable**
- pH dependent
- Kontribusi: ~2-3 kcal/mol per bridge

---

## Interaction Profile Example

### Top Compound Docking Analysis

```
COMPOUND: Curcumin (ΔG = -8.5 kcal/mol, Ki = 0.78 µM)

INTERAKSI TERDETEKSI:

1. HYDROGEN BONDS (3 total):
   ├─ HIS181 ← Carbonyl O (ligand)     [2.9 Å, 165°] ✓✓✓ Strong
   ├─ SER194 ← Hydroxyl O (ligand)     [3.1 Å, 155°] ✓✓ Good
   └─ ASN203 ← Carbonyl O (ligand)     [3.3 Å, 145°] ✓ Acceptable

2. HYDROPHOBIC CONTACTS (12 total):
   ├─ LEU85, VAL87, MET92              [3.6-3.9 Å] ✓✓ Excellent burial
   ├─ PHE112, LEU115                   [3.7-3.8 Å] ✓✓ Good
   └─ PRO156, VAL159                   [3.8-4.0 Å] ✓ Acceptable

3. AROMATIC INTERACTIONS (2 total):
   ├─ TRP200 - Aromatic ring π-π       [4.6 Å, parallel] ✓✓ Strong
   └─ PHE178 - Aromatic ring π-alkyl   [4.8 Å] ✓ Weak

4. ELECTROSTATIC:
   └─ None detected (ASP/GLU too far)

ASSESSMENT:
─────────
- Banyak H-bonds dengan key residues → SPECIFIC
- Extensive hydrophobic burial → STRONG AFFINITY
- π-π stacking dengan TRP200 → FAVORABLE
→ OVERALL: Excellent ligand candidate ★★★★★
```

---

## Scoring Functions

### AutoDock Vina Scoring

Vina menggunakan **empirical scoring function**:

```
ΔG = ΔG_vdw + ΔG_hbond + ΔG_desolvation + ΔG_torsion

Components:
1. Van der Waals (vdw)
   - Repulsive term (short distances)
   - Attractive term (optimal distances)
   
2. Hydrogen bonding
   - Directional component
   - Distance-dependent
   
3. Desolvation
   - Penalty untuk lose hydration
   - Solvent entropy changes
   
4. Rotatable bonds
   - Penalty untuk lose flexibility
   - Per rotatable bond: ~0.1-0.3 kcal/mol
```

### Ligand Properties Effect

```
Property            Effect on ΔG    Interpretation
──────────────────────────────────────────────────
Molecular Weight    Positive (worse) Heavy ligands harder to bind
LogP (Lipophilicity) Negative (better) Lipophilic ligands score better*
H-bond Donors       Variable        Beneficial jika match donors
H-bond Acceptors    Variable        Beneficial jika match acceptors
Rotatable Bonds     Positive (worse) Flexibility penalizes score

*Too lipophilic: poor solubility, ADME issues
Lipinski Rule: MW < 500, LogP < 5, HBD < 5, HBA < 10
```

### Scoring Reliability

**Vina Scoring Accuracy**:
- **Typically**: ± 1.0-1.5 kcal/mol error
- **Ranking**: Usually reliable untuk top compounds
- **Absolute values**: Less accurate (use for ranking, not absolute prediction)

---

## Validation & Quality Control

### Positive Control

**Harus**: Test dengan known inhibitor untuk validate protokol

```
Known Inhibitor:
- Should score ΔG << -7.0 kcal/mol
- Atau match literature values

Example: Pleconaril (HRV inhibitor)
- Literature: Ki ~10 nM (ΔG ≈ -9.5 kcal/mol)
- Your docking: ΔG = -9.3 kcal/mol
- Validation: ✓ Protokol working (±0.2 kcal/mol acceptable)
```

### Cross-Validation

**Multiple Poses Ranking**:

```
If consistent ranking dalam top-5:
- Compound A always rank 1-3
- Compound B always rank 2-4
- Compound C always rank 5-8

→ Ranking robust, reliable untuk prioritization
```

### Comparison dengan Literatur

Jika ada literature data untuk senyawa yang sama:

```
Compound X:
- Your docking ΔG: -7.2 kcal/mol
- Literature ΔG: -7.5 kcal/mol
- Difference: 0.3 kcal/mol ✓ Excellent agreement

Compound Y:
- Your docking ΔG: -6.5 kcal/mol
- Literature ΔG: -8.2 kcal/mol
- Difference: 1.7 kcal/mol ✗ Poor agreement (investigate)
```

---

## Reporting Results

### Essential Data untuk Report

#### 1. Binding Affinity Table

```markdown
| Rank | Compound | ΔG (kcal/mol) | Ki (µM) | RMSD (Å) | H-bonds |
|------|----------|:-------------:|:-------:|:--------:|:-------:|
| 1 | Curcumin | -8.5 | 0.78 | 1.2 | 3 |
| 2 | Quercetin | -8.2 | 1.1 | 1.5 | 2 |
| 3 | Kaempferol | -7.9 | 1.5 | 2.1 | 2 |
| ... | ... | ... | ... | ... | ... |
```

#### 2. Top Compounds Description

**Format**:
```
TOP 5 BINDING COMPOUNDS:

1. CURCUMIN (ΔG = -8.5 kcal/mol)
   Source: Curcuma longa (Turmeric)
   Interactions: 3 H-bonds, 12 hydrophobic contacts, π-π stacking
   Assessment: Excellent binder, strong inhibitor potential
   Structure-Activity: Phenolic OH groups critical for H-bonding
   
2. QUERCETIN (ΔG = -8.2 kcal/mol)
   ...
```

#### 3. Interaction Summary

```
INTERACTION STATISTICS:

H-bond analysis:
- Average H-bonds per top compound: 2.4
- Most common partner: HIS181 (5/5 compounds)
- H-bond contribution: ~12% of total ΔG

Hydrophobic burial:
- Average vdW contacts: 11.2 per compound
- Key residues: LEU85, MET92, TRP200
- vdW contribution: ~75% of total ΔG

Aromatic interactions:
- Frequency: 60% of top compounds
- π-π stacking dengan TRP200: 4/5 compounds
- Contribution: ~8% of total ΔG
```

#### 4. Visualization

**Gambar yang diperlukan**:
- Binding affinity distribution histogram
- Top compound 3D docking poses
- 2D interaction diagrams
- RMSD vs Affinity scatter plot

---

## Common Pitfalls & Interpretation Errors

### Error 1: Overinterpreting Absolute ΔG

❌ **Wrong**: "ΔG -8.5 means Ki exactly 0.78 µM"
✓ **Correct**: "ΔG -8.5 suggests low µM affinity range"

**Reason**: ±1.5 kcal/mol error = 20-30× Ki uncertainty

### Error 2: Single Pose Analysis

❌ **Wrong**: Analyze hanya Mode 1
✓ **Correct**: Check top 3 modes, assess consistency

### Error 3: Ignoring RMSD

❌ **Wrong**: High RMSD (4-5 Å) OK jika ΔG good
✓ **Correct**: High RMSD suggests unreliable pose

### Error 4: No Positive Control

❌ **Wrong**: Assume protokol works tanpa validation
✓ **Correct**: Test dengan known inhibitor dulu

### Error 5: Overweighting H-bonds

❌ **Wrong**: "5 H-bonds = best binder"
✓ **Correct**: Quality H-bonds + hydrophobic burial keduanya penting

---

## Advanced Interpretation

### RMSD Clustering

**Pose clustering strategy**:

```
All 10 modes → Cluster by RMSD < 2.0 Å

Cluster 1 (Biggest cluster):
- Modes 1, 2, 3
- RMSD within cluster: 0.5-1.8 Å
- Mean ΔG: -8.3 kcal/mol
→ MOST LIKELY binding mode

Cluster 2:
- Modes 4, 5
- RMSD: 3.2 Å dari Cluster 1
- Mean ΔG: -7.5 kcal/mol
→ Alternative binding mode (less likely)

Outliers:
- Modes 6-10
- RMSD > 4 Å
- ΔG worse
→ Likely artifacts (ignore)
```

### Consensus Scoring

Jika gunakan multiple docking engines:

```
Vina ΔG:     -8.5
AutoDock4:   -8.7
Glide SP:    -8.2
─────────────────
Consensus:   -8.5 ± 0.25 kcal/mol

Agreement yang baik → CONFIDENCE TINGGI untuk ranking
```

### Structure-Activity Relationship (SAR)

```
Analyzing multiple compounds:

Curcumin (ΔG -8.5): Dua fenolic OH + lipophilic core
Quercetin (ΔG -8.2): Tiga OH groups + ring A conjugation
Kaempferol (ΔG -7.9): Dua OH groups

PATTERN: Additional phenolic OH → Better binding
RECOMMENDATION: Test derivatives with more OH groups
```

---

## Decision Making Based on Results

### Compound Selection Criteria

```
FOR EXPERIMENTAL VALIDATION:

Select if:
1. ΔG < -7.5 kcal/mol (strong binder)
2. RMSD < 2.5 Å (reproducible pose)
3. ≥2 favorable interactions (H-bonds atau π-stacking)
4. Good drug-likeness (MW, LogP, etc)
5. Consistent ranking dalam top-10

High Priority:
- ΔG < -8.0 kcal/mol
- Top reproducible pose
- Multiple complementary interactions

Medium Priority:
- ΔG -7.5 to -8.0
- Good pose reproducibility
- Interesting SAR trends

Low Priority:
- ΔG -6.5 to -7.5
- Or poor pose reproducibility
- Or unusual interaction profiles
```

---

## References untuk Interpretasi

1. **Vina Scoring**: Trott & Olson 2010
2. **Interaction Analysis**: Leung et al. 2021
3. **Validation Methods**: Agarwal et al. 2010
4. **SAR Analysis**: Böhm et al. 2005

---

**Last Updated:** May 23, 2024

**Next**: Baca REFERENCES.md untuk publikasi terkait
