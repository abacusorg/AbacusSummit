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

| root               | notes | omega_b | omega_cdm | h      | A_s       | n_s    | alpha_s | N_ur   | N_ncdm | omega_ncdm | w0_fld | wa_fld | 
| ------------------ | ----- | ------- | --------- | ------ | --------- | ------ | ------- | ------ | ------ | ---------- |------- | ------ | 
| abacus_cosm000     | Baseline LCDM, Planck 2018 base_plikHM_TTTEEE_lowl_lowE_lensing mean | 0.02237 |  0.1200   | 0.6736 | 2.0830e-9 | 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 
| abacus_cosm001     | Baseline LCDM, but with massless neutrinos (high redshift constant, so lower Omega_m) | 0.02237 |  0.1200   | 0.6736 | 2.0830e-9 | 0.9649 | 0.0     | 3.046  | 0      | 0.0        | -1.0   | 0.0    | 
| abacus_cosm010     | AbacusCosmos Planck cosmology.  Original used RecFast, not HyRec, but match in Pk<0.1% | 0.02222 |   0.1199  | 0.6726 | 2.1e-9    | 0.9652 | 0.0     | 3.04   | 0      | 0.0        | -1.0   | 0.0    | 
| abacus_cosm020     | Baseline LCDM but increased in sigma8 by 10%. | 0.02237 |   0.1200  | 0.6736 | 2.5204e-9 | 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0  |  0.0    | 
