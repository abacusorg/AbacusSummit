#!/usr/bin/env bash

# Checking Abacus disk usage with `du` takes a while. But running it in parallel
# gives an excellent speedup.  Usually runs in 3 mins (maybe slower if the metadata is cold)

abacus=$CFS/desi/cosmosim/Abacus
dirs=$(find $abacus $abacus/small -mindepth 1 -maxdepth 1 ! -name scripts ! -name small)  # no scripts dir, too many log files. and recurse into small

module load parallel
time parallel -j 16 du -sb ::: ${dirs} | awk '{sum+=$1} END {print sum " bytes"}'
