Disk Space
==========

For users interested in downloading AbacusSummit data, this breakdown of the file sizes
of the various data products may be helpful.

.. TODO: let's use MB/GB/TB instead of MB (and reformat this page)

The following is an annotated summary of ``du -BMB`` (so units of 1,000,000 bytes, as disk drives use).
This is for AbacusSummit_base_c000_ph008, which is typical, supplemented
by AbacusSummit_base_c000_ph001 for some information about the full time slices.

.. code-block:: sh

    # The total outputs are 7.85 TB per simulation, if there are no full time slices.
    7851475 AbacusSummit_base_c000_ph008

    # When there are full time slices, they are about 3.5 TB *each*, 
    # with a mild trend in redshift, due to slight changes in compression efficiency.
    # Sims have between 0 and 12 full time-slice epochs.
    3578826   slices/z0.200
    3534315   slices/z0.800
    3498498   slices/z1.400
    3472193   slices/z2.000
    3451782   slices/z2.500
    3431805   slices/z3.000

    # Here's the breakdown; most of the data is in the halos.
    # Most users won't need to look at the logs.
    1       [top-level directory]
    1      info
    5649    log
    1274121 lightcones
    6571688 halos

    # The lightcones contain 10% of the particles in rv+pid, and 100% in heal.
    # rv: particle pos/vel
    # pid: can be used to connect particles in the lightcone to halos in the timeslices;
    #      also contains the kernel density estimate from the fully sampled density field.
    # heal: The Nside=16384, ring=True healpix projection
    # These are broken into files for each time step, typically d(ln(1+z)) ~ 0.002.
    703830  lightcones/rv
    329456  lightcones/heal
    240836  lightcones/pid

    # The halos come in two flavors: 12 primary time slices with more outputs, 
    # and then 21 secondary time slices with only limited outputs. 
    # Most users will only want the primary slices; the secondary ones 
    # are intended for merger trees and for matching halos onto the light cones.
    #
    # The primary slices are bigger, typically 400 GB each:
    412661  halos/z0.100
    412863  halos/z0.200
    412748  halos/z0.300
    412340  halos/z0.400
    411654  halos/z0.500
    408158  halos/z0.800
    402861  halos/z1.100
    396109  halos/z1.400
    388176  halos/z1.700
    379538  halos/z2.000
    364212  halos/z2.500
    348863  halos/z3.000
    # Total of primary slices: 4750 GB

    # The secondary slices are smaller, typically 100 GB and decreasing at high z:
    111493  halos/z0.150
    110879  halos/z0.250
    110041  halos/z0.350
    109006  halos/z0.450
    107437  halos/z0.575
    106324  halos/z0.650
    105147  halos/z0.725
    102498  halos/z0.875
    101105  halos/z0.950
    99575   halos/z1.025
    96330   halos/z1.175
    94619   halos/z1.250
    92831   halos/z1.325
    89070   halos/z1.475
    87182   halos/z1.550
    85311   halos/z1.625
    79098   halos/z1.850
    67995   halos/z2.250
    53962   halos/z2.750
    11267   halos/z5.000
    351    halos/z8.000
    # Total of secondary slices: 1822 GB

    # But one might opt only to keep certain types of files on disk, so here is the summary
    # of the types.  

    # For example, a minimal installation might be only the halo_info and halo_rv_A files,
    # which are 1.1 TB, and perhaps only for some of the primary epochs.  E.g., five
    # epochs might knock the storage down to 0.5 TB per simulation.

    # Another example would be to install only the primary epochs, without the 
    # field B samples.  This saves 1.83 TB per sim, so one is at 6 TB/sim.

    # The halo info files contain the stats about all halos, typically 70-75 GB/epoch.
    # Note that the file format supports reading only subsets of columns; many users
    # will need to load only a small fraction of these.
    73188   halos/z0.100 halo_info
    74301   halos/z0.200 halo_info
    75190   halos/z0.300 halo_info
    75864   halos/z0.400 halo_info
    76323   halos/z0.500 halo_info
    76416   halos/z0.800 halo_info
    74722   halos/z1.100 halo_info
    71488   halos/z1.400 halo_info
    67014   halos/z1.700 halo_info
    61615   halos/z2.000 halo_info
    51419   halos/z2.500 halo_info
    40797   halos/z3.000 halo_info
    # Primary halo_info: 818 GB

    73764   halos/z0.150 halo_info
    74763   halos/z0.250 halo_info
    75550   halos/z0.350 halo_info
    76107   halos/z0.450 halo_info
    76508   halos/z0.575 halo_info
    76591   halos/z0.650 halo_info
    76548   halos/z0.725 halo_info
    76120   halos/z0.875 halo_info
    75755   halos/z0.950 halo_info
    75270   halos/z1.025 halo_info
    74008   halos/z1.175 halo_info
    73240   halos/z1.250 halo_info
    72376   halos/z1.325 halo_info
    70387   halos/z1.475 halo_info
    69312   halos/z1.550 halo_info
    68204   halos/z1.625 halo_info
    64279   halos/z1.850 halo_info
    56553   halos/z2.250 halo_info
    45891   halos/z2.750 halo_info
    10066   halos/z5.000 halo_info
    303    halos/z8.000 halo_info
    # Secondary halo_info: 1362 GB

    # The particles associated to these halos, with 3% consistent subsample 
    # in A and 7% in B, all indexed out of the halo_info files.
    # First, we have the positions and velocities.  
    # Users painting HOD satellite galaxies into the halos probably could just use the A set.
    31415   halos/z0.100 halo_rv_A
    30859   halos/z0.200 halo_rv_A
    30213   halos/z0.300 halo_rv_A
    29498   halos/z0.400 halo_rv_A
    28733   halos/z0.500 halo_rv_A
    26264   halos/z0.800 halo_rv_A
    23699   halos/z1.100 halo_rv_A
    21216   halos/z1.400 halo_rv_A
    18767   halos/z1.700 halo_rv_A
    16457   halos/z2.000 halo_rv_A
    12965   halos/z2.500 halo_rv_A
    9965    halos/z3.000 halo_rv_A
    # Primary 3% halo rv: 280 GB

    70448   halos/z0.100 halo_rv_B
    69199   halos/z0.200 halo_rv_B
    67735   halos/z0.300 halo_rv_B
    66123   halos/z0.400 halo_rv_B
    64399   halos/z0.500 halo_rv_B
    58825   halos/z0.800 halo_rv_B
    53036   halos/z1.100 halo_rv_B
    47321   halos/z1.400 halo_rv_B
    41824   halos/z1.700 halo_rv_B
    36626   halos/z2.000 halo_rv_B
    28821   halos/z2.500 halo_rv_B
    22132   halos/z3.000 halo_rv_B
    # Primary 7% halo rv: 626 GB

    # And then we have the PIDs, with kernel densities embedded.
    # These are used build merger trees, but could also be used
    # to track particular particles as part of galaxy assignment,
    # e.g., to find the densest particle in a progenitor halo and
    # use its late-time position.
    13680   halos/z0.100 halo_pid_A
    13325   halos/z0.200 halo_pid_A
    12947   halos/z0.300 halo_pid_A
    12548   halos/z0.400 halo_pid_A
    12140   halos/z0.500 halo_pid_A
    10870   halos/z0.800 halo_pid_A
    9652    halos/z1.100 halo_pid_A
    8493    halos/z1.400 halo_pid_A
    7421    halos/z1.700 halo_pid_A
    6442    halos/z2.000 halo_pid_A
    4989    halos/z2.500 halo_pid_A
    3777    halos/z3.000 halo_pid_A
    # Primary 3% halo pid: 116 GB

    30217   halos/z0.100 halo_pid_B
    29390   halos/z0.200 halo_pid_B
    28501   halos/z0.300 halo_pid_B
    27584   halos/z0.400 halo_pid_B
    26637   halos/z0.500 halo_pid_B
    23780   halos/z0.800 halo_pid_B
    21020   halos/z1.100 halo_pid_B
    18439   halos/z1.400 halo_pid_B
    16061   halos/z1.700 halo_pid_B
    13899   halos/z2.000 halo_pid_B
    10731   halos/z2.500 halo_pid_B
    8097    halos/z3.000 halo_pid_B
    # Primary 7% halo pid: 254 GB

    # For the secondary epochs, we provide only the PID+density file.
    # These are slightly smaller because they include only L1 particles, not L0 particles.
    11726   halos/z0.150 halo_pid_A
    11238   halos/z0.250 halo_pid_A
    10743   halos/z0.350 halo_pid_A
    10256   halos/z0.450 halo_pid_A
    9655    halos/z0.575 halo_pid_A
    9292    halos/z0.650 halo_pid_A
    8940    halos/z0.725 halo_pid_A
    8258    halos/z0.875 halo_pid_A
    7941    halos/z0.950 halo_pid_A
    7620    halos/z1.025 halo_pid_A
    7007    halos/z1.175 halo_pid_A
    6716    halos/z1.250 halo_pid_A
    6429    halos/z1.325 halo_pid_A
    5883    halos/z1.475 halo_pid_A
    5628    halos/z1.550 halo_pid_A
    5389    halos/z1.625 halo_pid_A
    4680    halos/z1.850 halo_pid_A
    3621    halos/z2.250 halo_pid_A
    2563    halos/z2.750 halo_pid_A
    395    halos/z5.000 halo_pid_A
    16     halos/z8.000 halo_pid_A
    # Secondary 3% halo pid: 144 GB

    26003   halos/z0.150 halo_pid_B
    24879   halos/z0.250 halo_pid_B
    23749   halos/z0.350 halo_pid_B
    22643   halos/z0.450 halo_pid_B
    21274   halos/z0.575 halo_pid_B
    20442   halos/z0.650 halo_pid_B
    19659   halos/z0.725 halo_pid_B
    18120   halos/z0.875 halo_pid_B
    17410   halos/z0.950 halo_pid_B
    16685   halos/z1.025 halo_pid_B
    15316   halos/z1.175 halo_pid_B
    14664   halos/z1.250 halo_pid_B
    14026   halos/z1.325 halo_pid_B
    12802   halos/z1.475 halo_pid_B
    12243   halos/z1.550 halo_pid_B
    11719   halos/z1.625 halo_pid_B
    10139   halos/z1.850 halo_pid_B
    7822    halos/z2.250 halo_pid_B
    5509    halos/z2.750 halo_pid_B
    806    halos/z5.000 halo_pid_B
    34     halos/z8.000 halo_pid_B
    # Secondary 7% halo pid: 316 GB

    # We provide the rest of the density field, i.e., the complement of the halo set,
    # in the subsamples.  These would be used in matter-field statistics or if one wanted
    # to associate particles in the periphery of halos.  Or if one wanted to run a different
    # group finder (admittedly on only 10% of the dynamical particles).
    43432   halos/z0.100 field_rv_A
    44044   halos/z0.200 field_rv_A
    44724   halos/z0.300 field_rv_A
    45445   halos/z0.400 field_rv_A
    46195   halos/z0.500 field_rv_A
    48542   halos/z0.800 field_rv_A
    50898   halos/z1.100 field_rv_A
    53164   halos/z1.400 field_rv_A
    55295   halos/z1.700 field_rv_A
    57277   halos/z2.000 field_rv_A
    60189   halos/z2.500 field_rv_A
    62610   halos/z3.000 field_rv_A
    # Primary 3% field rv: 612 GB

    97497   halos/z0.100 field_rv_B
    98866   halos/z0.200 field_rv_B
    100381  halos/z0.300 field_rv_B
    101991  halos/z0.400 field_rv_B
    103666  halos/z0.500 field_rv_B
    108916  halos/z0.800 field_rv_B
    114209  halos/z1.100 field_rv_B
    119330  halos/z1.400 field_rv_B
    124160  halos/z1.700 field_rv_B
    128634  halos/z2.000 field_rv_B
    135233  halos/z2.500 field_rv_B
    140699  halos/z3.000 field_rv_B
    # Primary 7% field rv: 1374 GB

    # Field PIDs are probably not used much, but these do relate particles across epochs
    # and the PID encodes the initial grid location for Lagrangian displacements.
    16508   halos/z0.100 field_pid_A
    16556   halos/z0.200 field_pid_A
    16627   halos/z0.300 field_pid_A
    16709   halos/z0.400 field_pid_A
    16800   halos/z0.500 field_pid_A
    17124   halos/z0.800 field_pid_A
    17468   halos/z1.100 field_pid_A
    17809   halos/z1.400 field_pid_A
    18128   halos/z1.700 field_pid_A
    18443   halos/z2.000 field_pid_A
    18833   halos/z2.500 field_pid_A
    19093   halos/z3.000 field_pid_A
    # Primary 3% field pid: 210 GB

    36280   halos/z0.100 field_pid_B
    36327   halos/z0.200 field_pid_B
    36434   halos/z0.300 field_pid_B
    36582   halos/z0.400 field_pid_B
    36765   halos/z0.500 field_pid_B
    37426   halos/z0.800 field_pid_B
    38160   halos/z1.100 field_pid_B
    38855   halos/z1.400 field_pid_B
    39510   halos/z1.700 field_pid_B
    40150   halos/z2.000 field_pid_B
    41037   halos/z2.500 field_pid_B
    41698   halos/z3.000 field_pid_B
    # Primary 7% field pid: 459 GB

    # For the full time slices, they are split into L0 and field (non-L0) sets.
    # However, this was just due to convenience in the code; the L0 particles
    # are not indexed in halo_info.  Only concatenations will be useful.
    # The fractional split of L0 to field increases to low redshift.
    #
    # The position+velocity data is in the pack9 format, which gives 
    # somewhat higher precision than RVint.  These files average about
    # 2.8 TB per epoch, which is 8.5 bytes per particle.
    1682068   slices/z0.200/field_pack9
    1083440   slices/z0.200/L0_pack9

    1864771   slices/z0.800/field_pack9
    925909    slices/z0.800/L0_pack9

    2061023   slices/z1.400/field_pack9
    748046    slices/z1.400/L0_pack9

    2242314   slices/z2.000/field_pack9
    581440    slices/z2.000/L0_pack9

    2371831   slices/z2.500/field_pack9
    458272    slices/z2.500/L0_pack9

    2480799   slices/z3.000/field_pack9
    352132    slices/z3.000/L0_pack9

    # The PID and kernel density estimate are in the pid files.
    # These average about 0.7 TB per epoch, increasing toward low redshift.
    510862    slices/z3.000/field_pack9_pid
    88014     slices/z3.000/L0_pack9_pid

    501868    slices/z2.500/field_pack9_pid
    119812    slices/z2.500/L0_pack9_pid

    489859    slices/z2.000/field_pack9_pid
    158581    slices/z2.000/L0_pack9_pid

    472529    slices/z1.400/field_pack9_pid
    216902    slices/z1.400/L0_pack9_pid

    454954    slices/z0.800/field_pack9_pid
    288682    slices/z0.800/L0_pack9_pid

    444629    slices/z0.200/field_pack9_pid
    368691    slices/z0.200/L0_pack9_pid
