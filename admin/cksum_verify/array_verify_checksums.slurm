#!/usr/bin/env bash
#SBATCH -N1
#SBATCH -C haswell
#SBATCH -t 14:00:00
#SBATCH -q regular

#SBATCH --output=./logs/slurm-%A_%a.out

# Verifies Abacus checksums, parallel on 1 node

set -e
shopt -s globstar

now=$(date +"%T")
echo "Beginning run at: $now"

module load parallel

echo "Submitting job array of length " $SLURM_ARRAY_TASK_COUNT

ABACUSSUMMIT=/global/project/projectdirs/desi/cosmosim/Abacus
##export SIMNAME=${SIMS[$SLURM_ARRAY_TASK_ID]}
export SIMNAME=$(cat TMP_NEXT_BATCH.txt | sed -n $((SLURM_ARRAY_TASK_ID+1))'p')
echo "Task ID " $SLURM_ARRAY_TASK_ID "doing box " $SIMNAME

FAST_CKSUM=$ABACUS/external/fast-cksum/bin/fast_cksum

N=0
for C in $ABACUSSUMMIT/$SIMNAME/**/checksums.crc32; do
    D=$(dirname $C)
    echo "Processing directory $D"

    cd $D

#    LINE1="Processing directory $D"
#    LINE2="Files checksums.crc32 and - are identical"
#    VERIFIED_STR="${LINE1}"$'\n'"${LINE2}"

#	echo "${VERIFIED_STR}" 	

#	case `grep -Fx "${VERIFIED_STR}" ./logs/slurm* >/dev/null; echo $?` in
#	  0)
#	    echo "${VERIFIED_STR} already present. Skipping. "
#	    ;;
#	  1)
#	    echo "${VERIFIED_STR} missing. Checksumming."
	    FNS=$(find * -maxdepth 0 -type f ! -name checksums.crc32)
            NERSC_CHECKSUMS=$(parallel -j16 -k $FAST_CKSUM ::: $FNS)
            echo "$NERSC_CHECKSUMS" | diff -s checksums.crc32 -
#	    ;;
#	  *)
#	    echo "${VERIFIED_STR} threw error. Exiting."; exit 1;
#	    ;;
#	esac    
       
    N=$(( N + 1 ))

now=$(date +"%T")
echo "Done with $D at $now"

    cd - > /dev/null
done

echo "Verified $N checksum files"
echo $SIMNAME >> $ABACUSSUMMIT/verified_checksums/verified_checksums_${SLURM_JOB_ID}.txt

echo "All done!"
now=$(date +"%T")
echo "Completing run at: $now"
