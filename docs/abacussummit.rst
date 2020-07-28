AbacusSummit 
============
What is AbacusSummit?
---------------------
AbacusSummit is a suite of large, high-accuracy cosmological N-body simulations.
These simulations were designed to meet (and exceed!) the Cosmological Simulation Requirements of
the `Dark Energy Spectroscopic Instrument (DESI) survey <https://www.desi.lbl.gov/>`_.  AbacusSummit
was run on the `Summit <https://www.olcf.ornl.gov/summit/>`_ supercomputer at the Oak Ridge Leadership
Computing Facility under a time allocation from the Department of Energy's ALCC program.

Most of the simulations in AbacusSummit are 6912\ :sup:`3` = 330 billion 
particles in 2 Gpc/*h* volume, yielding a particle mass of about :math:`2\times 10^9\ \mathrm{M}_\odot/h`.

AbacusSummit consists of over 140 of these simulations, plus other larger and smaller simulations,
totaling about 60 trillion
particles.  Detailed specifications of the :doc:`simulations` and :doc:`cosmologies`
are available on other pages.

Key portions of the suite are:

* A primary Planck2018 LCDM cosmology with 25 base simulations (330 billion particles in 2 Gpc/*h*).

* Four secondary cosmologies with 6 base simulations, phase matched to the first 6 of the primary boxes.

* A grid of 79 other cosmologies, each with 1 phase-matched base simulation, to support interpolation in an 8-dimensional parameter space, including :math:`w_0`, :math:`w_a`, :math:`N_\mathrm{eff}`, and running of the spectral index.

* A suite of 1800 small boxes at the base mass resolution to support covariance estimation

* Other base simulations to match the cosmology of external flagship simulations and to explore the effects of our neutrino approximation.

* A 6x higher mass resolution simulation of the primary cosmology to allow study of group finding, and a large-volume 27x lower mass resolution simulation of the primary cosmology to provide full-sky light cone to *z*>2.

* Specialty simulations including those with fixed-amplitude white noise and scale-free simulations.

* Extensive data products including particle subsamples, halo catalogs, merger trees, kernel density estimates, and light cones.
