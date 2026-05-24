# Panduan Setup GitHub Repository

## 🚀 Langkah 1: Persiapan Awal

### 1.1 Create GitHub Account (jika belum ada)

```bash
1. Visit https://github.com/signup
2. Email, username, password
3. Verify email dari GitHub
4. Setup 2FA (recommended)
```

### 1.2 Install Git (Local Machine)

**Windows:**
```bash
# Download dari https://git-scm.com/download/win
# Run installer
# Select "Git from the command line and also from 3rd-party software"
# Verify:
git --version
```

**macOS:**
```bash
# Using Homebrew
brew install git

# Or download dari https://git-scm.com/download/mac
git --version
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install git

git --version
```

### 1.3 Configure Git

```bash
# Set your identity
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Verify
git config --global --list
```

---

## 🔑 Langkah 2: Setup Authentication

### 2.1 Personal Access Token (Recommended)

```bash
# GitHub Website:
1. Settings > Developer settings > Personal access tokens > Tokens (classic)
2. Click "Generate new token"
3. Select scopes:
   ✓ repo (full control of private repositories)
   ✓ gist
   ✓ read:org
4. Copy token & SIMPAN DI TEMPAT AMAN
```

### 2.2 SSH Key Setup (Alternative, lebih secure)

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Press Enter untuk default location
# Enter passphrase (optional tapi recommended)

# Copy public key
# Linux/macOS:
cat ~/.ssh/id_ed25519.pub

# Windows (PowerShell):
type $ENV:USERPROFILE\.ssh\id_ed25519.pub

# GitHub:
1. Settings > SSH and GPG keys
2. Click "New SSH key"
3. Paste public key
4. Click "Add SSH key"

# Test connection:
ssh -T git@github.com
# Output: Hi <username>! You've successfully authenticated...
```

---

## 📁 Langkah 3: Create GitHub Repository

### 3.1 Via GitHub Website

```bash
1. Login ke https://github.com
2. Click "+" di top right > "New repository"
3. Settings:

   Repository name: hrv-2r06-molecular-docking
   Description: Molecular docking analysis of HRV 2R06 with natural compounds
   
   Public / Private: PUBLIC (untuk research sharing)
   
   ✓ Add a README file (kamu akan ganti ini)
   ✓ Add .gitignore > Python
   ✓ Choose a license > MIT License

4. Click "Create repository"
5. Copy repository URL (untuk clone)
```

### 3.2 Initialize Local Repository

```bash
# Option A: Clone empty repo
git clone https://github.com/YOUR-USERNAME/hrv-2r06-molecular-docking.git
cd hrv-2r06-molecular-docking

# Option B: Initialize existing project
cd ~/path/to/project
git init
git remote add origin https://github.com/YOUR-USERNAME/hrv-2r06-molecular-docking.git
```

---

## 📂 Langkah 4: Add Project Files

### 4.1 Project Structure

```bash
# Buat struktur direktori
mkdir -p data/{protein,ligands/natural_compounds,ligands/ligands_prepared,reference}
mkdir -p results/{docking_results,binding_affinity,interaction_analysis,visualizations}
mkdir -p scripts/{utils}
mkdir -p notebooks
mkdir -p docs
mkdir -p figures

# Create .gitkeep untuk empty directories (jika perlu tracked)
find . -type d -empty -exec touch {}/.gitkeep \;
```

### 4.2 Copy Dokumentasi Files

```bash
# Files yang sudah dibuat:
- README.md
- LICENSE
- .gitignore
- requirements.txt
- METHODOLOGY.md
- INSTALLATION.md
- USAGE_GUIDE.md
- RESULTS_INTERPRETATION.md

# Copy ke project root:
cp /path/to/files/* .
```

### 4.3 Add Python Scripts

```bash
# Buat scripts directory
mkdir -p scripts

# Copy atau create:
- 01_protein_preparation.py
- 02_ligand_preparation.py
- 03_docking_execution.py
- 04_results_analysis.py
- 05_interaction_analysis.py
- utils/pdb_utils.py
- utils/docking_utils.py
- requirements.txt
```

### 4.4 Example Notebooks

```bash
# Create notebooks for analysis
mkdir -p notebooks

# Buat template notebooks (.ipynb files)
# Atau create README di notebooks folder
```

---

## 🔄 Langkah 5: First Git Commit

### 5.1 Check Status

```bash
git status

# Output akan menunjukkan:
# Untracked files:
#   README.md
#   LICENSE
#   .gitignore
#   docs/
#   scripts/
#   ... (semua file baru)
```

### 5.2 Add Files

```bash
# Add semua files
git add .

# Atau add specific files
git add README.md LICENSE .gitignore

# Verify
git status
# Output: On branch main, changes to be committed
```

### 5.3 First Commit

```bash
git commit -m "Initial commit: Add project structure and documentation

- README.md dengan overview project
- METHODOLOGY.md dengan protokol penelitian
- INSTALLATION.md dengan setup tools
- USAGE_GUIDE.md dengan workflow
- RESULTS_INTERPRETATION.md
- LICENSE dan .gitignore
- Python script templates untuk protein/ligand prep"
```

### 5.4 Push ke GitHub

```bash
# Set main branch
git branch -M main

# Push
git push -u origin main

# First push: setup tracking branch (-u flag)
# Subsequent pushes: git push

# Verify di GitHub:
# Visit https://github.com/YOUR-USERNAME/hrv-2r06-molecular-docking
# Files seharusnya terlihat di repository
```

---

## 📝 Langkah 6: Add Content Secara Berkala

### 6.1 Workflow untuk Updates

```bash
# 1. Check status
git status

# 2. See differences
git diff filename

# 3. Stage changes
git add filename
# atau stage all:
git add .

# 4. Commit dengan meaningful message
git commit -m "Add protein preparation results

- Prepared structure 2R06.pdbqt
- Removed water molecules
- Added Gasteiger charges"

# 5. Push ke remote
git push
```

### 6.2 When Adding Data

```bash
# Contoh: Adding prepared protein
cd data/protein
# Add prepared structure (tapi jangan PDB files)
git add 2R06_prepared.pdbqt

# Tapi ignore raw PDB files (di .gitignore sudah ada)
git status
# Verify: 2R06.pdb tidak muncul

git commit -m "Add prepared protein structure"
git push
```

### 6.3 When Adding Results

```bash
# Contoh: Adding docking results
cd results/binding_affinity
git add affinity_summary.csv
git add top_10_compounds.xlsx

git commit -m "Add binding affinity analysis results

- Analyzed 150 compounds from docking
- Top 10 compounds identified
- ΔG range: -8.5 to -5.2 kcal/mol"

git push
```

---

## 🌳 Langkah 7: Branch Management (Optional)

### 7.1 Create Feature Branch

```bash
# Develop baru: feature/add-new-compounds
git checkout -b feature/add-new-compounds

# Pakai branch khusus untuk development
# Main branch tetap stable

# Do work:
# - Modify files
# - Test
# - Commit

git add .
git commit -m "Add 50 new compounds to docking queue"

# Push branch ke remote
git push -u origin feature/add-new-compounds
```

### 7.2 Pull Request & Merge

```bash
# Di GitHub:
1. Visit repository
2. Click "Compare & pull request"
3. Title: "Add new compounds for analysis"
4. Description: Detail tentang perubahan
5. Click "Create pull request"
6. Review changes
7. Click "Merge pull request"
8. Confirm merge

# Local:
git checkout main
git pull origin main

# Delete feature branch (local)
git branch -d feature/add-new-compounds

# Delete feature branch (remote)
git push origin --delete feature/add-new-compounds
```

---

## 🏷️ Langkah 8: Releases & Tags

### 8.1 Create Release

```bash
# Create tag untuk specific version
git tag -a v1.0.0 -m "Version 1.0.0: Initial analysis complete

- Analyzed 150 natural compounds
- Identified top 10 binders (ΔG < -7.5)
- Interaction analysis complete"

# Push tags
git push origin v1.0.0

# Push semua tags
git push origin --tags
```

### 8.2 GitHub Release

```bash
# Di GitHub:
1. Go to "Releases" tab
2. Click "Create a new release"
3. Select tag: v1.0.0
4. Title: "Version 1.0.0 - Initial Analysis"
5. Description: Include summary of work
6. Upload files (optional):
   - Hasil CSV
   - Figures
   - Summary PDF
7. Publish release
```

---

## 📊 Langkah 9: GitHub Pages (Optional Documentation)

### 9.1 Enable GitHub Pages

```bash
# GitHub Settings:
1. Go to repository > Settings
2. Scroll to "GitHub Pages"
3. Source: Branch > main
4. Folder: / (root)
5. Click Save

# Atau use docs/ folder:
3. Source: Branch > main
4. Folder: /docs
5. Save
```

### 9.2 Create Website

```bash
# Create index.html di docs/ folder
mkdir -p docs

cat > docs/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>HRV 2R06 Molecular Docking</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        h1 { color: #333; }
        .result { background: #f0f0f0; padding: 10px; margin: 10px 0; }
    </style>
</head>
<body>
    <h1>Molecular Docking: HRV 2R06</h1>
    <p>Analysis of natural compounds against Human Rhinovirus</p>
    
    <h2>Top Results</h2>
    <div class="result">
        <strong>Curcumin</strong>: ΔG = -8.5 kcal/mol
    </div>
    <div class="result">
        <strong>Quercetin</strong>: ΔG = -8.2 kcal/mol
    </div>
    
    <p><a href="https://github.com/your-username/hrv-2r06-molecular-docking">GitHub</a></p>
</body>
</html>
EOF

git add docs/index.html
git commit -m "Add GitHub Pages documentation"
git push
```

**Access**: https://your-username.github.io/hrv-2r06-molecular-docking/

---

## 🎯 Langkah 10: README Best Practices

### 10.1 Update README dengan Repository Info

```markdown
# README.md Template

[Awal README sudah ada di repository - edit dengan info spesifik]

## 📊 Key Results

- **Total compounds analyzed**: 150
- **Top binder**: Curcumin (ΔG = -8.5 kcal/mol)
- **Repository**: github.com/YOUR-USERNAME/hrv-2r06-molecular-docking
- **Status**: ✅ Active Development

## 🔗 Links

- [Full Documentation](docs/)
- [Results Dashboard](https://your-username.github.io/hrv-2r06-molecular-docking)
- [Issues](../../issues)
- [Releases](../../releases)

## 📄 Citation

If you use this work, please cite:

```

Jangan lupa update README dengan actual info!

---

## 🔍 Langkah 11: Collaboration & Contributing

### 11.1 Add Collaborators

```bash
# GitHub:
1. Settings > Collaborators > Add people
2. Invite username/email
3. Select permission level (Maintain/Write)
```

### 11.2 Create Contributing Guidelines

```bash
cat > CONTRIBUTING.md << 'EOF'
# Contributing Guidelines

## How to Contribute

1. Fork repository
2. Create feature branch
3. Make changes
4. Submit pull request

## Code Standards

- Use Python style guide (PEP 8)
- Add docstrings untuk functions
- Include test cases

## Reporting Issues

Use GitHub Issues untuk bugs, features requests
EOF

git add CONTRIBUTING.md
git commit -m "Add contributing guidelines"
git push
```

---

## 📈 Langkah 12: Repository Maintenance

### 12.1 Regular Updates

```bash
# Weekly/Monthly:

# Pull latest changes
git pull origin main

# Check for updates
git status

# Update dependencies
pip install --upgrade -r requirements.txt

# Commit updates
git add requirements.txt
git commit -m "Update Python dependencies"
git push
```

### 12.2 Archive Old Branches

```bash
# List branches
git branch -a

# Delete old feature branches
git push origin --delete old-feature-branch

# Keep main, develop, release branches
```

---

## 🚨 Troubleshooting

### Issue: "Permission denied"

```bash
# Check SSH:
ssh -T git@github.com

# If failed, re-add SSH key:
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Or use HTTPS token instead of SSH
```

### Issue: "Push rejected"

```bash
# Pull latest changes first
git pull origin main

# If conflict:
git merge --abort  # or resolve conflicts manually

# Then push
git push
```

### Issue: "Large files"

```bash
# GitHub limit: 100 MB per file

# Remove large file:
git rm --cached large_file.zip
git commit -m "Remove large file"

# Use Git LFS untuk large files:
git lfs install
git lfs track "*.pdb"
git add .gitattributes
git commit -m "Add Git LFS tracking"
```

---

## ✅ Checklist: Ready for GitHub

- [ ] README.md dengan overview project
- [ ] LICENSE file (MIT atau sesuai pilihan)
- [ ] .gitignore dengan Python patterns
- [ ] requirements.txt dengan dependencies
- [ ] Documentation files (METHODOLOGY, USAGE, etc)
- [ ] Sample data atau instructions untuk download
- [ ] Python scripts dengan docstrings
- [ ] Example notebooks (optional)
- [ ] CONTRIBUTING.md (untuk collaboration)
- [ ] Initial commit dengan meaningful message
- [ ] Repository URL di README

---

## 📚 Resources

- [GitHub Docs](https://docs.github.com)
- [Git Tutorial](https://git-scm.com/doc)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [README Best Practices](https://www.makeareadme.com/)

---

**Last Updated:** May 23, 2024

**Ready to push!** 🚀
