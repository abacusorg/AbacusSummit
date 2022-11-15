#!/usr/bin/env bash

# Downselect the data on disk to the "high traffic" subset we have designated.
# Deletes:
# - All B particles
# - Field A particles from redshifts 0.1, 0.3, 0.4, 1.7, 3.0
# For now, we will leave base_c000_ph{000..025}, and highbase_c000_ph100 

set -e

if [[ $# -eq 0 ]] ; then
    echo 'Needs at least one sim arg'
    exit 1
fi

for sim in "$@"; do
    pushd $sim

    du -csh halos/z*/{halo_rv_B,halo_pid_B,field_rv_B,field_pid_B} halos/z{0.100,0.300,0.400,1.700,3.000}/{field_rv_A,field_pid_A}
    rm -rf halos/z*/{halo_rv_B,halo_pid_B,field_rv_B,field_pid_B} halos/z{0.100,0.300,0.400,1.700,3.000}/{field_rv_A,field_pid_A}

    popd
done

