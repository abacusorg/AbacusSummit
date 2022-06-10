#!/usr/bin/env bash
#SBATCH --qos=xfer
#SBATCH --time=24:00:00
#SBATCH --licenses=SCRATCH
##SBATCH --mem 0  # all memory
##SBATCH --ntasks-per-node=1
##SBATCH -c 16

##SBATCH -N 1
##SBATCH --ntasks-per-node=1
##SBATCH -c 16
##SBATCH -C haswell
##SBATCH -q xfer
##SBATCH --mem 0  # all memory
##SBATCH -t 24:00:00  # dtn wall clock unlimited

set -e  # quit on error

#module load esslurm

# This script runs htar to store files on tape (HPSS).
# Deletion of the originals will be taken care of later by hand

# While it's not obvious that one needs an allocation to run htar,
# it is multi-threaded and it thus seems prudent to avoid using a login node.
# We could imagine using the DTNs, but it's hard to know if a job is running or crashed

SIM_SET=${SIM_SET:-ScaleFree}
SIM_NAME=$1
HPSS_PREFIX="Abacus_ScaleFree"

WORKINGDIR=/project/projectdirs/desi/cosmosim/Abacus/extra/$SIM_NAME
HPSSDIR=/nersc/projects/desi/cosmosim/Abacus/$SIM_SET/$SIM_NAME
cd $WORKINGDIR

NTHREAD=${SLURM_CPUS_PER_TASK:-16}

echo "Executing $NTHREAD parallel htar jobs on $WORKINGDIR"

#htar -T $NTHREAD -cPvf "/hpss/prod/ast145/proj-shared/$SIM_SET/${SIM_NAME}.tar" $WORKINGDIR

#TARJOBS="$(find * -maxdepth 1 -type d -name 'halos*' -o -name lightcones)"
SLICEJOBS="$(find * -maxdepth 1 -type d -path 'slices/z*')"
hsi "mkdir $HPSSDIR"
[[ ! -z $SLICEJOBS ]] && hsi "mkdir $HPSSDIR/slices"
echo $SLICEJOBS

for JOB in $SLICEJOBS; do
    # do string substitution to get slices_z1 from slices/z1
    FNNAME="$HPSSDIR/$(dirname $JOB)/${HPSS_PREFIX}_${SIM_NAME}_${JOB//'/'/'_'}.tar"
	echo "FNNAME: \"${FNNAME}\""

    htar -T $NTHREAD -cvf $FNNAME $JOB
done

# One more quick job
TOPLEVEL="$(find -maxdepth 1 -type f) log/ info/"
htar -T $NTHREAD -cvf "$HPSSDIR/${HPSS_PREFIX}_${SIM_NAME}_log_and_info.tar" $TOPLEVEL

# This is a magic string that the assembly line looks for
echo "Abacus htar complete."



