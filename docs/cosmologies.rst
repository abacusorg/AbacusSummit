Cosmologies
===========

This page describes the specification of the Cosmologies and the CLASS
parameters that they define.  The CLASS parameter files and resulting
power spectra and transfer functions are available in the `AbacusSummit/Cosmologies <https://github.com/abacusorg/AbacusSummit/tree/master/Cosmologies>`_
directory.

We have given the cosmologies numbers, so that the simulations will refer to c123.

There are various sets of cosmologies in this list:

- The primary cosmology (c000) is a Planck2018 LCDM version, specifically the mean of base_plikHM_TTTEEE_lowl_lowE_lensing.
  This cosmology has 25 base boxes, plus other mass resolution options.  c009 is the same cosmology, but with massless neutrinos.
- There are 4 secondary cosmologies (c001-4), each with 6 base boxes.  There is a low-omega_c choice based on WMAP7,
  a wCDM choice, a high-Neff choice, and a low-sigma8 choice.
- There are about ten reference cosmologies (c010-c018) that match the choices employed in flagship runs from
  other groups, so ease comparisons between code bases.
- There is a linear derivative grid (c100-c116) that provides 8 matched pairs, with small positive and negative steps
  in an 8-dimensional parameter space, plus one additional simulation that is the high-sigma8 partner to the low-sigma8
  secondary cosmology.
- There is a larger unstructured emulator grid (c130-c181) that provides a wider coverage of this 8-dimensional space.

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

.. TODO: better way to link this CSV file?

Download the cosmologies table `here <https://github.com/abacusorg/AbacusSummit/blob/master/Cosmologies/cosmologies.csv>`_.
However, in analysis applications, users are encouraged to use the cosmological parameters stored as in the ``header`` field
of the ASDF data product files (which is loaded into the ``meta`` field of Astropy tables) rather than referencing the
cosmologies table.


.. note:: The following table is wide, you may have to scroll to the right to see all the columns.

.. csv-table::
    :file: ../Cosmologies/cosmologies.csv
    :header-rows: 1

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


