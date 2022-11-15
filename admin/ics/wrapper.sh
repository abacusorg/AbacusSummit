#!/usr/bin/env bash

sim=$1
res=$2

scratch=/dev/shm/lgarriso/ic/
subsuite=$(dirname ${sim})
sim=$(basename ${sim})
out=${SCRATCH}/abacus_ic/${subsuite}
log=logs/${sim}-${res}.log
abacussummit=$CFS/desi/cosmosim/Abacus/

mkdir -p ${scratch}
mkdir -p ${out}
mkdir -p $(dirname ${log})

python -m Abacus.zeldovich --density --ZD_qPLT=0 --ZD_NumBlock=32 \
    --ICFormat=\"ZelSimple\" --CPD=1 --out-parent=${scratch} \
    --ppd=${res} --ZD_CornerModes=1 \
    ${abacussummit}/${subsuite}/${sim}/abacus.par &> ${log}
    
$HOME/abacus/Production/AbacusSummit/nersc_package_ics.py \
    ${scratch}/${sim}/ic/ --delete --out=${out} &>> ${log}

# Only do on the last round
$HOME/abacus/external/fast-cksum/bin/merge_checksum_files.py \
    --delete ${out}/${sim}/*.crc32 \
    | sponge ${out}/${sim}/checksums.crc32
