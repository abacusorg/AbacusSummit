#!/usr/bin/env bash

set -e

simpath=$1
res=$2

simname=$(basename $simpath)

scratch=/dev/shm/lgarriso/ic/
out=${SCRATCH}/abacus_ic/
log=logs/${simname}-${res}.log

mkdir -p ${scratch}
mkdir -p ${out}
mkdir -p $(dirname ${log})

python -m Abacus.zeldovich --density --ZD_qPLT=0 --ZD_NumBlock=32 \
    --ICFormat=\"ZelSimple\" --CPD=1 --out-parent=${scratch} \
    --ppd=${res} --ZD_CornerModes=1 \
    $simpath/abacus.par &> ${log}
    
$HOME/abacus/Production/AbacusSummit/nersc_package_ics.py \
    ${scratch}/${simname}/ic/ --delete --out=${out} &>> ${log}

# Only do on the last round
$HOME/abacus/external/fast-cksum/bin/merge_checksum_files.py \
    --delete ${out}/${simname}/*.crc32 \
    | sponge ${out}/${simname}/checksums.crc32
