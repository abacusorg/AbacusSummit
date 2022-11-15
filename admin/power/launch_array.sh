#!/usr/bin/env bash

fn=small_redo6_AB.txt
njob=$(wc -l $fn | cut -d ' ' -f1)

time="00:30:00"
format=asdf

#time="4:00:00"
#format=asdf_pack9

summit=$COSMOSIM/Abacus

sbatch -o "small_log/${fn}-%A_%a.out" --array="1-${njob}" -N1 -t $time -C haswell -q regular --wrap="python -m Abacus.Analysis.PowerSpectrum.run_PS --nreaders=2 --nfft=2048 --format=${format} --nbins=2048 --out-parent=${summit}/power/small --nthreads=68 ${summit}/small/\$(awk \"NR == \${SLURM_ARRAY_TASK_ID}\" $fn)"

# now with zspace
sbatch -o "small_log/${fn}-%A_%a.out" --array="1-${njob}" -N1 -t $time -C haswell -q regular --wrap="python -m Abacus.Analysis.PowerSpectrum.run_PS --zspace --nreaders=2 --nfft=2048 --format=${format} --nbins=2048 --out-parent=${summit}/power/small --nthreads=68 ${summit}/small/\$(awk \"NR == \${SLURM_ARRAY_TASK_ID}\" $fn)"
