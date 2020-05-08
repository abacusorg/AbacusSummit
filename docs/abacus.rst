Abacus
=======

Here we briefly describe the Abacus N-body code.

What is Abacus?
---------------

Abacus is a high-accuracy, high-performance cosmological N-body simulation code.  It
is optimized for GPU architectures and for large volume, moderately
clustered simulations.  It is extremely fast: we clock over 30
million particle updates per second on commodity dual-Xeon, dual-GPU
computers and nearly 70 million particle updates per second on each
node of the Summit supercomputer.  But it is also extremely accurate:
typical force accuracy is below 1e-5 and we are using global
timesteps, so the leapfrog timesteps away from the cluster cores
are much smaller than the dynamical time.

Abacus has been described in several publications.  See :doc:`citation` for a list of these papers.

CompaSO, the Abacus on-the-fly halo finder, is described on the :doc:`compaso` page.
