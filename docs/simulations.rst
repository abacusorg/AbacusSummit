Simulations
===========

This directory contains the specification of the simulations in AbacusSummit.

Each simulation has a name, which is both the name of the subdirectory and the 
SimName inside the parameter file.  Inside the subdirectory is the abacus.par2
file, which is the user-customized instructions to the code, and some of the 
run-time information.

Run-time products: We may want to check in the final parameter file (abacus.par) as
well as the final status.log.

Only a few of our simulations include the full timeslice output;
we typically output only subsamples.  The full list is z=3.0, 2.5,
2.0, 1.7, 1.4, 1.1, 0.8, 0.5, 0.4, 0.3, 0.2, 0.1.  The partial
list is z = 2.5, 1.4, 0.8, 0.2.  Partial+HiZ adds z=3.0 and 2.0 to that.

A base simulation typically produces about 10 TB of subsampled output, and 
each output slice is another 4 TB above that.

At present, we're planning for 12 particle subsample redshifts, 24 groups-only redshifts,
and 3 subsample lightcones.

The cosmologies in the "Cosm" column are tabulated in :doc:`cosmologies`.

-----

Download the simulations table `here <https://github.com/abacusorg/AbacusSummit/blob/master/Simulations/simulations.csv>`_.

.. note:: The following table is wide, you may have to scroll to the right to see all the columns.

.. csv-table::
    :file: ../Simulations/simulations.csv
    :header-rows: 1
    :escape: '
