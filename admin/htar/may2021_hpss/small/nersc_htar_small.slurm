#!/usr/bin/env bash
#SBATCH --qos=xfer  # https://docs.nersc.gov/jobs/examples/#xfer-queue
#SBATCH --time=2-0  # max time 2 days
#SBATCH --mem 10GB  # docs recommend > 8 GB for large files

# This script is called from nersc_htar.sh

set -e  # quit on error

module load esslurm

# This script runs htar to store files on tape (HPSS).
# Deletion of the originals will be taken care of later by hand

# map 0-99 to 3000-4999
PHASEPAT1=$((300 + 2*SLURM_ARRAY_TASK_ID))'?'
PHASEPAT2=$((300 + 2*SLURM_ARRAY_TASK_ID + 1))'?'

PHSTART=$((3000 + 20*SLURM_ARRAY_TASK_ID))
PHEND=$((3000 + 20*SLURM_ARRAY_TASK_ID + 19))

WORKINGDIR=$CFS/desi/cosmosim/Abacus/small
HPSSDIR=/nersc/projects/desi/cosmosim/Abacus/small
cd $WORKINGDIR

NTHREAD=${SLURM_CPUS_PER_TASK:-16}

echo "Executing htar on ${WORKINGDIR} using ${NTHREAD} threads"

SIMS="$(find -maxdepth 1 -type d -name "AbacusSummit_small_c000_ph${PHASEPAT1}" -o -name "AbacusSummit_small_c000_ph${PHASEPAT2}" | sort)"

TARNAME="Abacus_small_AbacusSummit_small_c000_ph${PHSTART}-${PHEND}.tar"
htar -T $NTHREAD -cvf "${HPSSDIR}/${TARNAME}" ${SIMS}

# This is a magic string that the assembly line looks for
echo "Abacus htar complete."
