.. AbacusSummit documentation master file, created by
   sphinx-quickstart on Wed Apr 29 14:38:47 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
  
AbacusSummit
============

AbacusSummit is a suite of large, high-accuracy cosmological N-body simulations.
These simulations were designed to meet (and exceed!) the Cosmological Simulation Requirements of
the `Dark Energy Spectroscopic Instrument (DESI) survey <https://www.desi.lbl.gov/>`_.  AbacusSummit
was run on the `Summit <https://www.olcf.ornl.gov/summit/>`_ supercomputer at the Oak Ridge Leadership
Computing Facility under a time allocation from the DOE's ALCC program.

AbacusSummit was run using the Abacus N-body code.  For more information about the code, see :doc:`abacus`.

The specifications of the 160+ simulations that comprise AbacusSumit are given on the :doc:`simulations` page.

The cosmologies used by these simulations are specified on the :doc:`cosmologies` page.

The available data products (halo catalogs, lightcones, etc) are given on the :doc:`data-products` page.

The abacusutils package can be used to work with AbacusSummit data: https://abacusutils.readthedocs.io.  Full examples coming soon!

This documentation and code is hosted in the `abacusorg/AbacusSummit <https://github.com/abacusorg/abacussummit>`_ GitHub repository.  Please file an issue there for questions about AbacusSummit!

.. toctree::
   :maxdepth: 2
   :caption: Overview

   abacus
   abacussummit
   citation

.. toctree::
   :maxdepth: 2
   :caption: Specifications

   simulations
   cosmologies
   nbody-details

.. toctree::
   :maxdepth: 2
   :caption: Products

   data-products
   compaso
   data-access
   disk-space

.. toctree::
   :maxdepth: 2
   :caption: Other Topics

   visualizations

.. toctree::
   :maxdepth: 2
   :caption: About

   authors



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
