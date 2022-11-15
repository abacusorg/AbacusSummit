#!/usr/bin/env bash

fn=$1
format=$2

summit=${COSMOSIM}/Abacus

python -m Abacus.Analysis.PowerSpectrum.run_PS --nreaders=2 --nfft=2048 --format=${format} --nbins=2048 --out-parent=${summit}/power --nthreads=68 ${summit}/$(awk "NR == ${SLURM_ARRAY_TASK_ID}" $fn)
