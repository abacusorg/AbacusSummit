# Perlmutter CPU environment

module load python/3.9-anaconda-2021.11
#python -m venv /global/common/software/desi/users/lgarriso/venv_ic  # bootstrap

module load PrgEnv-gnu
module load cray-fftw
#module load gsl/2.7

module use $HOME/abacus/modulefiles
module load abacus

. $HOME/oneTBB/build/gnu_11.2_cxx11_64_relwithdebinfo/vars.sh

for dir in $HOME/installs/$NERSC_HOST/{gsl,swig,valgrind}; do
    [[ -d $dir/bin ]] && export PATH=$dir/bin:$PATH
    [[ -d $dir/lib ]] && export LD_LIBRARY_PATH=$dir/lib:$LD_LIBRARY_PATH
    [[ -d $dir/lib ]] && export LIBRARY_PATH=$dir/lib:$LIBRARY_PATH
    [[ -d $dir/include ]] && export CPATH=$dir/include:$CPATH
done

. /global/common/software/desi/users/lgarriso/venv_ic/bin/activate

export CXX=CC
export CC=cc

export SBATCH_ACCOUNT=desi
export SALLOC_ACCOUNT=desi
