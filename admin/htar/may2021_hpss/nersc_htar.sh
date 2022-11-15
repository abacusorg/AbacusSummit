#!/usr/bin/env bash

# Syntax:
# $ ./nersc_htar.sh AbacusSummit_base_c999_ph999

set -e
module load esslurm

SIM_NAME=$1

HTAR_LOG="/global/cfs/cdirs/desi/cosmosim/Abacus/scripts/logs/${SIM_NAME}_htar.out"

sbatch -o ${HTAR_LOG} --job-name="${SIM_NAME}_htar" nersc_htar.slurm $SIM_NAME
