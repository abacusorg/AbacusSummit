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

| root               | notes                                                                | omega_b | omega_cdm | h      | A_s       | n_s    | alpha_s | N_ur   | N_ncdm | omega_ncdm | w0_fld | wa_fld | sigma8 |
| ------------------ | -----                                                                | ------- | --------- | ------ | --------- | ------ | ------- | ------ | ------ | ---------- |------- | ------ | ------ |
| abacus_cosm000     | Baseline LCDM, Planck 2018 base_plikHM_TTTEEE_lowl_lowE_lensing mean | 0.02237 |  0.1200   | 0.6736 | 2.0830e-9 | 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 
| abacus_cosm001     | WMAP9+ACT+SPT LCDM, Calabrese++ 2017                                 | 0.02242 |  0.1134   | 0.7030 | 2.0376e-9 | 0.9638 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 
| abacus_cosm002     | wCDM with thawing model w0 = -0.7, wa = -0.5                         | 0.02237 |  0.1200   | TBD    | 2.TBD e-9 | 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 
| abacus_cosm003     | Neff=3.70, from base_nnu_plikHM_TT_lowl_lowE_Riess18_post_BAO        | 0.02260 |  0.1291   | 0.7160 | 2.2438e-9 | 0.9876 | 0.0     | 2.6868 | 1      | 0.00064420 | -1.0   | 0.0    | 
| abacus_cosm004     | Low sigma8_matter = 0.75, otherwise Baseline LCDM                    | 0.02237 |  0.1200   | 0.6736 | 1.7949e-9 | 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 
| abacus_cosm009     | Baseline LCDM with massless neutrinos matching omega_cb & sigma8_cb  | 0.02237 |  0.1200   | 0.6736 | 2.0417e-9 | 0.9649 | 0.0     | 3.046  | 0      | 0.0        | -1.0   | 0.0    | 
| abacus_cosm010     | AbacusCosmos Planck LCDM cosmology                                   | 0.02222 |  0.1199   | 0.6726 | 2.100e-9  | 0.9652 | 0.0     | 3.04   | 0      | 0.0        | -1.0   | 0.0    | 
| abacus_cosm011     | AbacusCosmos Planck LCDM cosmology +10% in sigma8                    | 0.02222 |  0.1199   | 0.6726 | 2.541e-9  | 0.9652 | 0.0     | 3.04   | 0      | 0.0        | -1.0   | 0.0    | 
| abacus_cosm012     | Euclid Flagship1 LCDM, sigma8_m=0.8279                               | 0.02200 |  0.1212   | 0.6700 | 2.1000e-9 | 0.9600 | 0.0     | 3.046  | 0      | 0.0        | -1.0   | 0.0    | 
| abacus_cosm013     | Euclid Flagship2 LCDM, sigma8_m=0.813715, sigma8_cb=0.817135         | 0.02200 |  0.1206   | 0.6700 | 2.1000e-9 | 0.9600 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 
| abacus_cosm014     | OuterRim LCDM, sigma8=0.80                                           | 0.02258 |  0.1109   | 0.7100 | 2.1591e-9 | 0.9630 | 0.0     | 3.046  | 0      | 0.0        | -1.0   | 0.0    | 
| abacus_cosm015     | DarkSky LCDM, sigma8=0.835                                           | 0.02215 |  0.1175   | 0.6880 | 2.1852e-9 | 0.9688 | 0.0     | 3.046  | 0      | 0.0        | -1.0   | 0.0    | 
| abacus_cosm016     | Horizon Run 4 LCDM, sigma8=0.7937                                    | 0.02281 |  0.1120   | 0.7200 | 2.0996e-9 | 0.9600 | 0.0     | 3.046  | 0      | 0.0        | -1.0   | 0.0    | 
| abacus_cosm017     | IllustrisTNG LCDM, sigma8=0.8159                                     | 0.02230 |  0.1194   | 0.6774 | 2.0671e-9 | 0.9667 | 0.0     | 3.046  | 0      | 0.0        | -1.0   | 0.0    | 
| abacus_cosm018     | MultiDark Planck LCDM, sigma8=0.8228                                 | 0.02214 |  0.1189   | 0.6777 | 2.1022e-9 | 0.9600 | 0.0     | 3.046  | 0      | 0.0        | -1.0   | 0.0    | 
| abacus_cosm100     | Baseline +2% ln(omega_b)                                             | 0.02282 |  0.1200   | TBD    | 2.TBD e-9 | 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 
| abacus_cosm101     | Baseline -2% ln(omega_b)                                             | 0.02193 |  0.1200   | TBD    | 2.TBD e-9 | 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 
| abacus_cosm102     | Baseline +3.3% ln(omega_c)                                           | 0.02237 |  0.1240   | TBD    | 2.TBD e-9 | 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 
| abacus_cosm103     | Baseline -3.3% ln(omega_c)                                           | 0.02237 |  0.1161   | TBD    | 2.TBD e-9 | 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 
| abacus_cosm104     | Baseline +0.01 n_s                                                   | 0.02237 |  0.1200   | TBD    | 2.TBD e-9 | 0.9749 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 
| abacus_cosm105     | Baseline -0.01 n_s                                                   | 0.02237 |  0.1200   | TBD    | 2.TBD e-9 | 0.9549 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 
| abacus_cosm106     | Baseline +0.02 nrun                                                  | 0.02237 |  0.1200   | TBD    | 2.TBD e-9 | 0.9649 | 0.02    | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 
| abacus_cosm107     | Baseline -0.02 nrun                                                  | 0.02237 |  0.1200   | TBD    | 2.TBD e-9 | 0.9649 | -0.02   | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 
| abacus_cosm108     | Baseline +0.1 w0                                                     | 0.02237 |  0.1200   | TBD    | 2.TBD e-9 | 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -0.9   | 0.0    | 
| abacus_cosm109     | Baseline -0.1 w0                                                     | 0.02237 |  0.1200   | TBD    | 2.TBD e-9 | 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.1   | 0.0    | 
| abacus_cosm110     | Baseline +0.4 wa, -0.1 w0                                            | 0.02237 |  0.1200   | TBD    | 2.TBD e-9 | 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.1   | 0.4    | 
| abacus_cosm111     | Baseline -0.4 wa, +0.1 w0                                            | 0.02237 |  0.1200   | TBD    | 2.TBD e-9 | 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -0.9   | -0.4   | 
| abacus_cosm112     | Baseline +2% sigma8                                                  | 0.02237 |  0.1200   | 0.6736 | 2.1672e-9 | 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 
| abacus_cosm113     | Baseline -2% sigma8                                                  | 0.02237 |  0.1200   | 0.6736 | 2.0021e-9 | 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 
| abacus_cosm114     | Baseline +0.3 nnu, +3.3% ln(omega_c), +0.01 n_s                      | 0.02237 |  0.1240   | TBD    | 2.TBD e-9 | 0.9749 | 0.0     | 2.3328 | 1      | 0.00064420 | -1.0   | 0.0    | 
| abacus_cosm115     | Baseline -0.3 nnu, -3.3% ln(omega_c), -0.01 n_s                      | 0.02237 |  0.1161   | TBD    | 2.TBD e-9 | 0.9549 | 0.0     | 1.7328 | 1      | 0.00064420 | -1.0   | 0.0    | 

Need to choose 3 other secondary cosmologies, at least one nonLCDM.  Probably one wCDM, one high Neff, one low S8.

wCDM: Chose w0=-0.7, wa=-0.5 to be an extreme thawing model.

Neff=3.70 cosmology: Took the chains from base_nnu_plikHM_TT_lowl_lowE_Riess18_post_BAO and averaged those in 3.595<nnu<3.90, chosen so that the weighted mean was 3.70.  Also standardized As to tau=0.0544.

Low sigma8: Opted to drop the amplitude by about 7.7%, to make sigma8(matter)=0.75.  This is a pretty shift, but there's lots of ways to damp power.

For the grid of positive/negative excursions for linear derivatives around the baseline LCDM, we opted for the simplicity of 
rectalinear derivatives in ln(omega_b), ln(omega_c), ns, nrun, sigma8, w0.  Note that we treat sigma8, not As, as the independent variable,
in the expectation that this will keep large-scale structure closer to constant.  
For wa, we opt to hold w(z=0.333)=w0+0.25*wa fixed, close to the mirage model.  
For Neff, the Planck chains suggested substantial degeneracies with omegac and ns, so we opt to move these two along
with Neff to stay close to the CMB degeneracy direction.

TODOs:

Could include the cosmologies of the recent ANL big runs as abacus_cosm019..021.
