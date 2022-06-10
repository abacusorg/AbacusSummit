#!/usr/bin/env bash

module load esslurm


VERIFIED_BOXES_FN='/global/cfs/cdirs/desi/cosmosim/Abacus/verified_checksums/master.txt'
SIM_NAME="None"
N=0
for i in $(cat $VERIFIED_BOXES_FN); do
	HTAR_LOG="/global/cfs/cdirs/desi/cosmosim/Abacus/scripts/logs/${i}_htar.out"
	
	case `grep -Fx "Abacus htar complete." $HTAR_LOG >/dev/null; echo $?` in
	  0)
	    echo "${i} already completed htar. Continuing"
	    ;;
	  1)
	    echo "${i} has htar underway but not complete. Continuing."
	    ;;
	  *)
	    echo "${i} ELIGIBLE FOR HTAR."
	    SIM_NAME=${i} 
            N=$((N+1))
            echo "Submitting ${SIM_NAME} for htar."
#            sbatch -o ${HTAR_LOG} --job-name="${SIM_NAME}_htar" nersc_htar.slurm $SIM_NAME
	    ;;
	esac

	if [ $N -ge 15 ];  then                 
		break	
	fi	

done

if [ "$SIM_NAME" == "None" ]; then
    echo "No eligible box found for htar-ing. Exiting."
    exit 1
else
    echo "Submitted $N eligible boxes."
    #sbatch -o ${HTAR_LOG} --job-name="${SIM_NAME}_htar" nersc_htar.slurm $SIM_NAME
fi

