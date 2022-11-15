#!/usr/bin/env bash

# run a command in parallel on AbacusSummit dirs

abacus=$CFS/desi/cosmosim/Abacus
toplevel="$(find $abacus/ -mindepth 1 -maxdepth 1)"
sims=$(echo "$toplevel" | grep AbacusSummit_)
nonsim=$(echo "$toplevel" | grep -v AbacusSummit_)
nonsim_plus_smallsub="$nonsim
$(echo "$nonsim" | sed 's,$,/small,')"

dirs="${sims}
$(find $nonsim_plus_smallsub -mindepth 1 -maxdepth 1 ! -name small)"

#echo "${dirs}" | sort -h > dirs.txt
#exit 0

module load parallel
time parallel -j 16 chmod -R o+rX ::: ${dirs}
