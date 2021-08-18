Data Access
===========

DESI Members
------------
DESI collaboration members can access the AbacusSummit data products on NERSC.
The path to the data products can be found on the DESI Wiki: https://desi.lbl.gov/trac/wiki/CosmoSimsWG/Abacus#AbacusSummit

Public
-------
We are pleased to be able to offer two online portals to access AbacusSummit data:

- the full 2 PB via OLCF's Constellation, tape-backed;
- a 750 TB subset via NERSC, disk-backed.

Constellation, as a tape-backed portal, is appropriate for bulk transfers between supercomputer centers. NERSC, as a disk-backed portal, and is appropriate for fetching narrow subsets of the data.

Full Data on Tape
~~~~~~~~~~~~~~~~~
Oak Ridge Leadership Computing Facility's `Constellation <https://www.olcf.ornl.gov/olcf-resources/rd-project/constellation-doi-framework-and-portal/>`_ portal hosts the full 2 PB AbacusSummit data set on the magnetic-tape-backed `High Performance Storage System (HPSS) <https://www.olcf.ornl.gov/olcf-resources/data-visualization-resources/hpss/>`_.  HPSS offers high throughput, but high access latency.  To ensure high performance, we aggregate the simulation files with coarse granularity, such that in most cases one must download an entire simulation's worth of halos, which is 6.1 TB for a ``base`` simulation.

The primary DOI of AbacusSummit is ``10.13139/OLCF/1811689``.  This is a persistent identifer to the access information at the following URL, from where the AbacusSummit data may be browsed and downloaded via Globus: https://doi.ccs.ornl.gov/ui/doi/355

.. note::
  Use the "Download" button at the top-right of https://doi.ccs.ornl.gov/ui/doi/355 to access the data

We are grateful to Ross Miller and the OLCF Constellation team for providing the opportunity to host this data and for their expert assistance during the creation of the DOI.

Subset of Data on Disk
~~~~~~~~~~~~~~~~~~~~~~
NERSC's `Community File System <https://docs.nersc.gov/filesystems/community/>`_ hosts a 750 TB subset of the most important AbacusSummit data products (includes most products except for the 7% "B" subsample).  We will shortly be able to provide a Globus portal to this data.


Using Globus
~~~~~~~~~~~~
Both the disk-backed and tape-backed portals use the Globus interface.  See here for instructions on using Globus: https://docs.globus.org/how-to/get-started/

Note that most university and large computing centers have Globus endpoints already configured that you can use.  But for transfers to other sites without a pre-configured endpoint, such as a personal computer, one can use `Globus Connect Personal <https://www.globus.org/globus-connect-personal>`_.

What data are available?
------------------------
The :doc:`data-products` page documents the data products.  

Note that you will almost certainly need to use the utilities at
https://abacusutils.readthedocs.io/
to unpack the outputs. 
