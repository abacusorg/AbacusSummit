.. highlight:: none

Data Access
===========

.. note::
  The public web portal to the data is https://abacusnbody.org. NERSC users should instead use the :ref:`CFS directory<data-access:CFS Directory on NERSC>` below. Both expose the same data.

.. tip::
  A new :ref:`BinderHub<data-access:Flatiron Institute BinderHub> access option has recently been added (July 2024).

All NERSC Users (including DESI Members)
----------------------------------------

CFS Directory on NERSC
~~~~~~~~~~~~~~~~~~~~~~
All NERSC users, including DESI collaboration members, can access AbacusSummit data products at the following public path on NERSC::

  /global/cfs/cdirs/desi/public/cosmosim/AbacusSummit

Note that despite ``desi`` being in the path, this is a public directory that anyone at NERSC can access. Users who want to work on the data at NERSC should access the data at this path, rather than making a copy or downloading the data via the web portal.

**Addtional information for DESI members**: more advice on getting set up to use AbacusSummit in a DESI NERSC software environment is given here: https://desi.lbl.gov/trac/wiki/CosmoSimsWG/Abacus#AbacusSummit

Some data products were removed from disk to save space. They are listed in :ref:`data-access:NERSC: Subset of Data on Disk`. NERSC users can retrieve any such products from tape as described :ref:`here<data-access:Accessing Extra Data on Tape (HPSS)>`. Other users can access the full data on tape at :ref:`OLCF Constellation<data-access:OLCF Constellation: Full Data on Tape>`.

Accessing Extra Data on Tape (HPSS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The full 2 PB AbacusSummit data set is stored on `NERSC HPSS <https://docs.nersc.gov/filesystems/archive/>`_ (tape). The HPSS directory is::

  /nersc/projects/desi/cosmosim/Abacus/
  
The directory structure mirrors that on disk.

One can list HPSS directory contents with ``hsi`` commands like::

  hsi ls /nersc/projects/desi/cosmosim/Abacus/

Data products are stored in HPSS tarballs, whose file contents can be listed with ``htar`` commands like::

  htar -t -f /nersc/projects/desi/cosmosim/Abacus/AbacusSummit_base_c000_ph000/Abacus_AbacusSummit_base_c000_ph000_halos.tar

To extract files to disk from an htar archive, one can use the same command but substitute the ``-t`` flag for ``-x``. Be sure to examine the output of the ``-t`` command first to make sure you have enough disk space for the extracted files!

One can also access just a subset of files in an htar archive. For example, to see the subsample A & B rv (pos/vel) files at redshift 0.1 in AbacusSummit_base_c000_ph000, use::

  htar -t -f /nersc/projects/desi/cosmosim/Abacus/AbacusSummit_base_c000_ph000/Abacus_AbacusSummit_base_c000_ph000_halos.tar './halos/z0.100/{halo,field}_rv_{A,B}'

See the `NERSC HPSS docs <https://docs.nersc.gov/filesystems/archive/>`_ for more on ``hsi`` and ``htar``.

Public
-------
We are pleased to be able to offer three online portals to access AbacusSummit data:

- the full 2 PB via OLCF's Constellation, tape-backed;
- a 750 TB subset via NERSC, disk-backed;
- a smaller, ad-hoc collection of data and minimal compute resources via Flatiron Institute's BinderHub.

Constellation, as a tape-backed portal, is appropriate for bulk transfers between supercomputer centers. Constellation also contains the HighZ and ScaleFree simulations.  NERSC, as a disk-backed portal, and is appropriate for fetching narrow subsets of the data. Flatiron's BinderHub is suitable for exploratory data analysis without having to download any data.

OLCF Constellation: Full Data on Tape
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Oak Ridge Leadership Computing Facility's `Constellation <https://www.olcf.ornl.gov/olcf-resources/rd-project/constellation-doi-framework-and-portal/>`_ portal hosts the full 2 PB AbacusSummit data set on the magnetic-tape-backed `High Performance Storage System (HPSS) <https://www.olcf.ornl.gov/olcf-resources/data-visualization-resources/hpss/>`_.  HPSS offers high throughput, but high access latency.  To amortize the latency, we aggregate the simulation files with coarse granularity, such that in most cases one must download many TB of data. For example, the halo catalogs for each simulation are in a single tarball (per simulation), which is 6.6 TB for a ``base`` simulation.

There are three DOIs describing various AbacusSummit data products. They are all hosted on Constellation and are listed here:

First Release of Data Products
  The first DOI of AbacusSummit is ``10.13139/OLCF/1811689``.  This is the primary 2 PB dataset containing all data products as they came "off the machine" (notably, no cleaning): halo catalogs, particle subsamples, full particle data, etc.  The DOI itself is a persistent identifer to the following URL, from where the AbacusSummit data may be browsed and downloaded via Globus: https://doi.ccs.ornl.gov/ui/doi/355.
  
Cleaned Halo Catalogs
  The next DOI is ``10.13139/OLCF/1828535``. This contains *cleaned halo catalogs* and particle subsamples.  Additionally, the halo catalogs are aggregated by redshift and simulation type (e.g. ``z0.100_base.tar`` contains all ``base`` simulations at redshift 0.1). Note that even though the cleaning information comes as a set of auxiliary files that annotate the primary catalogs, both the primary and auxiliary files are included in this DOI, thus forming a self-contained dataset. Many users will want to use AbacusSummit through this DOI.  The URL is https://doi.ccs.ornl.gov/ui/doi/363.
  
Halo Light Cone Catalogs
  The DOI of the halo light cone catalogs is ``10.13139/OLCF/1825069``, which directs to https://doi.ccs.ornl.gov/ui/doi/362.
  
Note that it can take many hours before a transfer from Constellation begins if the tape drive is busy. Once it starts, though, the typical bandwidth is several GB/s.

The availability of Constellation depends on the status of HPSS, which undergoes regular downtime for maintenance. If the data is inaccessible, please check the status of HPSS on the following page: https://www.olcf.ornl.gov/for-users/center-status/

NERSC: Subset of Data on Disk
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
NERSC's `Community File System <https://docs.nersc.gov/filesystems/community/>`_ (CFS) hosts a 750 TB subset of the most important AbacusSummit data products.  The portal to this data is here: https://abacusnbody.org/

Using that portal, you can select the desired subset of simulations, data products, and redshifts, and initiate the transfer via Globus.  See :ref:`data-access:using globus`.

This 750 TB subset includes most products except for:

- the 7% "B" particle subsample (halo and field);
- the 3% "A" field particle subsample at redshifts 0.1, 0.3, 0.4, 1.7, 3.0;
- the 100% time slice outputs.

Some simulations, like ``AbacusSummit_highbase_c000_ph100``, have all of their products on disk.  The list of such simulations may change over time depending on user demand.  Browsing the file tree (Globus or NERSC) is the best way to see if a particular simulation happens to have data products that are normally only on tape.

Some data products (initial conditions, merger trees) are not yet exposed via the web interface of this portal, but they can still be manually accessed by browsing the directory tree via Globus.

Note that the web portal is a view to the same directory on NERSC as described in :ref:`data-access:All NERSC Users (including DESI Members)`; the same files are available via both access methods (and thus users analyzing data at NERSC should not download an additional copy via the web portal).

The availability of the NERSC portal depends on the availability of CFS and the DTNs (data transfer nodes). If the data is inaccessible, please check the CFS and DTN status on the following page: https://www.nersc.gov/live-status/motd/

Flatiron Institute BinderHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Flatiron Institute's Scientific Computing Core runs a BinderHub service that allows users to run a JupyterLab session on a Flatiron server that has access to some AbacusSummit data.  Access to the AbacusSummit Binder projects requires sign-up: https://forms.gle/cj9U89irsEVcM7X66. Please also familiarize yourself with the documentation: https://wiki.flatironinstitute.org/Public/UsingFiBinder

.. warning::
    User data storage on BinderHub is ephemeral. **Your data will be deleted after a few days of inactivity!** Be sure to download any important data.

===================================  ==========================
Binder project                       Link
===================================  ==========================
``AbacusSummit`` (CPU-only)          |Binder AbacusSummit|
``AbacusSummit-cuda`` (GPU-enabled)  |Binder AbacusSummit-cuda|
===================================  ==========================

Only a modest amount of compute resources are available to each Binder server, usually around 4 cores and 128 GB RAM. The GPU-enabled environment also has access to a small GPU slice.  Network and IO bandwidth to the AbacusSummit data is also limited, so users should be careful to only load the data they need.

The exact set of simulations and data products that is available via BinderHub may change over time. Data may be added on request, subject to available storage capacity; please open an `issue <https://github.com/abacusorg/AbacusSummit/issues`_ if you have such a request, and please include specific simulations, data products, and redshifts.

Using Globus
~~~~~~~~~~~~
Both the NERSC disk-backed and Constellation tape-backed portals use the Globus interface.  See here for instructions on using Globus: https://docs.globus.org/how-to/get-started/

Note that most university and large computing centers have Globus endpoints already configured.  But for transfers to other sites without pre-configured endpoints, such as a personal computer, one can use `Globus Connect Personal <https://www.globus.org/globus-connect-personal>`_.

What data are available?
------------------------
The :doc:`data-products` page documents the data products.  All products are available at the Constellation portal (including ScaleFree and HighZ) and on NERSC HPSS, and most products are available at the NERSC disk portal.

Some data products (initial conditions, merger trees) are not yet exposed via the web interface of the NERSC portal, but they can still be manually accessed by browsing the directory tree via Globus.

Note that you will want to use the utilities at
https://abacusutils.readthedocs.io/
to unpack the outputs. 

Acknowledgements
----------------
At OLCF, we are grateful to Ross Miller and the Constellation team for providing the opportunity to host this data and for their expert assistance during the creation of the DOI.

The NERSC hosting was made possible with the support of Stephen Bailey, Benjamin Weaver, Eli Dart, Debbie Bard, and Lisa Gerhardt, who we thank warmly.

For additional acknowledgements related to the creation of the suite proper, please see :ref:`authors:acknowledgements & thanks`.


.. |Binder AbacusSummit| image:: https://mybinder.org/badge_logo.svg
   :target: https://binder.flatironinstitute.org/~lgarrison/AbacusSummit

.. |Binder AbacusSummit-cuda| image:: https://mybinder.org/badge_logo.svg
   :target: https://binder.flatironinstitute.org/~lgarrison/AbacusSummit-cuda
