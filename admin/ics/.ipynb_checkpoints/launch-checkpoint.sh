#!/usr/bin/env bash

cd logs/

#export OMP_NUM_THREADS=4
export OMP_NUM_THREADS=32
sbatch -N 1 --ntasks-per-node=1 -c ${OMP_NUM_THREADS} -C haswell --qos=regular -t 20:00 \
    disBatch  ../ics.disbatch -r ./ics.disbatch_40478038_status.txt -R
