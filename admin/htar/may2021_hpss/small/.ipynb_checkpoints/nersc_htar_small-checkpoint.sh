#!/usr/bin/env bash

# Syntax:
# $ ./nersc_htar_smallsh

set -e
module load esslurm

SIM_NAME=$1

HTAR_LOG='/global/cfs/cdirs/desi/cosmosim/Abacus/scripts/logs/%x-%A_%a.out'

# 100 jobs x 20 sims = 2000 sims
sbatch --array=1-99 -o ${HTAR_LOG} --job-name="small_htar" nersc_htar_small.slurm
