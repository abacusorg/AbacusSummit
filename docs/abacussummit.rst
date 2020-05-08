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
