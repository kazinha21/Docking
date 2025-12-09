#!/bin/bash
# Script para rodar todos os ligantes no AutoDock Vina contra todas as proteínas

# Pasta dos ligantes
LIGAND_DIR="PDBQT_files"

# Lista de proteínas
RECEPTORS=("model1ready_clean.pdbqt" "modeldelready_clean.pdbqt")

# Parâmetros do grid (alterar conforme seu setup)
CENTER_X=121.437
CENTER_Y=121.388
CENTER_Z=105.602
SIZE_X=102
SIZE_Y=89
SIZE_Z=193
NUM_MODES=20
EXHAUSTIVENESS=16

# Cria pastas para salvar saídas e logs
mkdir -p Vina_outputs
mkdir -p Vina_logs

# Loop pelas proteínas e ligantes
for receptor in "${RECEPTORS[@]}"; do
    for ligand in "$LIGAND_DIR"/*_H.pdbqt; do
        base_ligand=$(basename "$ligand" _H.pdbqt)
        base_receptor=$(basename "$receptor" .pdbqt)

        # Nomes de saída
        OUT_FILE="Vina_outputs/${base_receptor}_${base_ligand}_out.pdbqt"
        LOG_FILE="Vina_logs/${base_receptor}_${base_ligand}_log.txt"

        echo "Rodando Vina: $ligand contra $receptor ..."
        
        vina --receptor "$receptor" \
             --ligand "$ligand" \
             --center_x $CENTER_X --center_y $CENTER_Y --center_z $CENTER_Z \
             --size_x $SIZE_X --size_y $SIZE_Y --size_z $SIZE_Z \
             --num_modes $NUM_MODES \
             --exhaustiveness $EXHAUSTIVENESS \
             --out "$OUT_FILE" \
             | tee "$LOG_FILE"

        echo "Finalizado: $OUT_FILE"
    done
done

echo "Todos os docking completados!"
