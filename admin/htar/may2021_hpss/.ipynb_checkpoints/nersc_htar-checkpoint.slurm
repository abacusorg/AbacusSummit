#!/usr/bin/env bash
#SBATCH --qos=xfer  # https://docs.nersc.gov/jobs/examples/#xfer-queue
#SBATCH --time=2-0  # max time 2 days
#SBATCH --mem 16G  # docs recommend > 8 GB for large files

# This script is called from nersc_htar.sh

set -e  # quit on error

module load esslurm

# This script runs htar to store files on tape (HPSS).
# Deletion of the originals will be taken care of later by hand

SIM_SET=${SIM_SET:-supplemental}
SIM_NAME=$1

WORKINGDIR=$CFS/desi/cosmosim/Abacus/$SIM_SET/$SIM_NAME
HPSSDIR=/nersc/projects/desi/cosmosim/Abacus/$SIM_SET/$SIM_NAME
cd $WORKINGDIR

NTHREAD=${SLURM_CPUS_PER_TASK:-16}

echo "Executing htar on ${WORKINGDIR} using ${NTHREAD} threads"

TARJOBS="$(find -maxdepth 1 -type d -name 'halos*' -o -name lightcones) $(find -maxdepth 2 -type d -path './slices/z*')"
SLICEPUTJOBS="" #"$(find -maxdepth 2 -type f -path './slices/z*.tar')"
hsi "mkdir $HPSSDIR"

# this will make the SIMNAME_slices directory.
# but we then want the file to be named SIMNAME_slices/SIMNAME_thisslice.tar

for JOB in $TARJOBS; do
    FNNAME="$HPSSDIR/Abacus_${SIM_NAME}_${JOB#"./"}.tar"

    if [[ $JOB == './slices/'* ]]; then
    	TARFN=$(basename ${JOB})
        
    	hsi "mkdir $HPSSDIR/Abacus_${SIM_NAME}_slices"

    	FNNAME="$HPSSDIR/Abacus_${SIM_NAME}_slices/Abacus_${SIM_NAME}_${TARFN}.tar"
    fi

    htar -T $NTHREAD -cvf $FNNAME $JOB
done

for JOB in $SLICEPUTJOBS; do
    TARFN=$(basename ${JOB})
    
    hsi "mkdir $HPSSDIR/Abacus_${SIM_NAME}_slices"
    
    FNNAME="$HPSSDIR/Abacus_${SIM_NAME}_slices/Abacus_${SIM_NAME}_${TARFN}"
    
    hsi -v put $JOB : $FNNAME
    hsi -v put ${JOB}.idx : ${FNNAME}.idx
done

# One more quick job
TOPLEVEL="$(find -maxdepth 1 -type f) log/ info/"

htar -T $NTHREAD -cvf "$HPSSDIR/Abacus_${SIM_NAME}_log_and_info.tar" $TOPLEVEL

# This is a magic string that the assembly line looks for
echo "Abacus htar complete."
