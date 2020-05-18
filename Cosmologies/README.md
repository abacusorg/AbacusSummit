# AbacusSummit/Cosmologies

This directory contains the specification of the Cosmologies and the CLASS
parameters that they define.

We have given the cosmologies numbers, so that the simulations will refer to c123.

The cosmologies and their parameters are enumerated in this file, which we parse to 
make the CLASS input files and parameter files.

There are various sets of cosmologies in this list.

1) The primary cosmology (c000) is a Planck2018 LCDM version, specifically the mean of base_plikHM_TTTEEE_lowl_lowE_lensing.
This cosmology has 25 base boxes, plus other mass resolution options.  c009 is the same cosmology, but with massless neutrinos.

2) There are 4 secondary cosmologies (c001-4), each with 6 base boxes.  There is a low-omega_c choice based on WMAP7,
a wCDM choice, a high-Neff choice, and a low-sigma8 choice.

3) There are about ten reference cosmologies (c010-c018) that match the choices employed in flagship runs from
other groups, so ease comparisons between code bases.

4) There is a linear derivative grid (c100-c116) that provides 8 matched pairs, with small positive and negative steps
in an 8-dimensional parameter space, plus one additional simulation that is the high-sigma8 partner to the low-sigma8
secondary cosmology.

5) There is a larger unstructured emulator grid (c130-c181) that provides a wider coverage of this 8-dimensional space.

Further details are below the table.

-------

All cosmologies use tau=0.0544.  Most use 60 meV neutrinos, omega_nu = 0.00064420, scaling from z=1.
We use HyRec, rather than RecFast.

CLASS is run with the pk_ref.pre precision choices, unless the name ends with \_fast, in which case we use the defaults.
There was one case where CLASS underflowed an integration tolerance with the pk_ref precisions; we reverted to pk_permille.pre
for this.

Remember that Omega_m = (omega_b+omega_cdm+oemga_ncdm)/h^2.

We output five redshifts from CLASS, z=0.0, 1.0, 3.0, 7.0, and 49, which are called z1,z2,z3,z4,z5.

We use the CDM+Baryon power spectrum at z=1 (z2_pk_cb) and scale back by D(z_init)/D(1) 
to define our matter-dominated CDM-only simulation IC.  The growth function includes the
neutrinos as a smooth component.

| root               | notes                                                                | omega_b | omega_cdm | h      | A_s       | n_s    | alpha_s | N_ur   | N_ncdm | omega_ncdm | w0_fld | wa_fld | sigma8_m | sigma8_cb |
| ------------------ | -----                                                                | ------- | --------- | ------ | --------- | ------ | ------- | ------ | ------ | ---------- |------- | ------ | -------- | --------- |
| abacus_cosm000     | Baseline LCDM, Planck 2018 base_plikHM_TTTEEE_lowl_lowE_lensing mean | 0.02237 |  0.1200   | 0.6736 | 2.0830e-9 | 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 0.807952 | 0.811355  | 
| abacus_cosm001     | WMAP9+ACT+SPT LCDM, Calabrese++ 2017                                 | 0.02242 |  0.1134   | 0.7030 | 2.0376e-9 | 0.9638 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 0.776779 | 0.780222  | 
| abacus_cosm002     | wCDM with thawing model w0 = -0.7, wa = -0.5                         | 0.02237 |  0.1200   | 0.6278 | 2.3140e-09| 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -0.7   | -0.5    | 0.808189 | 0.811577  | 
| abacus_cosm003     | Neff=3.70, from base_nnu_plikHM_TT_lowl_lowE_Riess18_post_BAO        | 0.02260 |  0.1291   | 0.7160 | 2.2438e-9 | 0.9876 | 0.0     | 2.6868 | 1      | 0.00064420 | -1.0   | 0.0    | 0.855190 | 0.858583  | 
| abacus_cosm004     | Low sigma8_matter = 0.75, otherwise Baseline LCDM                    | 0.02237 |  0.1200   | 0.6736 | 1.7949e-9 | 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 0.749999 | 0.753159  | 
| abacus_cosm009     | Baseline LCDM with massless neutrinos matching omega_cb & sigma8_cb  | 0.02237 |  0.1200   | 0.6736 | 2.0417e-9 | 0.9649 | 0.0     | 3.046  | 0      | 0.0        | -1.0   | 0.0    | 0.811362 |0.811362  | 
| abacus_cosm010     | AbacusCosmos Planck LCDM cosmology                                   | 0.02222 |  0.1199   | 0.6726 | 2.100e-9  | 0.9652 | 0.0     | 3.04   | 0      | 0.0        | -1.0   | 0.0    | 0.823630 |0.823630  | 
| abacus_cosm011     | AbacusCosmos Planck LCDM cosmology +10% in sigma8                    | 0.02222 |  0.1199   | 0.6726 | 2.541e-9  | 0.9652 | 0.0     | 3.04   | 0      | 0.0        | -1.0   | 0.0    | 0.905993 |0.905993  | 
| abacus_cosm012     | Euclid Flagship1 LCDM, sigma8_m=0.8279                               | 0.02200 |  0.1212   | 0.6700 | 2.1000e-9 | 0.9600 | 0.0     | 3.046  | 0      | 0.0        | -1.0   | 0.0    | 0.827899 |0.827899  | 
| abacus_cosm013     | Euclid Flagship2 LCDM, sigma8_m=0.813715, sigma8_cb=0.817135         | 0.02200 |  0.1206   | 0.6700 | 2.1000e-9 | 0.9600 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 0.813715 | 0.817135  | 
| abacus_cosm014     | OuterRim LCDM, sigma8=0.80                                           | 0.02258 |  0.1109   | 0.7100 | 2.1591e-9 | 0.9630 | 0.0     | 3.046  | 0      | 0.0        | -1.0   | 0.0    | 0.800000 |0.800000  | 
| abacus_cosm015     | DarkSky LCDM, sigma8=0.835                                           | 0.02215 |  0.1175   | 0.6880 | 2.1852e-9 | 0.9688 | 0.0     | 3.046  | 0      | 0.0        | -1.0   | 0.0    | 0.835005 |0.835005  | 
| abacus_cosm016     | Horizon Run 4 LCDM, sigma8=0.7937                                    | 0.02281 |  0.1120   | 0.7200 | 2.0996e-9 | 0.9600 | 0.0     | 3.046  | 0      | 0.0        | -1.0   | 0.0    | 0.793693 |0.793693  | 
| abacus_cosm017     | IllustrisTNG LCDM, sigma8=0.8159                                     | 0.02230 |  0.1194   | 0.6774 | 2.0671e-9 | 0.9667 | 0.0     | 3.046  | 0      | 0.0        | -1.0   | 0.0    | 0.815903 |0.815903  | 
| abacus_cosm018     | MultiDark Planck LCDM, sigma8=0.8228                                 | 0.02214 |  0.1189   | 0.6777 | 2.1022e-9 | 0.9600 | 0.0     | 3.046  | 0      | 0.0        | -1.0   | 0.0    | 0.819708 |0.819708  |
| abacus_cosm019     | Baseline LCDM with two 0.06 eV neutrinos                             | 0.02237 |  0.1200   | 0.6683 | 2.1353e-09| 0.9649 | 0.0     | 1.0196 | 2      | 0.00064420,0.00064420 | -1.0   | 0.0    |0.805050 | 0.811826  | 
| abacus_cosm020     | Baseline LCDM w/ massless neutrinos matching theta_star & sigma8_cb  | 0.02237 |  0.1200   | 0.6790 | 2.0342e-09| 0.9649 | 0.0     | 3.046  | 0      | 0.0        | -1.0   | 0.0    | 0.811350 |0.811350  |
| abacus_cosm021     | MassiveNUs massless base                                             | 0.02254 |  0.12446  | 0.700  | 2.1000e-9 | 0.9700 | 0.0     | 3.046  | 0      | 0.0        | -1.0   | 0.0    |0.849842 |0.849842  | 
| abacus_cosm022     | MassiveNUs with one 0.1 eV massive neutrino species                  | 0.02254 |  0.12446  | 0.700  | 2.1000e-9 | 0.9700 | 0.0     | 2.0328 | 1      | 0.001074   | -1.0   | 0.0    | 0.829583 | 0.834908  | 
| abacus_cosm100     | Baseline +2% ln(omega_b)                                             | 0.02282 |  0.1200   | 0.6777 | 2.0934e-09| 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 0.808181 | 0.811575  | 
| abacus_cosm101     | Baseline -2% ln(omega_b)                                             | 0.02193 |  0.1200   | 0.6696 | 2.0751e-09| 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 0.808156 | 0.811570  | 
| abacus_cosm102     | Baseline +3.3% ln(omega_c)                                           | 0.02237 |  0.1240   | 0.6597 | 2.0205e-09| 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 0.808270 | 0.811574  | 
| abacus_cosm103     | Baseline -3.3% ln(omega_c)                                           | 0.02237 |  0.1161   | 0.6877 | 2.1541e-09| 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 0.808075 | 0.811582  | 
| abacus_cosm104     | Baseline +0.01 n_s                                                   | 0.02237 |  0.1200   | 0.6736 | 2.0684e-09| 0.9749 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 0.808166 | 0.811572  | 
| abacus_cosm105     | Baseline -0.01 n_s                                                   | 0.02237 |  0.1200   | 0.6736 | 2.0999e-09| 0.9549 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 0.808177 | 0.811580  | 
| abacus_cosm106     | Baseline +0.02 nrun                                                  | 0.02237 |  0.1200   | 0.6736 | 2.0638e-09| 0.9649 | 0.02    | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 0.808181 | 0.811586  | 
| abacus_cosm107     | Baseline -0.02 nrun                                                  | 0.02237 |  0.1200   | 0.6736 | 2.1045e-09| 0.9649 | -0.02   | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 0.808168 | 0.811571  | 
| abacus_cosm108     | Baseline +0.1 w0                                                     | 0.02237 |  0.1200   | 0.6444 | 2.2390e-09| 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -0.9   | 0.0    | 0.808177 | 0.811570  | 
| abacus_cosm109     | Baseline -0.1 w0                                                     | 0.02237 |  0.1200   | 0.7037 | 1.9465e-09| 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.1   | 0.0    | 0.808161 | 0.811576  | 
| abacus_cosm110     | Baseline +0.4 wa, -0.1 w0                                            | 0.02237 |  0.1200   | 0.6698 | 2.1219e-09| 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.1   | 0.4    | 0.808170 | 0.811572  | 
| abacus_cosm111     | Baseline -0.4 wa, +0.1 w0                                            | 0.02237 |  0.1200   | 0.6752 | 2.0639e-09| 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -0.9   | -0.4   | 0.808179 | 0.811584  | 
| abacus_cosm112     | Baseline +2% sigma8                                                  | 0.02237 |  0.1200   | 0.6736 | 2.1672e-9 | 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 0.824120 | 0.827591  | 
| abacus_cosm113     | Baseline -2% sigma8                                                  | 0.02237 |  0.1200   | 0.6736 | 2.0021e-9 | 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 0.792107 | 0.795443  | 
| abacus_cosm114     | Baseline +0.3 nnu, +3.3% ln(omega_c), +0.01 n_s                      | 0.02237 |  0.1240   | 0.6947 | 2.0463e-09| 0.9749 | 0.0     | 2.3328 | 1      | 0.00064420 | -1.0   | 0.0    | 0.808245 | 0.811563  | 
| abacus_cosm115     | Baseline -0.3 nnu, -3.3% ln(omega_c), -0.01 n_s                      | 0.02237 |  0.1161   | 0.6517 | 2.1211e-09| 0.9549 | 0.0     | 1.7328 | 1      | 0.00064420 | -1.0   | 0.0    | 0.808089 | 0.811582  | 
| abacus_cosm116     | Emulator grid around baseline cosmology                              | 0.02237 |  0.1200   | 0.6736 | 2.3938e-09| 0.9649 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.000 | 0.000  | 0.866133 | 0.869782  |
| abacus_cosm117     | Baseline +0.83% ln(omega_c)                                          | 0.02237 |  0.1210   | 0.6701 | 2.0675e-09| 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 0.808205 | 0.811584  | 
| abacus_cosm118     | Baseline -0.83% ln(omega_c)                                          | 0.02237 |  0.1190   | 0.6771 | 2.1014e-09| 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 0.808152 | 0.811582  | 
| abacus_cosm119     | Baseline +0.003 n_s                                                  | 0.02237 |  0.1200   | 0.6736 | 2.0794e-09| 0.9679 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 0.808168 | 0.811573  | 
| abacus_cosm120     | Baseline -0.003 n_s                                                  | 0.02237 |  0.1200   | 0.6736 | 2.0889e-09| 0.9619 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 0.808181 | 0.811585  | 
| abacus_cosm121     | Baseline +0.025 w0                                                   | 0.02237 |  0.1200   | 0.6662 | 2.1211e-09| 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -0.975   | 0.0    | 0.808169 | 0.811571  | 
| abacus_cosm122     | Baseline -0.025 w0                                                   | 0.02237 |  0.1200   | 0.6810 | 2.0483e-09| 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.025   | 0.0    | 0.808170 | 0.811577  | 
| abacus_cosm123     | Baseline +0.1 wa, -0.025 w0                                          | 0.02237 |  0.1200   | 0.6729 | 2.0915e-09| 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.025   | 0.1    | 0.808176 | 0.811580  | 
| abacus_cosm124     | Baseline -0.1 wa, +0.025 w0                                          | 0.02237 |  0.1200   | 0.6742 | 2.0778e-09| 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -0.975   | -0.1   | 0.808175 | 0.811580  | 
| abacus_cosm125     | Baseline +0.5% sigma8                                                | 0.02237 |  0.1200   | 0.6736 | 2.1039e-9 | 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 0.811995 | 0.815415  | 
| abacus_cosm126     | Baseline -0.5% sigma8                                                | 0.02237 |  0.1200   | 0.6736 | 2.0622e-9 | 0.9649 | 0.0     | 2.0328 | 1      | 0.00064420 | -1.0   | 0.0    | 0.803908 | 0.807294  | 
| abacus_cosm130     | Emulator grid around baseline cosmology                              | 0.02237 |  0.1200   | 0.6736 | 1.6140e-09| 0.9649 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.000 | 0.000  | 0.711201 | 0.714197  | 
| abacus_cosm131     | Emulator grid around baseline cosmology                              | 0.02237 |  0.1086   | 0.7165 | 2.3146e-09| 0.9649 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.000 | 0.000  | 0.807866 | 0.811587  | 
| abacus_cosm132     | Emulator grid around baseline cosmology                              | 0.02237 |  0.1200   | 0.6736 | 2.1791e-09| 0.9049 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.000 | 0.000  | 0.808189 | 0.811584  | 
| abacus_cosm133     | Emulator grid around baseline cosmology                              | 0.02237 |  0.1200   | 0.6736 | 2.6144e-09| 0.9649 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.000 | 0.000  | 0.905163 | 0.908976  | 
| abacus_cosm134     | Emulator grid around baseline cosmology                              | 0.02237 |  0.1326   | 0.6319 | 1.9066e-09| 0.9649 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.000 | 0.000  | 0.808458 | 0.811566  | 
| abacus_cosm135     | Emulator grid around baseline cosmology                              | 0.02237 |  0.1200   | 0.6736 | 1.9904e-09| 1.0249 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.000 | 0.000  | 0.808160 | 0.811573  | 
| abacus_cosm136     | Emulator grid around baseline cosmology                              | 0.02073 |  0.1192   | 0.6618 | 2.5239e-09| 0.9303 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.000 | 0.000  | 0.882475 | 0.886249  | 
| abacus_cosm137     | Emulator grid around baseline cosmology                              | 0.02212 |  0.1271   | 0.6472 | 1.6540e-09| 0.9252 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.000 | 0.000  | 0.729693 | 0.732609  | 
| abacus_cosm138     | Emulator grid around baseline cosmology                              | 0.02108 |  0.1138   | 0.6847 | 2.2282e-09| 0.9723 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.000 | 0.000  | 0.821432 | 0.825095  | 
| abacus_cosm139     | Emulator grid around baseline cosmology                              | 0.02416 |  0.1128   | 0.7164 | 2.1681e-09| 0.9732 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.000 | 0.000  | 0.793003 | 0.796493  | 
| abacus_cosm140     | Emulator grid around baseline cosmology                              | 0.02096 |  0.1221   | 0.6536 | 1.8126e-09| 0.9893 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.000 | 0.000  | 0.772033 | 0.775267  | 
| abacus_cosm141     | Emulator grid around baseline cosmology                              | 0.02381 |  0.1272   | 0.6623 | 1.9945e-09| 0.9384 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.000 | 0.000  | 0.799575 | 0.802737  | 
| abacus_cosm142     | Emulator grid around baseline cosmology                              | 0.02287 |  0.1130   | 0.7038 | 1.6701e-09| 0.9927 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.000 | 0.000  | 0.707082 | 0.710219  | 
| abacus_cosm143     | Emulator grid around baseline cosmology                              | 0.02206 |  0.1278   | 0.6443 | 2.1084e-09| 0.9952 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.000 | 0.000  | 0.847522 | 0.850903  | 
| abacus_cosm144     | Emulator grid around baseline cosmology                              | 0.02210 |  0.1130   | 0.6968 | 2.7653e-09| 0.9279 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.000 | 0.000  | 0.891360 | 0.895324  | 
| abacus_cosm145     | Emulator grid around baseline cosmology                              | 0.02428 |  0.1186   | 0.6961 | 2.1634e-09| 0.9347 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.000 | 0.000  | 0.801404 | 0.804769  | 
| abacus_cosm146     | Emulator grid around baseline cosmology                              | 0.02097 |  0.1180   | 0.6682 | 1.9020e-09| 0.9351 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.000 | 0.000  | 0.762696 | 0.765984  |
| abacus_cosm147     | Emulator grid around baseline cosmology                              | 0.02113 |  0.1215   | 0.6498 | 1.9081e-09| 0.9587 | 0.000  | 2.0328 | 1      | 0.00064420 | -0.809 | -0.628  | 0.777157 | 0.780416  | 
| abacus_cosm148     | Emulator grid around baseline cosmology                              | 0.02289 |  0.1201   | 0.6199 | 1.9629e-09| 0.9380 | 0.000  | 2.0328 | 1      | 0.00064420 | -0.925 | 0.393  | 0.714913 | 0.717888  | 
| abacus_cosm149     | Emulator grid around baseline cosmology                              | 0.02188 |  0.1200   | 0.6688 | 2.1521e-09| 0.9913 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.174 | 0.613  | 0.824854 | 0.828343  | 
| abacus_cosm150     | Emulator grid around baseline cosmology                              | 0.02248 |  0.1216   | 0.7224 | 2.5099e-09| 0.9355 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.090 | -0.373  | 0.937655 | 0.941570  | 
| abacus_cosm151     | Emulator grid around baseline cosmology                              | 0.02315 |  0.1254   | 0.6582 | 2.2686e-09| 0.9757 | 0.000  | 2.0328 | 1      | 0.00064420 | -0.826 | -0.615  | 0.860820 | 0.864288  | 
| abacus_cosm152     | Emulator grid around baseline cosmology                              | 0.02165 |  0.1148   | 0.6204 | 1.7965e-09| 0.9541 | 0.000  | 2.0328 | 1      | 0.00064420 | -0.732 | -0.187  | 0.677885 | 0.680849  | 
| abacus_cosm153     | Emulator grid around baseline cosmology                              | 0.02192 |  0.1199   | 0.6092 | 2.2946e-09| 0.9917 | 0.000  | 2.0328 | 1      | 0.00064420 | -0.735 | -0.172  | 0.794389 | 0.797729  | 
| abacus_cosm154     | Emulator grid around baseline cosmology                              | 0.02158 |  0.1148   | 0.7426 | 2.0689e-09| 0.9538 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.076 | -0.395  | 0.838698 | 0.842413  | 
| abacus_cosm155     | Emulator grid around baseline cosmology                              | 0.02369 |  0.1184   | 0.6247 | 2.0723e-09| 0.9713 | 0.000  | 2.0328 | 1      | 0.00064420 | -0.727 | -0.184  | 0.735302 | 0.738388  | 
| abacus_cosm156     | Emulator grid around baseline cosmology                              | 0.02202 |  0.1261   | 0.6499 | 1.9738e-09| 0.9678 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.176 | 0.621  | 0.801974 | 0.805210  | 
| abacus_cosm157     | Emulator grid around baseline cosmology                              | 0.02247 |  0.1214   | 0.6668 | 2.5108e-09| 0.9356 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.167 | 0.616  | 0.872315 | 0.875941  | 
| abacus_cosm158     | Emulator grid around baseline cosmology                              | 0.02201 |  0.1262   | 0.6958 | 1.8626e-09| 0.9667 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.082 | -0.392  | 0.829816 | 0.833179  | 
| abacus_cosm159     | Emulator grid around baseline cosmology                              | 0.02206 |  0.1261   | 0.5967 | 1.7977e-09| 0.9673 | 0.000  | 2.0328 | 1      | 0.00064420 | -0.726 | -0.220  | 0.718521 | 0.721402  | 
| abacus_cosm160     | Emulator grid around baseline cosmology                              | 0.02223 |  0.1185   | 0.7456 | 2.0963e-09| 0.9942 | 0.000  | 2.0328 | 1      | 0.00064420 | -1.271 | 0.217  | 0.876756 | 0.880523  | 
| abacus_cosm161     | Emulator grid around baseline cosmology                              | 0.02282 |  0.1274   | 0.7330 | 1.9688e-09| 0.9649 | 0.026  | 2.7283 | 1      | 0.00064420 | -1.000 | 0.000  | 0.793066 | 0.796247  | 
| abacus_cosm162     | Emulator grid around baseline cosmology                              | 0.02136 |  0.1048   | 0.6383 | 2.1592e-09| 0.9297 | -0.026  | 1.3521 | 1      | 0.00064420 | -1.000 | 0.000  | 0.779589 | 0.783285  | 
| abacus_cosm163     | Emulator grid around baseline cosmology                              | 0.02135 |  0.1290   | 0.7280 | 2.1689e-09| 0.9922 | -0.018  | 2.8575 | 1      | 0.00064420 | -1.000 | 0.000  | 0.838824 | 0.842187  | 
| abacus_cosm164     | Emulator grid around baseline cosmology                              | 0.02173 |  0.1091   | 0.6042 | 2.0003e-09| 0.9211 | 0.016  | 1.1769 | 1      | 0.00064420 | -1.000 | 0.000  | 0.774159 | 0.777681  | 
| abacus_cosm165     | Emulator grid around baseline cosmology                              | 0.02225 |  0.1278   | 0.7293 | 2.0676e-09| 1.0241 | 0.026  | 2.7558 | 1      | 0.00064420 | -1.000 | 0.000  | 0.835954 | 0.839319  | 
| abacus_cosm166     | Emulator grid around baseline cosmology                              | 0.02306 |  0.1151   | 0.6826 | 2.2779e-09| 0.9691 | 0.038  | 1.9089 | 1      | 0.00064420 | -1.000 | 0.000  | 0.837463 | 0.841106  | 
| abacus_cosm167     | Emulator grid around baseline cosmology                              | 0.02248 |  0.1400   | 0.7050 | 1.7321e-09| 0.9715 | -0.017  | 2.8889 | 1      | 0.00064420 | -1.000 | 0.000  | 0.768419 | 0.771255  | 
| abacus_cosm168     | Emulator grid around baseline cosmology                              | 0.02157 |  0.1084   | 0.6070 | 2.5378e-09| 0.9275 | 0.016  | 1.1911 | 1      | 0.00064420 | -1.000 | 0.000  | 0.871407 | 0.875401  | 
| abacus_cosm169     | Emulator grid around baseline cosmology                              | 0.02189 |  0.1222   | 0.6474 | 1.8067e-09| 0.9898 | 0.038  | 1.9109 | 1      | 0.00064420 | -1.000 | 0.000  | 0.777925 | 0.781158  | 
| abacus_cosm170     | Emulator grid around baseline cosmology                              | 0.02319 |  0.1076   | 0.6418 | 1.7994e-09| 0.9387 | -0.026  | 1.3411 | 1      | 0.00064420 | -1.000 | 0.000  | 0.716059 | 0.719332  | 
| abacus_cosm171     | Emulator grid around baseline cosmology                              | 0.02348 |  0.1272   | 0.6733 | 2.2585e-09| 0.9762 | -0.038  | 2.1543 | 1      | 0.00064420 | -1.000 | 0.000  | 0.852878 | 0.856267  | 
| abacus_cosm172     | Emulator grid around baseline cosmology                              | 0.02282 |  0.1032   | 0.6369 | 2.1259e-09| 0.9012 | 0.017  | 1.1954 | 1      | 0.00064420 | -1.000 | 0.000  | 0.765650 | 0.769278  | 
| abacus_cosm173     | Emulator grid around baseline cosmology                              | 0.02322 |  0.1161   | 0.6800 | 1.8904e-09| 0.9628 | 0.038  | 1.9049 | 1      | 0.00064420 | -1.000 | 0.000  | 0.763962 | 0.767255  | 
| abacus_cosm174     | Emulator grid around baseline cosmology                              | 0.02302 |  0.1064   | 0.6427 | 2.4889e-09| 0.9437 | -0.026  | 1.3242 | 1      | 0.00064420 | -1.000 | 0.000  | 0.840113 | 0.843996  | 
| abacus_cosm175     | Emulator grid around baseline cosmology                              | 0.02173 |  0.1336   | 0.6432 | 1.7429e-09| 0.9898 | -0.003  | 2.7456 | 1      | 0.00064420 | -0.911 | 0.350  | 0.708760 | 0.711484 | 
| abacus_cosm176     | Emulator grid around baseline cosmology                              | 0.02238 |  0.1199   | 0.6972 | 2.3120e-09| 0.9459 | 0.036  | 1.9043 | 1      | 0.00064420 | -1.222 | 0.339  | 0.892483 | 0.896318  | 
| abacus_cosm177     | Emulator grid around baseline cosmology                              | 0.02239 |  0.1344   | 0.6820 | 2.0641e-09| 1.0002 | 0.007  | 2.8643 | 1      | 0.00064420 | -0.757 | -0.443  | 0.806026 | 0.809110  | 
| abacus_cosm178     | Emulator grid around baseline cosmology                              | 0.02234 |  0.1204   | 0.6542 | 1.9665e-09| 0.9424 | 0.037  | 1.8987 | 1      | 0.00064420 | -0.874 | -0.455  | 0.791239 | 0.794555  | 
| abacus_cosm179     | Emulator grid around baseline cosmology                              | 0.02240 |  0.1067   | 0.5881 | 2.2365e-09| 0.9308 | -0.003  | 1.1884 | 1      | 0.00064420 | -0.755 | -0.435  | 0.775969 | 0.779541  | 
| abacus_cosm180     | Emulator grid around baseline cosmology                              | 0.02258 |  0.1209   | 0.7451 | 2.2790e-09| 0.9796 | -0.034  | 2.1722 | 1      | 0.00064420 | -1.108 | -0.274  | 0.894071 | 0.897833  | 
| abacus_cosm181     | Emulator grid around baseline cosmology                              | 0.02169 |  0.1112   | 0.5745 | 2.0651e-09| 0.9336 | -0.013  | 1.4059 | 1      | 0.00064420 | -0.910 | 0.350  | 0.730036 | 0.733292  | 
----

Further details about the cosmology choices:

Beyond the Planck2018 LCDM primary cosmology, we chose 4 other secondary cosmologies.
One was WMAP7, to have a large change in omega_m, H0, and sigma8.
Others were one wCDM, one high Neff, and one low S8.

wCDM: Chose w0=-0.7, wa=-0.5 to be an extreme thawing model.

Neff=3.70 cosmology: Took the chains from base_nnu_plikHM_TT_lowl_lowE_Riess18_post_BAO and averaged those in 3.595 < nnu < 3.90, chosen so that the weighted mean was 3.70.  Also standardized As to tau=0.0544.

Low sigma8: Opted to drop the amplitude by about 7.7%, to make sigma8(matter)=0.75.  This is a sizeable shift, but there's lots of ways to damp power.

Then we are doing a large grid of cosmologies to provide control of first and second
derivatives around the primary LCDM model.

For the grid of positive/negative excursions for linear derivatives around the baseline LCDM, we opted for the simplicity of 
rectalinear derivatives in ln(omega_b), ln(omega_c), ns, nrun, sigma8_m, w0.  Note that we treat sigma8_m, not As, as the independent variable,
in the expectation that this will keep large-scale structure closer to constant.  
For wa, we opt to hold w(z=0.333)=w0+0.25\*wa fixed, close to the mirage model.  
For Neff, the Planck chains suggested substantial degeneracies with omegac and ns, so we opt to move these two along
with Neff to stay close to the CMB degeneracy direction.

We added one extra simulation to be the paired opposite to the low-sigma8 secondary cosmology.

For the broader emulator set, we construct the unstructured grid as follows:  We place points on the surface 
of an 8-dimensional unit sphere,
denoting these v0..v7, then map them into the 8-dimensional parameter space by:

* sigma8cb = 0.811355 (1 + 0.12 v0 - 0.125 v4 + 0.06 u0), where u0 is another random number, uniform in [-1,1].

* omega_c = 0.1200 exp(0.100 v1 + 0.165 v6)

* ns = 0.9649 + 0.06 v2 + 0.05 v6

* omegab = 0.02237 exp(0.10 v3)

* w0 = -1.0 + 0.3 v4 -0.2 v5

* wa = 0.8 v5

* Nur = 2.0328 + 1.2 v6

* alpha_s = 0.05 v7

These parameter ranges were chosen to be relatively large (5-8 sigma) beyond today's CMB+LSS constraints, 
but it is important to note that most of an 8-d sphere is not close to the extreme in any one parameter, 
but rather 1/sqrt(8) of that extreme.

We have continued to have omega_c and ns vary with Nur, and w0 to vary with wa (so that variations in wa 
hold w(z=0.333) constant).  In addition, we opted to have sigma8 vary with w(0.333), not as much as a pure
wCDM fit to the CMB would imply, but to partially track that behavior.

Finally, we add extra +-6% scatter to sigma8.  Note that if we were holding the amplitude of the CMB anisotropies
fixed (and fixed tau), then our parameter variations would vary sigma8 quite a lot.  But we have not varied tau
or neutrino mass, so we want to allow some scatter in sigma8.

Next, we have to specify the distribution of points on the 8-d unit sphere.  We want to keep the points well 
separated, but also impose some constraints.  We seek to have some of the points sit in subspaces, so that
one doesn't have to be using the entire 8-dimensional space in all fits.  And we want to avoid most antipodal 
points, as these provide only redundant information about second derivatives (since we already have the linear
derivative set).  We also want to mildly exceed the number of simulations needed to constrain the second
derivatives, so that there is some ability to drop simulations for cross-validation.

We use 49 antipodal pairs of points on the sphere.  These are subject to the constraints below,
but otherwise are evolved from their random start to an electrostatic glass, resulting in a well
dispersed set of points.  The constraints:

a) The first 3 pairs are forced to be at the unit vectors in the v0, v1, and v2 directions, which
will map to individual extremal excursions in sigma8cb, omega_c, and ns.  We retain both points
of each pair in the grid, as these are particularly important directions.  In all cases below,
we keep only the first point of each pair.

b) The next 11 pairs sample only the v0..v3 directions and are constrained to have v4..v7 = 0, 
so that they will only sample sigma8cb, omega_c, ns, and omega_b.  
We note that the 4-dimensional space has 10 second derivatives, for which we're 
17 simulations (and 14 non-antipodal).

c) The next 14 pairs sample the v0..v5 directions, holding v6..v7 = 0.  These will add w0, wa
to the space.  This introduces 11 new second derivatives.

d) The next 14 pairs sample the v0..v3 + v6..7 directions, holding v4..v5 = 0.  These will add
Nur and alpha_s to the LCDM space.  Again, this introduces 11 new second derivatives.

e) The last 7 pairs sample the full space, and hence have excursions in w0, wa, Nur, and alpha_s.
This last subspace has 4 new second derivatives to measure.

The randomness of the starting point was subjected to some patterns on the sign of certain coordinates
in order to encourage a glass with better balance in 2-d projections.  This was judged simply by eye.

------

TODOs:

We need to define the re-blindable sample.

We plan to run fixed-amplitude sims, probably in 1 Gpc/h boxes, for the primary and secondary cosmologies.

Could run the cosmologies of the recent ANL big runs as abacus_cosm019..021.

We are considering doing one or more large scale-free runs.

We could add more emulator sims, e.g., to the interior of the sphere.

We would like to include a BDE model; needs mild code development.  

We'd like to include one or more runs with neutrinos treated in the LRA; needs substantial code development.

We'd like to consider an f_NL!=0 run; needs moderate code development.


