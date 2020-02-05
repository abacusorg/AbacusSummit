## This directory contains the specification of the Cosmologies and the CLASS
parameters that they define.

We have given the cosmologies numbers, so that the simulations will refer to c123.

The cosmologies and their parameters are enumerated in this file, which we parse to 
make the CLASS input files and parameter files.

-------

All cosmologies use tau=0.0544.  Most use 60 meV neutrinos, omega_nu = 0.00064420, scaling from z=1.
We use HyRec, rather than RecFast.

CLASS is run with the pk_ref.pre precision choices, unless the name ends with _fast, in which case we use the defaults.

Remember that Omega_m = (omega_b+omega_cdm+oemga_ncdm)/h^2.

We output five redshifts from CLASS, z=0.0, 1.0, 3.0, 7.0, and 49, which are called z1,z2,z3,z4,z5.

We use the CDM+Baryon power spectrum at z=1 (z2_pk_cb) and scale back by D(z_init)/D(1) 
to define our matter-dominated CDM-only simulation IC.  The growth function includes the
neutrinos as a smooth component.

| root               | notes                                                                | omega_b | omega_cdm | h      | A_s       | n_s    | alpha_s | N_ur   | N_ncdm | omega_ncdm | w0_fld | wa_fld | 
| ------------------ | -----                                                                | ------- | --------- | ------ | --------- | ------ | ------- | ------ | ------ | ---------- |------- | ------ | 
| abacus_cosm000     | Baseline LCDM, Planck 2018 base_plikHM_TTTEEE_lowl_lowE_lensing mean | 0.02237 |  0.1200   | 0.6736 | 2.0830e-9 | 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 
| abacus_cosm001     | WMAP9+ACT+SPT LCDM, Calabrese++ 2017                                 | 0.02242 |  0.1134   | 0.7030 | 2.0376e-9 | 0.9638 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 
| abacus_cosm009     | Baseline LCDM with massless neutrinos matching omega_cb & sigma8_cb  | 0.02237 |  0.1200   | 0.6736 | 2.0417e-9 | 0.9649 | 0.0     | 3.046  | 0      | 0.0        | -1.0   | 0.0    | 
| abacus_cosm010     | AbacusCosmos Planck LCDM cosmology                                   | 0.02222 |  0.1199   | 0.6726 | 2.100e-9  | 0.9652 | 0.0     | 3.04   | 0      | 0.0        | -1.0   | 0.0    | 
| abacus_cosm011     | AbacusCosmos Planck LCDM cosmology +10% in sigma8                    | 0.02222 |  0.1199   | 0.6726 | 2.541e-9  | 0.9652 | 0.0     | 3.04   | 0      | 0.0        | -1.0   | 0.0    | 
| abacus_cosm012     | Euclid Flagship1 LCDM, sigma8_m=0.8279                               | 0.02200 |  0.1212   | 0.6700 | 2.1000e-9 | 0.9600 | 0.0     | 3.046  | 0      | 0.0        | -1.0   | 0.0    | 
| abacus_cosm013     | Euclid Flagship2 LCDM, sigma8_m=0.813715, sigma8_cb=0.817135         | 0.02200 |  0.1206   | 0.6700 | 2.1000e-9 | 0.9600 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 
| abacus_cosm014     | OuterRim LCDM, sigma8=0.80                                           | 0.02258 |  0.1109   | 0.7100 | 2.1591e-9 | 0.9630 | 0.0     | 3.046  | 0      | 0.0        | -1.0   | 0.0    | 
| abacus_cosm015     | DarkSky LCDM, sigma8=0.835                                           | 0.02215 |  0.1175   | 0.6880 | 2.1852e-9 | 0.9688 | 0.0     | 3.046  | 0      | 0.0        | -1.0   | 0.0    | 
| abacus_cosm016     | Horizon Run 4 LCDM, sigma8=0.7937                                    | 0.02281 |  0.1120   | 0.7200 | 2.0996e-9 | 0.9600 | 0.0     | 3.046  | 0      | 0.0        | -1.0   | 0.0    | 
| abacus_cosm017     | IllustrisTNG LCDM, sigma8=0.8159                                     | 0.02230 |  0.1194   | 0.6774 | 2.0671e-9 | 0.9667 | 0.0     | 3.046  | 0      | 0.0        | -1.0   | 0.0    | 

TODOs:

Need to choose 3 other secondary cosmologies, at least one nonLCDM.  Probably one wCDM, one high Neff, one low S8.

abacus_cosm018 = ANL LCDM
abacus_cosm019 = ANL wCDM
