from meeko import MoleculePreparation
from meeko import PDBQTWriterLegacy
from rdkit import Chem
import glob
import os

# Pasta de saída para os arquivos PDBQT
output_folder = "PDBQT_files"
os.makedirs(output_folder, exist_ok=True)

# Pega todos os arquivos .sdf na pasta atual
for file in glob.glob("*.sdf"):
    mol = Chem.MolFromMolFile(file, removeHs=False)
    if mol is None:
        print(f"Erro ao carregar {file}, pulando...")
        continue

    # Cria o objeto de preparação e adiciona H
    prep = MoleculePreparation()
    molsetups = prep.prepare(mol)  # prepara a molécula

    # Para cada setup, escreve PDBQT
    for i, setup in enumerate(molsetups):
        pdbqt_string, is_ok, err = PDBQTWriterLegacy.write_string(setup)
        if is_ok:
            # Define arquivo de saída dentro da pasta
            base_name = os.path.splitext(file)[0]
            output_file = os.path.join(output_folder, f"{base_name}_H.pdbqt")
            with open(output_file, "w") as f:
                f.write(pdbqt_string)
            print(f"{file} -> {output_file} preparado!")
        else:
            print(f"Erro ao gerar PDBQT de {file}: {err}")
