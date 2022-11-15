#!/usr/bin/env bash
# Entry point to verify Abacus checksums, using job array of N tasks, each on 1 node.
# Usage: ./submit_array.sh NUM_ARRAY_TASKS
# Finds at most next NUM_ARRAY_TASKS unverified sims and writes each SIMNAME
# to verified_checksums_all.txt upon completion.
DEBUG=${2:-0}
NUM_ARRAY_JOBS=$1
if [ $# -lt 1 ]; then
  echo 1>&2 "$0: not enough arguments"
  exit 2
elif [ $# -gt 2 ]; then
  echo 1>&2 "$0: too many arguments"
  exit 2
fi


echo "Will verify checksums for at most $NUM_ARRAY_JOBS boxes."

ABACUSSUMMIT=/global/project/projectdirs/desi/cosmosim/Abacus
cat $ABACUSSUMMIT/verified_checksums/verified_checksums*.txt >> $ABACUSSUMMIT/verified_checksums/master.txt

TMP_FILE=TMP_NEXT_BATCH.txt
if [ -f $TMP_FILE ] ; then
    rm $TMP_FILE
fi

N=0
for sim in $ABACUSSUMMIT/*AbacusSummit*/; do ##### only do c100+ -- no timeslices
        sim_dir=$(basename $sim)
        if ! grep -Fxq "$sim_dir" $ABACUSSUMMIT/verified_checksums/master.txt
        then
                echo $sim_dir >> $TMP_FILE
                N=$(( N+1 ))
        fi

        if [[ $N = $NUM_ARRAY_JOBS ]]
        then
                break
        fi
done

echo "Found $N boxes to verify checksums:"
tail -"$N" $TMP_FILE

rm $ABACUSSUMMIT/verified_checksums/verified_checksums*.txt

echo "Submitting batch job."
export RANGE=$((N-1))

if [[ $DEBUG = 1 ]]; then
	sbatch --array=0-"$RANGE" --time="0:01:00" --qos=debug array_verify_checksums.slurm
else
	sbatch --array=0-"$RANGE" array_verify_checksums.slurm
fi	
