# Informasi Ligand - HRV 2R06 Molecular Docking Project

**Researcher:** Milka Natasya Purwanto  
**Email:** mlknatsya05@gmail.com  
**Lab:** Laboratorium Bioinformatika  
**Date:** May 23, 2024

---

## 🌿 5 Senyawa Tanaman Obat Lokal Indonesia

### 1. ANDROGRAPHOLIDE (dari Sambiloto)

**Asal Tanaman:**
- Nama Latin: *Andrographis paniculata*
- Nama Lokal: Sambiloto, Hempedu Bumi
- Famili: Acanthaceae

**Informasi Kimia:**
- Struktur: Diterpenoid lactone
- SMILES: `CC(C)C1(C)C(=CC(=O)OC1C2CC(O)C(C)(C)C(=C2C=C3C(=CC(=O)OC3=C)O)C)C`
- Molecular Weight: 350.45 g/mol
- LogP: 3.45
- H-bond Donors: 2
- H-bond Acceptors: 6

**Potensi Biologis:**
- ⭐⭐⭐⭐⭐ Sangat Tinggi
- Imunostimulan kuat
- Antiviral (terbukti terhadap berbagai virus)
- Antiinflamasi
- Bioaktivitas utama sambiloto

**Referensi:**
- Sudarsono et al. (2020). Antiviral properties of andrographolide
- Traditional use: Pengobatan demam, flu, infeksi virus

---

### 2. BAICALEIN (dari Bungli)

**Asal Tanaman:**
- Nama Latin: *Scutellaria baicalensis* (Huang-qin)
- Nama Lokal: Bungli, Scutellaria
- Famili: Lamiaceae

**Informasi Kimia:**
- Struktur: Flavone (5,6,7-trihydroxyflavone)
- SMILES: `O1C=C(O)C2=C1C=C(O)C(=O)C2O`
- Molecular Weight: 270.24 g/mol
- LogP: 2.87
- H-bond Donors: 3
- H-bond Acceptors: 6

**Potensi Biologis:**
- ⭐⭐⭐⭐ Tinggi
- Antioksidan kuat
- Antiviral terhadap virus RNA
- Inhibitor protease virus
- Antiinflamasi

**Referensi:**
- Wang et al. (2019). Baicalein inhibits virus replication
- Traditional use: Pengobatan demam, inflamasi

---

### 3. KAEMPFEROL (dari Kencur)

**Asal Tanaman:**
- Nama Latin: *Kaempferia galanga*
- Nama Lokal: Kencur
- Famili: Zingiberaceae

**Informasi Kimia:**
- Struktur: Flavonol (3,5,7,4'-tetrahydroxyflavone)
- SMILES: `O1C=C(O)C2=C1C=C(O)C(=O)C2O`
- Molecular Weight: 286.24 g/mol
- LogP: 1.38
- H-bond Donors: 4
- H-bond Acceptors: 6

**Potensi Biologis:**
- ⭐⭐⭐ Sedang-Tinggi
- Antioksidan
- Antiviral terhadap berbagai virus
- Antiinflamasi
- Bioavailabilitas baik

**Referensi:**
- Nabavi et al. (2018). Kaempferol: A natural antiviral compound
- Traditional use: Pengobatan pencernaan, antiseptik

---

### 4. APIGENIN (dari Seledri)

**Asal Tanaman:**
- Nama Latin: *Apium graveolens*
- Nama Lokal: Seledri, Celery
- Famili: Apiaceae

**Informasi Kimia:**
- Struktur: Flavone (4',5,7-trihydroxyflavone)
- SMILES: `O1C=C(O)C2=C1C=C(C=C2O)C3=CC(=O)C(=C(C3)O)O`
- Molecular Weight: 270.24 g/mol
- LogP: 2.13
- H-bond Donors: 3
- H-bond Acceptors: 5

**Potensi Biologis:**
- ⭐⭐⭐ Sedang-Tinggi
- Antiviral broad-spectrum
- Inhibitor protease virus
- Antikanker
- Antioksidan

**Referensi:**
- Angulo et al. (2020). Apigenin shows antiviral activity
- Traditional use: Pengobatan inflamasi, antioksidan

---

### 5. QUERCETIN (dari Sirsak)

**Asal Tanaman:**
- Nama Latin: *Annona muricata*
- Nama Lokal: Sirsak, Graviola
- Famili: Annonaceae

**Informasi Kimia:**
- Struktur: Flavonol (3,5,7,3',4'-pentahydroxyflavone)
- SMILES: `O1C=C(O)C2=C1C=C(O)C(O)=C2O`
- Molecular Weight: 302.24 g/mol
- LogP: 1.78
- H-bond Donors: 5
- H-bond Acceptors: 7

**Potensi Biologis:**
- ⭐⭐⭐⭐⭐ Sangat Tinggi
- Antiviral paling kuat di antara flavonol
- Antioksidan super kuat
- Antikanker
- Antiinflamasi

**Referensi:**
- Moghadamtousi et al. (2015). Quercetin: Antiviral effects
- Traditional use: Pengobatan kanker, antioksidan alami

---

## 📊 Perbandingan Senyawa

| Parameter | Andrographolide | Baicalein | Kaempferol | Apigenin | Quercetin |
|-----------|---|---|---|---|---|
| MW (g/mol) | 350.45 | 270.24 | 286.24 | 270.24 | 302.24 |
| LogP | 3.45 | 2.87 | 1.38 | 2.13 | 1.78 |
| H-bond Donors | 2 | 3 | 4 | 3 | 5 |
| H-bond Acceptors | 6 | 6 | 6 | 5 | 7 |
| Famili Kimia | Diterpenoid | Flavone | Flavonol | Flavone | Flavonol |
| Potensi Antiviral | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## 🔬 Target & Metodologi

### Target Protein: Human Rhinovirus 2R06
- **PDB ID:** 2R06
- **Resolusi:** Crystal structure via X-ray diffraction
- **Active Site:** Canyon region antara VP2-VP3
- **Mekanisme:** Inhibitor binding pada active site untuk block virus attachment

### Docking Protocol
1. **Protein Preparation:** UCSF Chimera / AutoDockTools
2. **Ligand Preparation:** PyRx / RDKit
3. **Molecular Docking:** AutoDock Vina
4. **Analysis:** Binding affinity, interaction profile
5. **Visualization:** PyMOL, Discovery Studio

### Expected Output
- ΔG (binding free energy) untuk setiap senyawa
- H-bond networks
- Hydrophobic contacts
- Ranking senyawa dengan potensi tertinggi
- Publication-ready figures

---

## 💡 Signifikansi Penelitian

1. **Struktur-Based Drug Discovery**
   - Computational screening senyawa natural
   - Efisien dan cost-effective
   - Mendukung pengembangan obat berbasis bukti ilmiah

2. **Sumber dari Tanaman Lokal Indonesia**
   - Biodiversity Indonesia yang kaya
   - Pengetahuan tradisional + metode modern
   - Potensi untuk pharmaceutical development

3. **Target Virus Rhinovirus**
   - HRV penyebab common cold
   - Belum ada antiviral spesifik tersedia
   - Potensi untuk therapeutic development
   - Public health relevance

4. **Metodologi Open Science**
   - Reproducible protocol
   - Available data & code
   - Contribution ke scientific community

---

## 📝 Struktur File untuk Docking

```
data/ligands/natural_compounds/
├── andrographolide.sdf (atau .pdb)
├── baicalein.sdf
├── kaempferol.sdf
├── apigenin.sdf
└── quercetin.sdf
```

**Format:** SDF atau PDB dengan 3D coordinates
**Status:** Ready untuk UCSF Chimera preparation

---

## 🚀 Langkah Selanjutnya

1. ✅ Ligand catalog ready
2. ⏳ Download/generate struktur 3D
3. ⏳ Protein preparation (HRV 2R06)
4. ⏳ Ligand preparation (PyRx)
5. ⏳ Molecular docking (AutoDock Vina)
6. ⏳ Results analysis & visualization
7. ⏳ Documentation & publication

---

**Created by:** Milka Natasya Purwanto  
**Laboratory:** Laboratorium Bioinformatika  
**Date:** May 23, 2024  
**Status:** Ready for Docking Analysis
