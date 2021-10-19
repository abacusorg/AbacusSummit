Data Access
===========

DESI Members & Other NERSC Users
--------------------------------
NERSC users, including DESI collaboration members, can access AbacusSummit data products at the following public path on NERSC:

``/global/project/projectdirs/desi/public/cosmosim/AbacusSummit``

**For DESI members**: more advice on getting set up to use AbacusSummit in a DESI NERSC software environment is given here: https://desi.lbl.gov/trac/wiki/CosmoSimsWG/Abacus#AbacusSummit

Public
-------
We are pleased to be able to offer two online portals to access AbacusSummit data:

- the full 2 PB via OLCF's Constellation, tape-backed;
- a 750 TB subset via NERSC, disk-backed.

Constellation, as a tape-backed portal, is appropriate for bulk transfers between supercomputer centers. NERSC, as a disk-backed portal, and is appropriate for fetching narrow subsets of the data.  The Constellation portal also contains the HighZ and ScaleFree simulations.

OLCF Constellation: Full Data on Tape
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Oak Ridge Leadership Computing Facility's `Constellation <https://www.olcf.ornl.gov/olcf-resources/rd-project/constellation-doi-framework-and-portal/>`_ portal hosts the full 2 PB AbacusSummit data set on the magnetic-tape-backed `High Performance Storage System (HPSS) <https://www.olcf.ornl.gov/olcf-resources/data-visualization-resources/hpss/>`_.  HPSS offers high throughput, but high access latency.  To amortize the latency, we aggregate the simulation files with coarse granularity, such that in most cases one must download many TB of data. For example, the halo catalogs for each simulation are in a single tarball (per simulation), which is 6.6 TB for a ``base`` simulation.

The primary DOI of AbacusSummit is ``10.13139/OLCF/1811689``.  This is a persistent identifer to the access information at the following URL, from where the AbacusSummit data may be browsed and downloaded via Globus: https://doi.ccs.ornl.gov/ui/doi/355

.. note::
  Use the "Download" button at the top-right of https://doi.ccs.ornl.gov/ui/doi/355 to access the data
  
Note that it can take many hours before a transfer from Constellation begins if the tape drive is busy. Once it starts, though, the typical bandwidth is several GB/s.

The availability of Constellation depends on the status of HPSS, which undergoes regular downtime for maintenance. If the data is inaccessible, please check the status of HPSS on the following page: https://www.olcf.ornl.gov/for-users/center-status/

NERSC: Subset of Data on Disk
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
NERSC's `Community File System <https://docs.nersc.gov/filesystems/community/>`_ (CFS) hosts a 750 TB subset of the most important AbacusSummit data products (includes most products except for the 7% "B" particle subsample and the 100% time slice outputs).  The portal to this data is here: https://abacussummit-portal.nersc.gov/

Using that portal, you can select the desired subset of simulations, data products, and redshifts, and initiate the transfer via Globus.  See :ref:`Using Globus`.

Some data products (initial conditions, merger trees) are not yet exposed via the web interface of this portal, but they can still be manually accessed by browsing the directory tree via Globus.

The availability of the NERSC portal depends on the availability of CFS and the DTNs (data transfer nodes). If the data is inaccessible, please check the CFS and DTN status on the following page: https://www.nersc.gov/live-status/motd/

Using Globus
~~~~~~~~~~~~
Both the disk-backed and tape-backed portals use the Globus interface.  See here for instructions on using Globus: https://docs.globus.org/how-to/get-started/

Note that most university and large computing centers have Globus endpoints already configured.  But for transfers to other sites without pre-configured endpoints, such as a personal computer, one can use `Globus Connect Personal <https://www.globus.org/globus-connect-personal>`_.

What data are available?
------------------------
The :doc:`data-products` page documents the data products.  All products are available at the Constellation portal (including ScaleFree and HighZ), and most products except for the 7% "B" particle subsample and the 100% time slice outputs are available at the NERSC portal.

Some data products (initial conditions, merger trees) are not yet exposed via the web interface of the NERSC portal, but they can still be manually accessed by browsing the directory tree via Globus.

Note that you will almost certainly need to use the utilities at
https://abacusutils.readthedocs.io/
to unpack the outputs. 

Acknowledgements
----------------
At OLCF, we are grateful to Ross Miller and the Constellation team for providing the opportunity to host this data and for their expert assistance during the creation of the DOI.

The NERSC hosting was made possible with the spport of Stephen Bailey, Benjamin Weaver, Eli Dart, Debbie Bard, and Lisa Gerhardt, who we thank warmly.

For additional acknowledgements related to the creation of the suite proper, please see :ref:`authors:acknowledgements-thanks`.
