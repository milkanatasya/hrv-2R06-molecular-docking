# 🚀 QUICK START - Panduan Cepat Molecular Docking GitHub

## ⏱️ 5 Menit Setup (TL;DR)

### Langkah 1: Buat Repository GitHub (2 menit)

```bash
1. Visit https://github.com/new
2. Repository name: hrv-2r06-molecular-docking
3. Description: Molecular docking HRV 2R06 with natural compounds
4. Public
5. ✓ Add README, ✓ Add .gitignore (Python), ✓ MIT License
6. Create repository
7. Copy repository URL
```

### Langkah 2: Setup Local (2 menit)

```bash
# Clone repository
git clone https://github.com/YOUR-USERNAME/hrv-2r06-molecular-docking.git
cd hrv-2r06-molecular-docking

# Copy files dari package ini
# (Semua .md, .py, .txt, LICENSE, .gitignore)
```

### Langkah 3: Push Files (1 menit)

```bash
git add .
git commit -m "Initial commit: Molecular docking project setup"
git push origin main
```

**SELESAI!** Repository Anda siap! ✅

---

## 📝 Yang Harus di-Edit Segera

Edit 3 file ini dengan info Anda:

### 1. **README.md** (Atas file)
```markdown
Ubah:
- [Your Author Name]
- [your.email@example.com]
- [Your Institution/Lab Name]
```

### 2. **LICENSE**
```
Ubah:
Copyright (c) 2024 [Your Name]
```

### 3. **.gitignore**
```
Bisa digunakan as-is untuk Python projects
(Tidak perlu edit kecuali ada tool spesifik)
```

---

## 📚 Files Included

| File | Size | Waktu Baca | Penting? |
|------|------|-----------|---------|
| **README.md** | 16 KB | 10 min | ⭐⭐⭐ HARUS |
| **GITHUB_SETUP.md** | 13 KB | 15 min | ⭐⭐⭐ HARUS |
| **USAGE_GUIDE.md** | 15 KB | 15 min | ⭐⭐ Penting |
| **METHODOLOGY.md** | 11 KB | 12 min | ⭐⭐ Penting |
| **INSTALLATION.md** | 12 KB | 12 min | ⭐⭐ Penting |
| **RESULTS_INTERPRETATION.md** | 13 KB | 15 min | ⭐ Reference |
| **requirements.txt** | 1.2 KB | 2 min | ⭐⭐ Penting |
| **.gitignore** | 2.2 KB | 1 min | ⭐⭐ Ready |
| **LICENSE** | 1.1 KB | 1 min | ⭐⭐ Ready |
| **01_protein_preparation.py** | 8.8 KB | 5 min | ⭐ Template |

---

## 🎯 First Week Roadmap

### **Day 1: Setup** (30 min)
- [ ] Buat GitHub repository
- [ ] Clone ke local
- [ ] Copy files
- [ ] Edit README, LICENSE
- [ ] Push pertama

### **Day 2-3: Read Docs** (1-2 jam)
- [ ] Read README.md
- [ ] Read GITHUB_SETUP.md
- [ ] Read INSTALLATION.md
- [ ] Start installing tools

### **Day 4-5: Prepare Data** (2-3 jam)
- [ ] Download PDB structure (2R06)
- [ ] Collect compound structures
- [ ] Create ligand catalog
- [ ] First commit: "Add protein structure & compound list"

### **Day 6-7: Start Docking** (Ongoing)
- [ ] Read USAGE_GUIDE.md
- [ ] Prepare protein
- [ ] Prepare ligands
- [ ] Run docking
- [ ] Commit results regularly

---

## 💻 Common Git Commands

```bash
# Check status
git status

# Add files
git add .          # Semua files
git add filename   # Specific file

# Commit dengan message
git commit -m "Add docking results"

# Push ke GitHub
git push

# Pull latest changes
git pull

# See history
git log --oneline

# Undo last commit (belum push)
git reset --soft HEAD~1

# Check differences
git diff filename
```

---

## 📊 Repository Organization

**Create these folders setelah clone:**

```bash
# Dalam project folder:
mkdir -p data/protein data/ligands/{natural_compounds,ligands_prepared}
mkdir -p results/{docking_results,binding_affinity,interaction_analysis,visualizations}
mkdir -p scripts/utils
mkdir -p notebooks
mkdir -p figures
```

---

## ✅ Pre-Docking Checklist

Sebelum start docking:

- [ ] Repository di GitHub sudah live
- [ ] Local clone working
- [ ] README.md di-edit dengan info Anda
- [ ] INSTALLATION.md di-read
- [ ] Tools sudah install (Chimera, AutoDock, PyRx, PyMOL)
- [ ] Python 3.8+ dengan venv setup
- [ ] PDB file 2R06 sudah download
- [ ] Compound list ready
- [ ] First commit done

---

## 🔄 Regular Workflow

**Every work session:**

```bash
# Start
git pull                    # Get latest changes
# ... do work ...
git add .                   # Stage changes
git commit -m "description" # Commit dengan message
git push                    # Push ke GitHub
```

**After docking run:**

```bash
git add results/
git commit -m "Add docking results for compounds X-Y

- ΔG range: -8.5 to -6.2 kcal/mol
- Top 5 binders identified
- Interaction analysis complete"
git push
```

---

## 🎯 Commit Message Template

```
Subject: Brief description (50 chars max)

Body: More detailed explanation
- What was done
- Key results
- Any issues encountered

Example:
---
Add molecular docking results for natural compounds

- Docked 50 compounds against HRV 2R06
- Top binder: Curcumin (ΔG = -8.5 kcal/mol)
- Binding affinity summary saved to CSV
- Hydrogen bonding analysis complete
```

---

## 🚨 Important Notes

### **Large Files**

❌ Jangan commit:
- Raw .pdb files (>1 MB)
- AutoDock .dlg files yang besar
- Video files
- Binary data

✅ Boleh commit:
- Summary CSV results
- Python scripts
- Documentation
- Small structures (PDBQT prepared)

**Already handled:** .gitignore sudah exclude file besar

### **Sensitive Info**

❌ Jangan commit ke public repo:
- Passwords, tokens
- Email addresses (keep generic)
- Private data

✅ OK untuk research project:
- Methodology
- Results
- Analysis code

---

## 🆘 Quick Help

### Problem: "fatal: not a git repository"

```bash
# Masalah: Bukan di git folder
# Solusi:
cd /path/to/hrv-2r06-molecular-docking
git status  # Should work now
```

### Problem: "nothing to commit"

```bash
# Masalah: Tidak ada file baru
# Solusi:
git status              # Lihat apa yang ada
git add NEW_FILES
git commit -m "message"
```

### Problem: "push rejected"

```bash
# Solusi 1: Pull dulu
git pull origin main
git push

# Solusi 2: Cek token/SSH
ssh -T git@github.com
```

---

## 📞 When to Push?

**Push frequently!** Hindari:
- Commit besar yang menumpuk
- Work tanpa backup

**Good practice:**
- End of each day
- After completing each task
- Before major changes

---

## 🎓 Next Reading

1. **Immediate**: README.md + GITHUB_SETUP.md
2. **Before docking**: INSTALLATION.md + METHODOLOGY.md
3. **During docking**: USAGE_GUIDE.md
4. **After docking**: RESULTS_INTERPRETATION.md

---

## 💡 Pro Tips

### 1. Use .gitkeep untuk empty folders
```bash
find . -type d -empty -exec touch {}/.gitkeep \;
```

### 2. Make .gitignore changes
```bash
# Jika perlu override gitignore:
git add -f large_file.pdb
git commit -m "Add important large file"
```

### 3. Tag releases
```bash
# After publikasi/milestone:
git tag -a v1.0.0 -m "First analysis complete"
git push origin v1.0.0
```

### 4. Branch untuk experiment
```bash
git checkout -b feature/new-compounds
# ... experiment ...
git checkout main
git merge feature/new-compounds
```

---

## ⏰ Time Estimates

| Task | Time |
|------|------|
| GitHub setup | 5 min |
| Read docs | 1-2 hours |
| Install tools | 30-60 min |
| Protein prep | 30 min |
| Ligand prep (50 compounds) | 1-2 hours |
| Docking (50 compounds) | 2-4 hours |
| Analysis & visualization | 2-3 hours |
| First publication-ready result | ~1 week |

---

## 🎉 Conclusion

**Anda sekarang punya:**

✅ Professional GitHub repository setup  
✅ Complete documentation  
✅ Ready-to-use .gitignore & LICENSE  
✅ Code templates  
✅ Clear workflow guide  

**Langkah selanjutnya:**

1. Run GITHUB_SETUP.md steps
2. Read documentation
3. Install tools
4. Start docking!
5. Push results regularly

---

**Questions?** Refer ke file .md yang sesuai atau search GitHub docs

**Ready?** Let's go! 🚀

---

Created: May 23, 2024
