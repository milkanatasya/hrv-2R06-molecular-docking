#!/usr/bin/env python
"""
Protein Preparation Script for Molecular Docking

Functions:
- Download PDB file dari RCSB
- Clean structure (remove water, heteroatoms)
- Add hydrogens & charges
- Convert to PDBQT format

Usage:
    python scripts/01_protein_preparation.py --pdb-id 2R06 --output data/protein/
"""

import argparse
import os
import subprocess
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def download_pdb(pdb_id, output_dir):
    """
    Download PDB file dari RCSB PDB
    
    Args:
        pdb_id (str): PDB ID (e.g., '2R06')
        output_dir (str): Directory untuk save file
    
    Returns:
        str: Path to downloaded PDB file
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = output_dir / f"{pdb_id}.pdb"
    
    if output_file.exists():
        logger.info(f"✓ PDB file already exists: {output_file}")
        return str(output_file)
    
    logger.info(f"Downloading PDB {pdb_id}...")
    
    try:
        from Bio import PDB
        pdbl = PDB.PDBList()
        pdb_file = pdbl.retrieve_pdb_file(pdb_id, file_format='pdb', 
                                          pdir=str(output_dir))
        
        # Move file to correct location
        if pdb_file != str(output_file):
            os.rename(pdb_file, output_file)
        
        logger.info(f"✓ Downloaded: {output_file}")
        return str(output_file)
    
    except Exception as e:
        logger.error(f"Error downloading PDB: {e}")
        raise


def prepare_protein_chimera(pdb_file, output_file=None):
    """
    Prepare protein menggunakan UCSF Chimera
    Requires Chimera installed dan accessible from PATH
    
    Args:
        pdb_file (str): Input PDB file
        output_file (str): Output PDBQT file
    
    Returns:
        str: Path to prepared protein
    """
    if output_file is None:
        output_file = pdb_file.replace('.pdb', '_prepared.pdbqt')
    
    logger.info(f"Preparing protein with Chimera: {pdb_file}")
    
    # Chimera script
    chimera_script = f"""
open {pdb_file}
select water
delete selected
select heteroatom & ~protein & ~nucleic
delete selected
Tools Structure Editing DockPrep
"""
    
    # Save script
    script_file = pdb_file.replace('.pdb', '_prep.py')
    with open(script_file, 'w') as f:
        f.write(chimera_script)
    
    # Run chimera
    try:
        result = subprocess.run(
            ['chimera', '--nogui', '--script', script_file],
            capture_output=True,
            timeout=60
        )
        
        if result.returncode == 0:
            logger.info(f"✓ Protein prepared: {output_file}")
            return output_file
        else:
            logger.error(f"Chimera error: {result.stderr.decode()}")
            raise RuntimeError("Chimera preparation failed")
    
    except FileNotFoundError:
        logger.error("Chimera tidak ditemukan di PATH")
        raise
    finally:
        # Clean up script
        if os.path.exists(script_file):
            os.remove(script_file)


def prepare_protein_adt(pdb_file, output_file=None):
    """
    Prepare protein menggunakan AutoDockTools
    
    Args:
        pdb_file (str): Input PDB file
        output_file (str): Output PDBQT file
    
    Returns:
        str: Path to prepared protein
    """
    if output_file is None:
        output_file = pdb_file.replace('.pdb', '_prepared.pdbqt')
    
    logger.info(f"Preparing protein with AutoDockTools: {pdb_file}")
    
    try:
        # Menggunakan meeko (more modern ADT wrapper)
        from meeko import MoleculePreparation
        
        mol = MoleculePreparation.from_pdb_file(pdb_file)
        
        # Remove water & heteroatoms
        mol.remove_water()
        mol.remove_heteroatoms_except_cofactors()
        
        # Add hydrogens & charges
        mol.add_missing_hydrogens()
        mol.compute_charges()
        
        # Save as PDBQT
        mol.write_pdbqt_file(output_file)
        
        logger.info(f"✓ Protein prepared: {output_file}")
        return output_file
    
    except ImportError:
        logger.warning("Meeko tidak terinstall, mencoba method alternative...")
        return prepare_protein_biopython(pdb_file, output_file)


def prepare_protein_biopython(pdb_file, output_file=None):
    """
    Simple preparation menggunakan BioPython
    Note: Tidak se-comprehensive seperti Chimera/ADT
    
    Args:
        pdb_file (str): Input PDB file
        output_file (str): Output PDB file
    
    Returns:
        str: Path to prepared protein
    """
    if output_file is None:
        output_file = pdb_file.replace('.pdb', '_prepared.pdb')
    
    logger.info(f"Preparing protein with BioPython: {pdb_file}")
    
    from Bio.PDB import PDBIO, Select
    
    class ProteinSelect(Select):
        """Select only protein atoms"""
        def accept_residue(self, residue):
            # Keep protein residues
            if residue.resname in ['ALA', 'ARG', 'ASN', 'ASP', 'CYS',
                                   'GLU', 'GLN', 'GLY', 'HIS', 'ILE',
                                   'LEU', 'LYS', 'MET', 'PHE', 'PRO',
                                   'SER', 'THR', 'TRP', 'TYR', 'VAL']:
                return True
            return False
    
    try:
        from Bio.PDB import PDBParser
        
        parser = PDBParser(QUIET=True)
        structure = parser.get_structure('protein', pdb_file)
        
        io = PDBIO()
        io.set_structure(structure)
        io.save(output_file, ProteinSelect())
        
        logger.info(f"✓ Protein cleaned: {output_file}")
        return output_file
    
    except Exception as e:
        logger.error(f"BioPython preparation error: {e}")
        raise


def validate_protein(pdb_file):
    """
    Validate protein structure
    
    Args:
        pdb_file (str): Path to PDB file
    
    Returns:
        dict: Validation results
    """
    logger.info(f"Validating protein: {pdb_file}")
    
    try:
        from Bio.PDB import PDBParser
        
        parser = PDBParser(QUIET=True)
        structure = parser.get_structure('protein', pdb_file)
        
        # Count atoms
        atom_count = sum(1 for _ in structure.get_atoms())
        
        # Count chains
        chains = list(structure.get_chains())
        chain_count = len(chains)
        
        # Count residues
        residue_count = sum(1 for _ in structure.get_residues())
        
        results = {
            'file': pdb_file,
            'atoms': atom_count,
            'chains': chain_count,
            'residues': residue_count,
            'status': 'OK'
        }
        
        logger.info(f"✓ Validation results:")
        logger.info(f"  - Atoms: {atom_count}")
        logger.info(f"  - Chains: {chain_count}")
        logger.info(f"  - Residues: {residue_count}")
        
        return results
    
    except Exception as e:
        logger.error(f"Validation error: {e}")
        return {'status': 'ERROR', 'error': str(e)}


def main():
    """Main function"""
    
    parser = argparse.ArgumentParser(
        description='Prepare protein untuk molecular docking'
    )
    
    parser.add_argument(
        '--pdb-id',
        type=str,
        help='PDB ID untuk download (e.g., 2R06)'
    )
    parser.add_argument(
        '--input',
        type=str,
        help='Path ke PDB file (alternative ke --pdb-id)'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='data/protein/',
        help='Output directory'
    )
    parser.add_argument(
        '--method',
        type=str,
        choices=['chimera', 'adt', 'biopython'],
        default='biopython',
        help='Preparation method'
    )
    parser.add_argument(
        '--validate-only',
        action='store_true',
        help='Hanya validate, tidak prepare'
    )
    
    args = parser.parse_args()
    
    # Get PDB file
    if args.pdb_id:
        pdb_file = download_pdb(args.pdb_id, args.output)
    elif args.input:
        pdb_file = args.input
    else:
        parser.error('Specify --pdb-id atau --input')
    
    # Validate input
    validation = validate_protein(pdb_file)
    if validation['status'] != 'OK':
        logger.error("Validation failed")
        return 1
    
    # Prepare protein
    if not args.validate_only:
        if args.method == 'chimera':
            output_file = prepare_protein_chimera(pdb_file)
        elif args.method == 'adt':
            output_file = prepare_protein_adt(pdb_file)
        else:
            output_file = prepare_protein_biopython(pdb_file)
        
        # Validate output
        validate_protein(output_file)
        logger.info(f"\n✓ Preparation complete: {output_file}")
    
    return 0


if __name__ == '__main__':
    exit(main())
