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

-----

| SimName                            | Cosm | Phase   | PPD  | Box (Mpc) | z_Final | Full Outputs | Notes |
| ----------------------------       | ---- | -----   | ---- | ----      | ------- | -----        | ----- |
| AbacusSummit_base_c000_ph000       | 000  | 000     | 6912 | 2000      | 0.1     | Full         | Planck2018 LCDM |
| AbacusSummit_base_c000_ph{001-005} | 000  | 001-005 | 6912 | 2000      | 0.1     | Partial+HiZ  | Planck2018 LCDM |
| AbacusSummit_base_c000_ph{006-024} | 000  | 006-024 | 6912 | 2000      | 0.1     | none         | Planck2018 LCDM |
| AbacusSummit_high_c000_ph100       | 000  | 100     | 6912 | 1000      | 0.8     | Full to 0.8  | High-res LCDM, no lightcone |
| AbacusSummit_high_c000_ph100_base  | 000  | 100     | 3456 | 1000      | 0.8     | Full to 0.8  | Base-res LCDM, no lightcone |
| AbacusSummit_huge_c000_ph100       | 000  | 200     | 10000| 8700      | 0.1     | 1.4, 1.1, 0.8, 0.5, 0.2 | Low-res LCDM, box-centered lightcone |
| AbacusSummit_huge_c000_ph{000-024}_base | 000  | 000-024 | 2304 | 2000 | 0.1     | 1.4, 1.1, 0.8, 0.5, 0.2 | Low-res match to base, no lightcone |
| AbacusSummit_base_c001_ph000       | 001  | 000     | 6912 | 2000      | 0.1     | Partial+HiZ  | Low omega_c |
| AbacusSummit_base_c001_ph{001-005} | 001  | 001-005 | 6912 | 2000      | 0.1     | Partial      | Low omega_c |
| AbacusSummit_base_c002_ph000       | 002  | 000     | 6912 | 2000      | 0.1     | Partial+HiZ  | wCDM w=-0.8? |
| AbacusSummit_base_c002_ph{001-005} | 002  | 001-005 | 6912 | 2000      | 0.1     | Partial      | wCDM w=-0.8? |
| AbacusSummit_base_c003_ph000       | 003  | 000     | 6912 | 2000      | 0.1     | Partial+HiZ  | TBD |
| AbacusSummit_base_c003_ph{001-005} | 003  | 001-005 | 6912 | 2000      | 0.1     | Partial      | TBD |
| AbacusSummit_base_c004_ph000       | 004  | 000     | 6912 | 2000      | 0.1     | Partial+HiZ  | TBD |
| AbacusSummit_base_c004_ph{001-005} | 004  | 001-005 | 6912 | 2000      | 0.1     | Partial      | TBD |
| AbacusSummit_base_c009_ph000       | 009  | 000     | 6912 | 2000      | 0.1     | Partial      | Baseline LCDM with massless neutrinos |
| AbacusSummit_base_c010_ph000       | 010  | 000     | 6912 | 2000      | 0.1     | 0.1          | AbacusCosmos LCDM, Prototype |
| AbacusSummit_base_c011_ph000       | 011  | 000     | 6912 | 2000      | 0.1     | none         | High-sigma8, Prototype |
| AbacusSummit_base_c012_ph000       | 012  | 000     | 6912 | 2000      | 0.1     | none         | Euclid Flagship1 |
| AbacusSummit_base_c013_ph000       | 013  | 000     | 6912 | 2000      | 0.1     | none         | Euclid Flagship2 |
| AbacusSummit_base_c014_ph000       | 014  | 000     | 6912 | 2000      | 0.1     | none         | OuterRim |
| AbacusSummit_base_c015_ph000       | 015  | 000     | 6912 | 2000      | 0.1     | none         | Dark Sky |
| AbacusSummit_base_c016_ph000       | 016  | 000     | 6912 | 2000      | 0.1     | none         | Horizon |
| AbacusSummit_base_c017_ph000       | 017  | 000     | 6912 | 2000      | 0.1     | none         | Illustris |
| AbacusSummit_base_c018_ph000       | 018  | 000     | 6912 | 2000      | 0.1     | none         | Multidark Planck |
