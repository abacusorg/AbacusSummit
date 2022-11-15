#!/usr/bin/env bash

# write all output to log, and to stdout
logfn="check_cleaning_$(date +"%FT%T").log"
exec > >(tee "$logfn") 2>&1

tstart=$(date +%s.%N)

abacus=$CFS/desi/cosmosim/Abacus

pushd $abacus > /dev/null
ncheck=0
nfail=0
for sim in AbacusSummit_*/ small/AbacusSummit_*; do
    anymissing_sim=0
    
    pushd $sim/halos > /dev/null
    for zdir in z*/; do
        anymissing_z=0
        
        if [[ ! -d $zdir/halo_info ]]; then
            if [[ $anymissing_sim == 0 ]]; then
                    echo "- $sim"
                    anymissing_sim=1
                fi
            echo "    - $sim/halos/$zdir exists but does not contain halo_info dir"
            continue
        fi
        
        # we know z=8, small box doesn't have cleaning
        [[ $sim == small/* && $zdir == "z8.000/" ]] && continue
        
        pushd $zdir/halo_info > /dev/null
        for hi in halo_info_*.asdf; do
            slab=$(echo $hi | \grep -Po '(\d+)')
            ncheck=$((ncheck+1))
            cfn="$abacus/cleaning/$sim/$zdir/cleaned_halo_info/cleaned_halo_info_$slab.asdf"
            if [[ ! -f $cfn ]]; then
                if [[ $anymissing_sim == 0 ]]; then
                    echo "- $sim"
                    anymissing_sim=1
                fi
                if [[ $anymissing_z == 0 ]]; then
                    echo "    - $zdir"
                    anymissing_z=1
                fi
            
                #echo "File \"$cfn\" does not exist"
                echo "        - cleaned_halo_info_$slab.asdf"
                nfail=$((nfail+1))
            fi
        done
        popd > /dev/null
    done
    popd > /dev/null
done

tend=$(date +%s.%N)
elapsed=$(echo "$tend - $tstart" | bc | xargs printf "%.4g sec" )
echo "All done. Checked $ncheck, missing $nfail, took $elapsed"
