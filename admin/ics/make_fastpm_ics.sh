#!/usr/bin/env bash

# Make ICs for a set of sims

fn=ph001-024_white_noise.txt
nsim=$(wc -l $fn | cut -d ' ' -f1)
p="/project/projectdirs/desi/cosmosim/Abacus/ic/for_fastpm"
abacussummit="/project/projectdirs/desi/cosmosim/Abacus/"
ppd=5184
block=96
zinit=1
thread=16

export OMP_NUM_THREADS=${thread}

sbatch -t 0-3 -N1 -n1 -c${thread} --mem=64G -C haswell -q regular --array=1-$nsim --wrap "python -m Abacus.zeldovich --ZD_qPLT=0 --ZD_NumBlock=${block} --ZD_qdensity=2 --ppd=${ppd} --InitialRedshift=${zinit} --density --out-parent=$p ${abacussummit}/\$(sed \"\${SLURM_ARRAY_TASK_ID}q;d\" $fn)/abacus.par --white"
