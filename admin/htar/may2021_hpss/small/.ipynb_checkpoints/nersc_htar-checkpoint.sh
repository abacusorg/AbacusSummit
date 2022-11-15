#!/usr/bin/env bash

# Syntax:
# $ ./nersc_htar.sh AbacusSummit_base_c999_ph999

set -e
module load esslurm

SIM_NAME=$1

HTAR_LOG='/global/cfs/cdirs/desi/cosmosim/Abacus/scripts/logs/%x-%A_%a.out'

sbatch --array=0-99 -o ${HTAR_LOG} --job-name="small_htar" nersc_htar_small.slurm
