N-body Details
==============

Here we describe technical choices with respect to the N-body method
that affect the accuracy of the outputs (e.g. softening, time stepping, ICs).

All of the simulations start at *z* = 99 utilizing second-order Lagrangian
Perturbation Theory initial conditions following corrections of
first-order particle linear theory; these are described in Garrison
et al. (2016, see :doc:`citation`) and have a target correction redshift of 12.  The 
particles are displaced from a cubic grid.

The simulations use spline force softening, described in Garrison
et al. (2018).  Force softening for the standard boxes is 7.2 kpc/*h*
(Plummer equivalent), or 1/40th of the initial particle grid spacing.
This softening is fixed in proper (not comoving) distance
and capped at 0.3 of the interparticle spacing at early times.

We use global time steps that begin capped at :math:`\Delta(\ln a)=0.03` but
quickly drop, tied to a criteria on the ratio of the Mpc-scale
velocity dispersion to the Mpc-scale maximum acceleration, with 
the simulation obeying the most stringent case.  This is scaled
by a parameter eta, which is 0.25 in these simulations.  Simulations
require about 1100 time steps to reach *z* = 0.1.

Users of the outputs probably don't need to know much of the numerical
details of the code, but there is one numerical concept that enters
into the data products.  Abacus uses a cubic grid of size CPD\ :sup:`3`,
chosen to tune code speed.  For AbacusSummit, CPD is ususally 1701.
Processing proceeds in y-z slabs of cells, and particle outputs are
ordered into these cells and slabs.  Before being presented to users,
these outputs are aggregated into "superslabs" of 51 or 52 slabs.
