# AbacusSummit/Simulations

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

The cosmologies in the "Cosm" column are tabulated in [Cosmologies](../Cosmologies/README.md).

-----

| SimName                            | Cosm | Phase   | PPD  | Box (Mpc/h) | z_Final | Full Outputs | Notes |
| ----------------------------       | ---- | -----   | ---- | ----      | ------- | -----        | ----- |
| AbacusSummit_base_c000_ph000       | 000  | 000     | 6912 | 2000      | 0.1     | Full         | Planck2018 LCDM |
| AbacusSummit_base_c000_ph{001-005} | 000  | 001-005 | 6912 | 2000      | 0.1     | Partial+HiZ  | Planck2018 LCDM |
| AbacusSummit_base_c000_ph{006-024} | 000  | 006-024 | 6912 | 2000      | 0.1     | none         | Planck2018 LCDM |
| AbacusSummit_fixedbase_c000_ph099  | 000  | 099     | 4096 | 1185      | 0.1     | Full         | Base-res LCDM, fixed amplitudes |
| AbacusSummit_fixedbase_c{001-004}_ph099 | 001-005  | 099 | 4096 | 1185 | 0.1     | Partial      | Base-res LCDM, fixed amplitudes |
| AbacusSummit_fixedbase_c000_ph098  | 000  | 098     | 4096 | 1185      | 0.1     | Full         | Base-res LCDM, fixed amplitudes, inversion of phase 99 |
| AbacusSummit_high_c000_ph100       | 000  | 100     | 6300 | 1000      | 0.1     | Full         | High-res LCDM, no lightcone |
| AbacusSummit_highbase_c000_ph100   | 000  | 100     | 3456 | 1000      | 0.1     | Full         | Base-res LCDM, no lightcone |
| AbacusSummit_huge_c000_ph200       | 000  | 200     | 10000| 8700      | 0.1     | 1.4, 1.1, 0.8, 0.5, 0.2 | Low-res LCDM, box-centered lightcone |
| AbacusSummit_huge_c000_ph201       | 000  | 201     | 8640 | 7500      | 0.1     | 1.4, 1.1, 0.8, 0.5, 0.2 | Low-res LCDM, box-centered lightcone |
| AbacusSummit_hugebase_c000_ph{000-024} | 000  | 000-024 | 2304 | 2000 | 0.1     | 1.4, 1.1, 0.8, 0.5, 0.2 | Low-res match to base, no lightcone |
| AbacusSummit_base_c001_ph000       | 001  | 000     | 6912 | 2000      | 0.1     | Partial+HiZ  | Low omega_c |
| AbacusSummit_base_c001_ph{001-005} | 001  | 001-005 | 6912 | 2000      | 0.1     | Partial      | Low omega_c |
| AbacusSummit_base_c002_ph000       | 002  | 000     | 6912 | 2000      | 0.1     | Partial+HiZ  | wCDM with thawing model w0 = -0.7, wa = -0.5 |
| AbacusSummit_base_c002_ph{001-005} | 002  | 001-005 | 6912 | 2000      | 0.1     | Partial      | wCDM with thawing model w0 = -0.7, wa = -0.5 |
| AbacusSummit_base_c003_ph000       | 003  | 000     | 6912 | 2000      | 0.1     | Partial+HiZ  | Neff=3.70, from base_nnu_plikHM_TT_lowl_lowE_Riess18_post_BAO |
| AbacusSummit_base_c003_ph{001-005} | 003  | 001-005 | 6912 | 2000      | 0.1     | Partial      | Neff=3.70, from base_nnu_plikHM_TT_lowl_lowE_Riess18_post_BAO |
| AbacusSummit_base_c004_ph000       | 004  | 000     | 6912 | 2000      | 0.1     | Partial+HiZ  | Low sigma8_matter = 0.75, otherwise Baseline LCDM |
| AbacusSummit_base_c004_ph{001-005} | 004  | 001-005 | 6912 | 2000      | 0.1     | Partial      | Low sigma8_matter = 0.75, otherwise Baseline LCDM |
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
| AbacusSummit_base_c019_ph000       | 019  | 000     | 6912 | 2000      | 0.1     | none         | Baseline LCDM w/2 massive neutrino species |
| AbacusSummit_base_c020_ph000       | 020  | 000     | 6912 | 2000      | 0.1     | none         | Baseline LCDM with massless neutrinos |
| AbacusSummit_highbase_c021_ph000   | 021  | 000     | 3456 | 1000      | 0.1     | Partial      | MassiveNUs with massless neutrinos |
| AbacusSummit_highbase_c022_ph000   | 022  | 000     | 3456 | 1000      | 0.1     | Partial      | MassiveNUs w/1 massive 0.1 eV neutrino species |
| AbacusSummit_base_c{100-115}_ph000 | 100-115  | 000     | 6912 | 2000      | 0.1     | none         | Linear Derivative Grid |
| AbacusSummit_base_c116_ph000       | 116  | 000     | 6912 | 2000      | 0.1     | none         | Linear Derivative Grid |
| AbacusSummit_base_c{117-126}_ph000 | 117-126  | 000     | 6912 | 2000      | 0.1     | none         | Linear Derivative Grid |
| AbacusSummit_base_c{130-181}_ph000 | 130-181  | 000     | 6912 | 2000      | 0.1     | none         | Broader Emulator Grid  |

### TODO: these cosmologies do not yet exist
\# | AbacusSummit_base_c019_ph000       | 019  | 000     | 6912 | 2000      | 0.1     | none         | ANL LCDM |

\# | AbacusSummit_base_c020_ph000       | 020  | 000     | 6912 | 2000      | 0.1     | none         | ANL wCDM |

\# | AbacusSummit_base_c{050-059}_ph000 | 050-059  | 000     | 6912 | 2000      | 0.1     | none         | Blinded Cosmologies |

\# | AbacusSummit_base_c{182-199}_ph000 | 182-199  | 000     | 6912 | 2000      | 0.1     | none         | Broader Emulator Grid  |

