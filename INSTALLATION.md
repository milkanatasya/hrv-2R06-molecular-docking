# Panduan Instalasi - Tools & Software

## 📋 Daftar Tools

| Software | Platform | Lisensi | Ukuran | Link |
|----------|----------|---------|--------|------|
| UCSF Chimera | Windows/Mac/Linux | Gratis | ~160 MB | https://www.cgl.ucsf.edu/chimera/download.html |
| AutoDockTools | Windows/Mac/Linux | Gratis | ~30 MB | https://autodock.scripps.edu/resources/adt |
| PyRx | Windows/Mac/Linux | Gratis | ~500 MB | https://pyrx.sourceforge.io/ |
| PyMOL | Cross-platform | Community Edition Gratis | ~200 MB | https://pymol.org/2/ |
| DS Visualizer | Windows/Linux | Gratis (Trial) | ~2 GB | https://discover.3ds.com/discovery-studio-visualizer-download |
| Python 3.8+ | Cross-platform | Gratis | ~100 MB | https://www.python.org/downloads/ |

---

## 🐍 Python & Environment Setup

### 1. Install Python 3.8+

**Windows:**
```bash
# Download dari https://www.python.org/downloads/
# Atau gunakan Windows Store
# PENTING: Check "Add Python to PATH"

# Verify instalasi
python --version
pip --version
```

**macOS:**
```bash
# Menggunakan Homebrew
brew install python@3.11

# Atau download dari python.org
# Verify
python3 --version
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install python3.11 python3-pip python3-venv

# Verify
python3 --version
pip3 --version
```

### 2. Setup Virtual Environment

```bash
# Navigate ke project directory
cd ~/hrv-2r06-molecular-docking

# Create virtual environment
python -m venv venv

# Aktivasi virtual environment
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate

# Untuk deactivate:
deactivate
```

### 3. Install Python Dependencies

```bash
# Pastikan venv sudah activated

# Upgrade pip, setuptools, wheel
pip install --upgrade pip setuptools wheel

# Install dari requirements.txt
pip install -r scripts/requirements.txt

# Verify instalasi
pip list
```

**requirements.txt**:
```txt
biopython==1.83
pandas==2.0.0
numpy==1.24.0
matplotlib==3.7.0
seaborn==0.12.0
scipy==1.10.0
rdkit==2023.03.1
jupyter==1.0.0
ipython==8.12.0
plotly==5.13.0
scikit-learn==1.2.0
requests==2.31.0
```

---

## 🛠️ UCSF Chimera Installation

### Windows

```bash
1. Download installer dari:
   https://www.cgl.ucsf.edu/chimera/download.html
   
   Select: Windows
   Download: chimera-1.17.3.win64.exe (atau versi terbaru)

2. Double-click installer
3. Follow installation wizard
4. Select installation directory (default: C:\Program Files\UCSF\Chimera)
5. Finish installation

6. Verify:
   - Start > Search "Chimera"
   - Launch application
   - Menu: Help > About Chimera
```

### macOS

```bash
1. Download DMG dari website
2. Double-click chimera-1.17.3.dmg
3. Drag Chimera icon ke Applications folder
4. Eject disk image
5. Open Applications > Chimera.app

# Verify di Terminal:
open /Applications/Chimera.app
```

### Linux

```bash
1. Download tar.gz dari website:
   wget https://www.cgl.ucsf.edu/chimera/cgi-bin/secure/chimera-1.17.3.linux_x86_64.tar.gz

2. Extract:
   tar xzf chimera-1.17.3.linux_x86_64.tar.gz
   cd chimera-1.17.3

3. Run installer:
   ./install.sh

4. Follow prompts untuk lokasi instalasi
   Default: ~/chimera-1.17.3

5. Add ke PATH:
   echo 'export PATH=$PATH:~/chimera-1.17.3/bin' >> ~/.bashrc
   source ~/.bashrc

6. Verify:
   chimera --version
```

### Verifikasi Instalasi

```bash
# Buka file PDB untuk test
# File > Open > pilih PDB file
# Jika berhasil: struktur protein ditampilkan dalam 3D viewer
```

---

## 🖱️ AutoDockTools (ADT) Installation

### Windows

```bash
1. Download:
   https://autodock.scripps.edu/resources/adt
   Select: ADT Zip File for Windows
   File: adt-1.5.7.win32.zip

2. Extract zip ke folder (contoh: C:\ADT\)

3. Jalankan:
   Buka file manager
   Navigate ke C:\ADT\Lib\site-packages\AutoDockTools\bin\
   Double-click: ADT.exe

4. Create shortcut (optional):
   Right-click ADT.exe > Send to > Desktop (create shortcut)
```

### macOS

```bash
1. Download ADT untuk macOS
   https://autodock.scripps.edu/resources/adt

2. Extract zip file

3. Buka Terminal:
   cd ~/Downloads/adt-1.5.7/bin
   ./ADT

4. Atau buat alias di ~/.bash_profile:
   echo 'alias adt="/path/to/adt/bin/ADT"' >> ~/.bash_profile
   source ~/.bash_profile
```

### Linux

```bash
1. Download zip file
   wget https://autodock.scripps.edu/...

2. Extract:
   unzip adt-1.5.7.linux_x86_64.zip
   cd adt-1.5.7

3. Jalankan:
   ./bin/ADT

4. Atau setup di PATH:
   export PATH=$PATH:~/adt-1.5.7/bin
```

### Verifikasi

```bash
# ADT window harus muncul
# Menu: Help > About ADT
# Verify version 1.5.7 atau lebih baru
```

---

## 🔬 PyRx Installation

### All Platforms (Recommended: Use Installer)

```bash
# Method 1: Download Pre-built
1. Visit: https://pyrx.sourceforge.io/
2. Download binary untuk OS Anda
3. Extract folder
4. Run executable (setup-pyrx.exe Windows / pyrx Linux)

# Method 2: Python Package
pip install pyrx

# Method 3: Build from Source
git clone https://sourceforge.net/p/pyrx/code/
cd pyrx
python setup.py install
```

### Windows - Detailed Steps

```bash
1. Download: pyrx-0.9.7.w64.exe
2. Run installer
3. Select installation path (default: C:\Program Files\PyRx)
4. Complete installation
5. Double-click PyRx shortcut to launch
```

### macOS/Linux

```bash
1. Download appropriate version
2. Extract tar.gz or zip
3. Run setup:
   chmod +x setup-pyrx
   ./setup-pyrx
4. Follow instructions
5. Add to PATH if needed
```

### Verifikasi PyRx

```bash
# Launch PyRx
pyrx

# Window should appear with:
# - File menu
# - Docking panel
# - Visualization area
# - Tools menu
```

---

## 🐍 PyMOL Installation

### Option 1: Community Edition (Gratis)

```bash
# Install via conda (easiest)
conda install -c conda-forge pymol-open-source

# Or pip
pip install pymol-open-source

# Verify
pymol --version
```

### Option 2: Official Installers

**Windows:**
```bash
1. Download dari https://pymol.org/
   Select: PyMOL Community Edition
   File: PyMOL-2.x.x.exe

2. Run installer
3. Follow wizard
4. Launch dari Start menu
```

**macOS:**
```bash
# Using Homebrew (recommended)
brew install pymol

# Or download DMG from website
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt-get install pymol

# Or from source
pip install pymol
```

### Verifikasi

```bash
# Launch PyMOL
pymol

# Window dengan shell harus muncul
# Load test file: File > Open > PDB
```

---

## 📊 Discovery Studio Visualizer Installation

### Download & Installation

```bash
# Note: DS Visualizer requires free account registration

1. Visit: https://discover.3ds.com/discovery-studio-visualizer-download
2. Create free account (email verification required)
3. Download untuk sistem operasi Anda
4. Follow installation wizard
5. License file akan diemail

File size: ~2 GB (quite large)
Installation time: 10-15 minutes
```

### Windows

```bash
1. Download: Discovery_Studio_2024_installer.exe
2. Run as Administrator
3. Accept license agreement
4. Select installation folder (default: Program Files)
5. Complete installation
6. Launch dari Start menu
```

### macOS

```bash
1. Download DMG
2. Run installer
3. Drag application ke Applications
4. Launch dari Applications folder
```

### Linux

```bash
1. Download RPM atau DEB sesuai distro
2. Install:
   # Debian/Ubuntu
   sudo dpkg -i DiscoveryStudio2024.deb
   sudo apt-get install -f  # Fix dependencies
   
   # CentOS/RHEL
   sudo rpm -ivh DiscoveryStudio2024.rpm

3. Launch:
   discovery-studio
   # atau cari di Applications
```

### Verifikasi

```bash
# Launch DS Visualizer
# Welcome dialog harus muncul
# File > Open > pilih PDB file untuk test
```

---

## 🔗 AutoDock Vina Setup

### Windows

```bash
# Method 1: Download pre-built binary
1. Download vina_1_2_0_linux_x86 dari:
   http://vina.scripps.edu/

2. Extract zip file

3. Add ke PATH:
   System Properties > Environment Variables
   New > Variable name: VINA_PATH
   Variable value: C:\path\to\vina\bin
   Edit PATH > Add %VINA_PATH%

4. Test:
   cmd > vina --help
   # should print usage information
```

### macOS

```bash
# Using Homebrew (easiest)
brew install autodock-vina

# Verify
vina --help

# Or download binary manually
# Extract dan add to PATH in ~/.bash_profile
```

### Linux

```bash
# Build from source
git clone https://github.com/ccsb-scripps/AutoDock-Vina.git
cd AutoDock-Vina/build/linux/release
make
# Binary di ../release/vina

# Or use precompiled:
wget http://vina.scripps.edu/download/autodock_vina_1_2_0_linux_x86_64.tgz
tar xzf autodock_vina_1_2_0_linux_x86_64.tgz

# Add to PATH
export PATH=$PATH:~/autodock_vina_1_2_0_linux_x86_64/bin
```

---

## ✅ Complete Installation Verification

Jalankan script ini untuk verify semua tools:

```bash
#!/bin/bash
# verify_installation.sh

echo "=== Verifying Installation ==="
echo

# Python
echo "1. Python:"
python --version
pip list | grep -E "biopython|pandas|numpy|rdkit"
echo

# Chimera
echo "2. UCSF Chimera:"
which chimera
echo

# AutoDockTools
echo "3. AutoDockTools:"
echo "   (Open ADT GUI to verify)"
echo

# PyRx
echo "4. PyRx:"
which pyrx
echo

# PyMOL
echo "5. PyMOL:"
pymol --version
echo

# Vina
echo "6. AutoDock Vina:"
vina --help | head -3
echo

# DS Visualizer
echo "7. Discovery Studio:"
echo "   (Launch GUI to verify)"
echo

echo "=== All checks complete ==="
```

**Run verification:**
```bash
bash verify_installation.sh
```

---

## 🐛 Troubleshooting

### Python Issues

```bash
# ModuleNotFoundError: No module named 'X'
# Solution:
pip install package_name
pip list  # verify install

# Wrong Python version?
python --version
which python
# Use specific version: python3.9 ...
```

### PyRx Won't Launch

```bash
# Check Python path in PyRx config
# Reinstall:
pip uninstall pyrx
pip install pyrx --upgrade

# Check dependencies:
pip list | grep -E "numpy|scipy"
```

### Chimera/ADT GUI Issues

```bash
# Linux X11 forwarding issues?
export DISPLAY=:0

# Reinstall via conda (sometimes easier):
conda install -c bioconda chimera
conda install -c bioconda autodocktools
```

### Vina Binary Not Found

```bash
# Check PATH
echo $PATH

# Add to PATH:
export PATH=$PATH:/path/to/vina/bin

# Permanent (add to ~/.bashrc or ~/.bash_profile):
echo 'export PATH=$PATH:/path/to/vina/bin' >> ~/.bashrc
source ~/.bashrc
```

---

## 🔄 Updating Tools

```bash
# Python packages
pip install --upgrade package_name
pip install --upgrade pip

# Chimera (download new version)
# AutoDockTools (download new version)
# PyRx (automatic updates or download new binary)
# PyMOL
pip install --upgrade pymol

# Vina (download new release from scripps)
```

---

## 💾 Environment Variables

### Linux/macOS

```bash
# Add ke ~/.bashrc atau ~/.bash_profile:

# Python virtual environment activation (optional)
alias activate_mol='source ~/hrv-2r06-molecular-docking/venv/bin/activate'

# Tool paths
export CHIMERA_HOME=/path/to/chimera
export ADT_HOME=/path/to/adt
export VINA_BIN=/path/to/vina/bin

# Update PATH
export PATH=$PATH:$VINA_BIN

# Apply changes
source ~/.bashrc
```

### Windows

```batch
# Setenv.bat atau command line

set CHIMERA_HOME=C:\Program Files\UCSF\Chimera
set ADT_HOME=C:\ADT
set VINA_BIN=C:\vina\bin

set PATH=%PATH%;%VINA_BIN%

# Permanent: setx in command prompt or GUI Environment Variables
```

---

## 📚 Next Steps

1. ✅ Instalasi semua tools sesuai section di atas
2. ✅ Verify installation dengan script
3. ✅ Download PDB file dari RCSB PDB
4. ✅ Lanjut ke USAGE_GUIDE.md untuk workflow

---

**Last Updated:** May 23, 2024

**Verified on:** Windows 10/11, macOS 12+, Ubuntu 20.04+
