#!/usr/bin/env bash

# syntax:
# ./change_cleaning_dir_structure.sh cleaned_halos/AbacuSummit_base_c123_ph123

set -e

OLDSIM="$1"
NEWSIM="$1/../../cleaning/$(basename $1)"

# make per-type dirs
for zdir in $OLDSIM/halos/z*; do
    mkdir $zdir/{cleaned_halo_info,cleaned_rvpid}
    mv $zdir/cleaned_halo_info*.asdf $zdir/cleaned_halo_info
    mv $zdir/cleaned_rvpid*.asdf $zdir/cleaned_rvpid
    \grep halo_info $zdir/checksums.crc32 > $zdir/cleaned_halo_info/checksums.crc32
    \grep rvpid $zdir/checksums.crc32 > $zdir/cleaned_rvpid/checksums.crc32
    rm $zdir/checksums.crc32
done
    
# move to cleaning dir
mkdir $NEWSIM
mv $OLDSIM/halos/* $NEWSIM
rmdir -p $OLDSIM/halos
