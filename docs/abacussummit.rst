AbacusSummit 
============
What is AbacusSummit?
---------------------
AbacusSummit is a suite of large, high-accuracy cosmological N-body simulations.
These simulations were designed to meet (and exceed!) the Cosmological Simulation Requirements of
the `Dark Energy Spectroscopic Instrument (DESI) survey <https://www.desi.lbl.gov/>`_.  AbacusSummit
was run on the `Summit <https://www.olcf.ornl.gov/summit/>`_ supercomputer at the Oak Ridge Leadership
Computing Facility under a time allocation from the DOE's ALCC program.

Most of the simulations in AbacusSummit are 6912\ :sup:`3` = 330 billion 
particles in 2 Gpc/h volume, yielding a particle mass of about 2e9 Msun/h.  

AbacusSummit consists of ~150 of these simulations, totaling about 50 trillion
particles.  Detailed specifications of the :doc:`simulations` and :doc:`cosmologies`
are available on other pages.

25 simulations are in one LCDM cosmology (Planck2018),
6 simulations each in 4 other cosmologies, and then 1 simulation
in a spread of other cosmologies, suitable for emulator grids and
blind mock challenges.  We will also likely run some simulations
at 8x higher and 27x lower mass resolutions to support a wider range
of applications and numerical/systematic tests.

All of the simulations start at z=99 utilizing second-order Lagrangian
Perturbation Theory initial conditions following corrections of
first-order particle linear theory; these are described in Garrison
et al. (2016, see :ref:`papers`) and have a target correction redshift of 5.  The 
particles are displaced from a cubic grid.

The simulations use spline force softening, described in Garrison
et al. (2018).  Force softening for the standard boxes is 7.2 kpc/h
(Plummer equivalent), fixed in proper (not comoving) distance
and capped at 0.3 of the interparticle spacing at early times.

We use global time steps that begin capped at :math:`\Delta(\ln a)=0.03` but
quickly drop, tied to a criteria on the ratio of the Mpc-scale
velocity dispersion to the Mpc-scale maximum acceleration, with 
the simulation obeying the most stringent case.  This is scaled
by a parameter eta, which is 0.25 in these simulations.  Simulations
require about 1100 time steps to reach z=0.1.

Users of the outputs probably don't need to know much of the numerical
details of the code, but there is one numerical concept that enter
into the data products.  Abacus uses a cubic grid of size CPD\ :sup:`3`,
chosen to tune code speed.  For AbacusSummit, CPD is ususally 1701.
Processing proceeds in y-z slabs of cells, and particle outputs are
ordered into these cells and slabs.
