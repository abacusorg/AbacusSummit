#!/usr/bin/env bash

. env.sh
mkdir -p logs

export OMP_NUM_THREADS=64
sbatch -N 5 --ntasks-per-node=1 -C cpu --qos=regular -t 0-3 \
    -o 'logs/slurm-%j.out' \
    disBatch -e --status-header ics.base.disbatch -p logs/
    # -R -r logs/ics.disbatch_disBatch_221109151331_783_status.txt
