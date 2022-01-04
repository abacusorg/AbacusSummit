Data Access
===========

.. note::
  The primary web portal to the data is https://abacusnbody.org. More details follow below.

All NERSC Users (including DESI Members)
----------------------------------------
All NERSC users, including DESI collaboration members, can access AbacusSummit data products at the following public path on NERSC:

``/global/project/projectdirs/desi/public/cosmosim/AbacusSummit``

Note that despite ``desi`` being in the path, this is a public directory that anyone at NERSC can access. Users who want to work on the data at NERSC should access the data at this path, rather than making a copy or downloading the data via the web portal.

**Addtional information for DESI members**: more advice on getting set up to use AbacusSummit in a DESI NERSC software environment is given here: https://desi.lbl.gov/trac/wiki/CosmoSimsWG/Abacus#AbacusSummit

Public
-------
We are pleased to be able to offer two online portals to access AbacusSummit data:

- the full 2 PB via OLCF's Constellation, tape-backed;
- a 750 TB subset via NERSC, disk-backed.

Constellation, as a tape-backed portal, is appropriate for bulk transfers between supercomputer centers. NERSC, as a disk-backed portal, and is appropriate for fetching narrow subsets of the data.  The Constellation portal also contains the HighZ and ScaleFree simulations.

OLCF Constellation: Full Data on Tape
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Oak Ridge Leadership Computing Facility's `Constellation <https://www.olcf.ornl.gov/olcf-resources/rd-project/constellation-doi-framework-and-portal/>`_ portal hosts the full 2 PB AbacusSummit data set on the magnetic-tape-backed `High Performance Storage System (HPSS) <https://www.olcf.ornl.gov/olcf-resources/data-visualization-resources/hpss/>`_.  HPSS offers high throughput, but high access latency.  To amortize the latency, we aggregate the simulation files with coarse granularity, such that in most cases one must download many TB of data. For example, the halo catalogs for each simulation are in a single tarball (per simulation), which is 6.6 TB for a ``base`` simulation.

There are three DOIs describing various AbacusSummit data products. They are all hosted on Constellation and are listed here:

First Release of Data Products
  The first DOI of AbacusSummit is ``10.13139/OLCF/1811689``.  This is the primary 2 PB dataset containing all data products as they came "off the machine" (notably, no cleaning): halo catalogs, particle subsamples, etc.  The DOI itself is a persistent identifer to the following URL, from where the AbacusSummit data may be browsed and downloaded via Globus: https://doi.ccs.ornl.gov/ui/doi/355.
  
Cleaned Halo Catalogs
  The next DOI is ``10.13139/OLCF/1828535``. This contains *cleaned halo catalogs* and particle subsamples.  Additionally, the halo catalogs are aggregated by redshift and simulation type (e.g. ``z0.100_base.tar`` contains all ``base`` simulations at redshift 0.1). Note that even though the cleaning information comes as a set of auxiliary files that annotate the primary catalogs, both the primary and auxiliary files are included in this DOI, thus forming a self-contained dataset. Many users will want to use AbacusSummit through this DOI.  The URL is https://doi.ccs.ornl.gov/ui/doi/363.
  
Halo Light Cone Catalogs
  The DOI of the halo light cone catalogs is ``10.13139/OLCF/1825069``, which directs to https://doi.ccs.ornl.gov/ui/doi/362.

.. note::
  Use the "Download" button at the top-right of ``doi.ccs.ornl.gov`` URLs to access the data on Globus
  
Note that it can take many hours before a transfer from Constellation begins if the tape drive is busy. Once it starts, though, the typical bandwidth is several GB/s.

The availability of Constellation depends on the status of HPSS, which undergoes regular downtime for maintenance. If the data is inaccessible, please check the status of HPSS on the following page: https://www.olcf.ornl.gov/for-users/center-status/

NERSC: Subset of Data on Disk
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
NERSC's `Community File System <https://docs.nersc.gov/filesystems/community/>`_ (CFS) hosts a 750 TB subset of the most important AbacusSummit data products (includes most products except for the 7% "B" particle subsample and the 100% time slice outputs).  The portal to this data is here: https://abacusnbody.org/

Using that portal, you can select the desired subset of simulations, data products, and redshifts, and initiate the transfer via Globus.  See :ref:`data-access:using globus`.

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

The NERSC hosting was made possible with the support of Stephen Bailey, Benjamin Weaver, Eli Dart, Debbie Bard, and Lisa Gerhardt, who we thank warmly.

For additional acknowledgements related to the creation of the suite proper, please see :ref:`authors:acknowledgements & thanks`.
