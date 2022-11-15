#!/usr/bin/env bash

# Check that all the Pks files are in place

parent=${COSMOSIM}/Abacus/power/
joblists="${1:-base2_nevertarred_AB.txt}"

for jobs in ${joblists}; do
    format=$(echo $jobs | \grep -q '_AB' && echo 'AB' || echo $format)
    format=$(echo $jobs | \grep -q '_slices' && echo 'pack9' || echo $format)
    [[ $format ]] || (echo "format unknown"; exit 1)

    ngood=0
    i=1  # job number
    while read z; do
        sim=$(dirname $(dirname $z))
        z=$(basename $z)
        #ncsv=$(ls ${parent}/${sim}_products/power/${z}_${format}/power_nfft2048*.csv | wc -l)
        ncsv=$(find ${parent}/${sim}_products/power/${z}_${format}/power_nfft2048*.csv -size +50k | wc -l)
        #[[ $ncsv -eq 2 ]] && ngood=$(( ngood + 1 )) || echo "${i}:${sim}/halos/${z}"
        [[ $ncsv -eq 2 ]] && ngood=$(( ngood + 1 )) || echo "${sim}/halos/${z}"
        i=$((i + 1))
    done < "${jobs}"

    echo "Found ${ngood} good out of $(wc -l $jobs)" >&2
done
