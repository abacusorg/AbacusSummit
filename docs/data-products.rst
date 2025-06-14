Data Products
=============

Overview
--------

We have designed a set of data products aimed at supporting mock
catalogs to be constructed using halo occupation distributions, as well
as efficient access to measurements of the density fields. Minimization
of data volume has been a high priority. Indeed, we have stored full
particle snapshots only for a few simulations. Even with this economy,
we are producing 2 PB of data products.

The key data products are:

1. **Halo catalogs** with various statistics computed on-the-fly from the
   full particle set.

2. **10% subsamples of particles**, consistently selected across redshift,
   output with position, velocity, kernel density, and particle ID,
   organized so as to preserve halo membership.

3. A **light cone** stretching from the corner of the box and including a
   single second periodic copy of the box. This provides an octant of sky
   to z=0.8 and about 800 sq deg to *z*\=2.4. The outputs are the subsample
   of particles, as well as the Nside=16384 healpix pixel number for all
   particles.

4. **Full particle catalogs** for a few timeslices of a few boxes.

We perform group finding at 12 primary redshifts and 21 secondary
redshifts.  Most users should focus on the primary redshifts.

- **Primary redshifts**: *z*\=0.1, 0.2, 0.3, 0.4, 0.5, 0.8, 1.1, 1.4, 1.7, 2.0, 2.5, 3.0

- **Primary + Secondary redshifts**: *z*\=0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.575, 0.65, 0.725, 0.8, 0.875, 0.95, 1.025, 1.1, 1.175, 1.25, 1.325, 1.4, 1.475, 1.55, 1.625, 1.7, 1.85, 2.0, 2.25, 2.5, 2.75, 3.0, 5.0, 8.0

.. note ::
    The 21 "secondary" redshifts are only approximate and may not match
    from simulation to simulation.  We do not shorten the Abacus
    timestep to land exactly on these secondary redshifts as we do
    for the primary redshifts.  Always use the redshift in the header,
    not the directory name.

At each primary redshift, we output the properties computed for the L1
halos in ``halo_info`` files (see :doc:`compaso`). The list of properties is below.

We also output a subsample of the particle, split into 3% and 7% sets
(so 10% total), called "A" and "B", so that users can minimize their data
access depending on application. These subsamples are consistent across
redshift and are selected based on a hash of the particle ID number, so
effectively randomly.

The particles are further split into files based on whether the particle
is in a L0 halo or not. The particles belonging to a given L1 halo are
contiguous in each of the A and B files, and the start and number of the
two sets are in in the ``halo_info`` files. This allows a user to easily
fetch a random subsample of particles from the L1 halo; we use these for
satellite galaxy positions.

Particle positions and velocities are output in one file. A separate
file contains the unique particle ID number, which is easily parsed as
the initial grid position, as well as the kernel density estimate and a
sticky bit that is set if the particle has ever been in the most massive
L2 halo of a L1 halo with more than 35 particles.

Hence, each primary redshift yields 9 set of files: ``halo_info`` and
then {A,B} x {field,halo} x {RV,PID}.

Each set of files is split into 34 files, containing 50 slabs each (51
for the last), to permit users to work on portions of the simulation.

A potential confusing aspect is that field particles are assigned to a
file based on the slab number of their cell, but halo particles are
assigned to a file based on the slab number of their L0 halo. L0 halos
can span up to 20 slabs (though most are much smaller, as a slab is just
over 1 Mpc wide) and can involve hundreds of cells. A L0 halo is
assigned to a slab based on the lowest x-value of its cells. In other
words, if a halo has particles from slabs C..D, it will be in the file
for slab C. So one cannot simply take the halo and field files of
matching slab range and get the union of all particles.

.. note ::
   Most applications will need to load at least one padding file
   on either side of the file under consideration in order to ensure
   all halos and particles within a compact range of *X* coordinates
   are present in memory.

For the 21 secondary redshifts, we output the halo catalogs and the halo
subsample particle IDs (w/densities and sticky L2 tag) only, so not the
positions/velocities nor the field particles.

The purpose of the secondary redshifts is to support generation of
merger trees, as the PIDs can be used to associate halos between
snapshots. It may also be possible to use the finer redshift sampling to
associate halo catalogs to the light cones, as the subsample of
particles are the same. For example, one could use the halo catalog to
generate a HOD at a redshift, assign a given PID to be a satellite
galaxy, then go find that PID in the light cone files.

Data Model
----------

All files are in `ASDF format <https://asdf.readthedocs.io>`_. Most of the files
have only one binary block. The only exception are the ``halo_info`` files,
where every column of the table is a separate block. This allows the user
to load only the columns needed for an analysis.

.. note ::
   Loading a narrow subset of halo catalog columns can save substantial
   time and memory.  Within abacusutils, use the ``fields`` argument to
   the :doc:`CompaSOHaloCatalog constructor <abacusutils:compaso>` to achieve this.

Within ASDF, we apply compression to each binary block. We do this via
the `Blosc package <https://blosc.org/pages/blosc-in-depth/>`_, using
bit/byte transposition followed by `zstd compression <https://facebook.github.io/zstd/>`_.
We have found that transposition gives substantially better
compression ratios (we chose bit vs byte empirically for each file
type) and that ``zstd`` provides fast decompression, fast enough that
one CPU core can keep up with most network disk array read speeds.
The abacusutils package uses the ASDF compression extension API
to allow users to transparently load the files ones they have installed
abacusutils and ASDF.

The ASDF header is human-readable, meaning one can use a Linux command
line tool like ``less`` to examine the simulation metadata stored in
every ASDF file. This was one motivation for choosing ASDF over HDF5.  We
include various descriptive and quantitative aspects of the simulation in this header.

The halo statistics are in ``halo_info`` files. These columns of these
outputs are described below. Most are substantially compressed,
including using ratios (e.g., of radii) to scale variables. As such, the
binary format of the columns will differ from that revealed by the
Python package.

CRC32 checksums are provided for all files in the ``checksums.crc32``
file that resides in each directory. These should match the GNU
``cksum`` utility, pre-installed in most Linux environments. We also
offer a fast implementation of ``cksum`` with about 10x better
performance here: https://github.com/abacusorg/fast-cksum.

Halo Statistics
---------------

Here is the list of statistics computed on each CompaSO halo.
In most cases, these quantities are condensed to reduce the bit
precision and thereby save space; this is in addition to the
transposition/compression performed in the ASDF file storage. Sometimes
the condensing is simple: e.g., when we have the chance to store a
quantity (often a ratio) in the range [0,1], we multiply by 32000 and
store as an int16. Others are more complicated, e.g., the Euler angles
of the eigenvectors are stored to about 4 degree precision and all
packed into an uint16.

We provide a Python package to undo this condensation and expose
Astropy tables (and therefore NumPy arrays) to the user. See
https://abacusutils.readthedocs.io for details and
installation instructions.

The listing below gives the data format in the binary files, but also
gives the format that is revealed to the user by the Python when that differs.

Keep in mind that the halo catalog consists of purely L1 halos
(see :doc:`compaso`), and that the spherical overdensity definition
is a function of epoch. The value is stored in the ``SODensityL1``
header field (relative to the mean cosmic density).

-  ``uint64_t id``: A unique halo number.

-  ``uint64_t npstartA``: Where to start counting in the particle output
   for subsample A

-  ``uint64_t npstartB``: Where to start counting in the particle output
   for subsample B

-  ``uint32_t npoutA``: Number of taggable particles pos/vel/aux written
   out in subsample A

-  ``uint32_t npoutB``: Number of taggable particles pos/vel/aux written
   out in subsample B

-  ``uint32_t ntaggedA``: Number of tagged particle PIDs written out in
   subsample A. A particle is tagged if it is taggable and is in the
   largest L2 halo for a given L1 halo.

-  ``uint32_t ntaggedB``: likewise for subsample B;

-  ``uint32_t N``: The number of particles in this halo.  This is the primary halo mass field.

-  ``uint32_t L2_N[N_LARGEST_SUBHALOS]``: The number of particles in the
   largest L2 subhalos

-  ``uint32_t L0_N``: The number of particles in the L0 parent group

-  ``float SO_central_particle[3]``: Coordinates of the SO central
   particle

-  ``float SO_central_density``: Density of the SO central particle.

-  ``float SO_radius``: Radius of SO halo (distance to particle furthest
   from central particle, or a constant if the SO crossing is not reached)

-  ``float SO_L2max_central_particle[3]``: Coordinates of the SO central
   particle for the largest L2 subhalo.

-  ``float SO_L2max_central_density``: Density of the SO central
   particle of the largest L2 subhalo.

-  ``float SO_L2max_radius``: Radius of SO halo (distance to particle
   furthest from central particle) for the largest L2 subhalo

The following quantities are computed using a center defined by the
center of mass position and velocity of the largest L2 subhalo. In
addition, the same quantities with ``_com`` use a center defined by the
center of mass position and velocity of the full L1 halo.

All second moments and mean speeds are computed only using particles in
the inner 90% of the mass relative to this center.

-  ``float x_L2com[3]``: Center of mass pos of the largest L2 subhalo.

-  ``float v_L2com[3]``: Center of mass vel of the largest L2 subhalo.

-  ``float sigmav3d_L2com``: The 3-d velocity dispersion, i.e., the
   square root of the sum of eigenvalues of the second moment tensor of
   the velocities relative to the center of mass.

-  ``float meanSpeed_L2com``: Mean speed of particles, relative to the
   center of mass.

-  ``float sigmav3d_r50_L2com``: Velocity dispersion (3-d) of the inner
   50% of particles.

-  ``float meanSpeed_r50_L2com``: Mean speed of the inner 50% of
   particles.

-  ``float r100_L2com``: Radius of 100% of mass, relative to L2 center.

-  ``float vcirc_max_L2com``: Max circular velocity, relative to the
   center of mass position and velocity, based on the particles in this
   L1 halo .

-  ``int16_t sigmavMin_to_sigmav3d_L2com``: Min(sigmav\_eigenvalue) /
   sigmav3d, condensed to [0,30000].

-  ``int16_t sigmavMax_to_sigmav3d_L2com``: Max(sigmav\_eigenvalue) /
   sigmav3d, condensed to [0,30000].

-  ``uint16_t sigmav_eigenvecs_L2com``: Eigenvectors of the velocity
   dispersion tensor, condensed into 16 bits.

-  ``int16_t sigmavrad_to_sigmav3d_L2com``: sigmav\_rad / sigmav3d,
   condensed to [0,30000].

-  ``int16_t sigmavtan_to_sigmav3d_L2com``: sigmav\_tan / sigmav3d,
   cndensed to [0,30000].

-  ``int16_t r10_L2com``, ``r25_L2com``, ``r33_L2com``, ``r50_L2com``,
   ``r67_L2com``, ``r75_L2com``, ``r90_L2com``, ``r95_L2com``,
   ``r98_L2com``: Radii of this percentage of mass, relative to L2
   center. Expressed as ratios of r100 and condensed to [0,30000].

-  ``int16_t sigmar_L2com[3]``: The square root of eigenvalues of the
   moment of inertia tensor, as ratios to r100, condensed to [0,30000].

-  ``int16_t sigman_L2com[3]``: The square root of eigenvalues of the
   weighted moment of inertia tensor, in which we have computed the mean
   square of the normal vector between the COM and each particle,
   condensed to [0,30000].

-  ``uint16_t sigmar_eigenvecs_L2com``: The eigenvectors of the inertia
   tensor, condensed into 16 bits.

-  ``uint16_t sigman_eigenvecs_L2com``: The eigenvectors of the weighted
   inertia tensor, condensed into 16 bits

-  ``int16_t rvcirc_max_L2com``: Radius of max circular velocity,
   relative to the L2 center, stored as the ratio to r100 condensed to
   [0,30000].

Halo light cone catalogs
~~~~~~~~~~~~~~~~~~~~~~~~
The halo light cone catalogs contain several additional fields listed below.

- ``int64_t index_halo``: Index of the halo into the full redshift catalogue
- ``uint32_t N_interp``: Interpolated number of particles in the halo.
- ``float pos_interp[3]``: Interpolated centre of mass position of the largest L2 subhalo.
- ``float vel_interp[3]``: Interpolated centre of mass velocity of the largest L2 subhalo.
- ``float pos_avg[3]``: Average position of the subsample A and B particles in the halo.
- ``float vel_avg[3]``: Average velocity of the subsample A and B particles in the halo.
- ``float redshift_interp``: Interpolated redshift at which the light cone crosses the halo path.
- ``int8_t origin``: Index of the box from which the halo is taken (``0`` signifies the original box, ``1`` and ``2`` - copies of the original box), stored as integer between 0 and 5 (if the raw field ``origin >= 3``, then no merger history is available for this halo, so ``(pos|vel)_interp`` coincides with ``(x|v)_L2com``; when loading with the Python package, the ``origin`` field is modified ``origin %= 3``, and the fields ``(pos|vel)_interp`` of the halos without merger history are substituted with ``(pos|vel)_avg``).

For more details on how these quantities are computed, see `Hadzhiyska et al. (2021) <https://academic.oup.com/mnras/advance-article/doi/10.1093/mnras/stab3066/6408495>`_.
  
Units
~~~~~
The units of positions/radii and velocities, as unpacked by ``abacusutils``
in Python, are comoving Mpc/*h* and proper km/s.

In the raw ``halo_info`` files on disk, positions and radii (where not
normalized in a ratio) are in units of the unit box, while velocities are
in km/s. Densities are in units of the cosmic mean (so the mean density is 1).

The Abacus convention is
to store positions in the range [-BoxSize/2, BoxSize/2), so if your code
expects [0, BoxSize) positions, you may need to apply periodic wrap.
A wrap is recommended instead of a shift of +BoxSize/2 because the former
preserves the origin of the box, which is sometimes useful when comparing
with other data products or other *N*-body codes that have run the same
simulation.

The primary halo mass field is ``N``, the number of particles in the halo.
This can be converted to M\ :sub:`☉`\ /*h* units with the ``ParticleMassHMsun``
header field.

The conversion of proper km/s to comoving redshift-space displacement may
be achieved by multiplying by ``BoxSize/VelZSpace_to_kms``.  The numerator
brings it from unit-box to BoxSize-box, and the denominator brings it to comoving RSD.

Known Bugs
~~~~~~~~~~
None at present.

Frequently Asked Questions
~~~~~~~~~~~~~~~~~~~~~~~~~~
SO_radius special value
************************
Some fraction of low-mass halos have ``SO_radius`` all equal to the same
value, which is approximately 1.36 Mpc/*h* in the "base" sims.  This occurs
when the halo still does not drop below the SO threshold even at its most
distant particle.  The enclosed density is guaranteed to be below the SO
threshold at this special value, but if the exact value is desired, one can
trivially compute this using the halo mass and the mean background density.
(Previously, this special value had been listed on this website as a bug,
but this has now been clarified as intended behavior of CompaSO).

The exact value of the special number is a computational detail but may
be computed as ``X*BoxSize/CPD*sqrt(3)/3``, where ``X`` is equal to 2 in
the overwhelming majority of cases.  It is allowed to be equal to 3 or
greater integers, but in AbacusSummit base simulations, this is about 7 orders
of magnitude rarer.

None of the other radial fields (e.g. the radial percentiles, ``r10``, ``r25``, etc)
should exhibit a special value in this way.

Particle data
-------------

The particle positions and velocities from subsamples are stored in
"RV" files. The positions and velocities have been condensed into
three 32-bit integers, for x, y, and z. The positions map [-0.5,0.5] to
+-500,000 and are stored in the upper 20 bits. The velocites are mapped
from [-6000,6000) km/s to [0,4096) and stored in the lower 12 bits. The
resulting Nx3 array of int32 is then compressed within ASDF.

The particle positions and velocities from full timeslices are stored in
``pack9`` files. These provide mildly higher bit precision, albeit with
some complexity. Particles are stored in cells (a cubic grid internal to
Abacus). Each cell has a 9-byte header, containing the cell 3-d index
and a velocity scaling, and then each particle is stored as 9 bytes,
with 12 bits for each position and velocity component. As the base
simulations have 1701 cells per dimension, this is about 23 bits of
positional precision.

The particle ID numbers and kernel densities are stored in ``PID`` files
packed into a 64-bit integer. The ID numbers are simply the ``(i,j,k)``
index from the initial grid, and these 3 numbers are placed as the lower
three 16-bit integers. The kernel density is stored as the square root
of the density in cosmic density units in bits 1..12 of the upper 16-bit
integer. Bit 0 is used to mark whether the particle has ever been inside
the largest L2 halo of a L1 halo with more than 35 particles; this is
available to aid in merger tree construction.

When using the ``npstartA`` and ``npoutA`` fields to index the halo particle
subsamples, one might noticed that ``sum(halos['npoutA'])`` is less than
``len(halo_subsamples)``.  In other words, there are unindexed halo particles.
This is because the subsamples are taken from the L0 particles, but only
the L1 particles are indexed by halos (see :doc:`compaso` for the distinction).


Light Cones
-----------

For the base boxes, the light cone is structured as three periodic
copies of the box, centered at (0,0,0), (0,0,2000), and (0,2000,0) in
Mpc/*h* units. This is observed from the location (-990, -990, -990),
i.e., 10 Mpc/*h* inside a corner. This provides an octant to a distance of
1990 Mpc/*h* (*z*\=0.8), shrinking to two patches each about 800 square
degrees at a distance of 3990 Mpc/*h* (*z*\=2.4).

The three boxes are output separately and the positions are referred to
the center of each periodic copy, so the particles from the higher
redshift box need to have 2000 Mpc/*h* added to their *z* coordinate.

Particles are output from every time step (recall that these simulations
use global time steps for each particle). In each step, we linearly
interpolate to find the time when the light cone intersects this each
particle, and then linearly update the position and velocity to this
time.

Each time step generates a separate file, which includes the entire box,
for each periodic copy.

We store only a subsample of particles, the union of the A and B
subsets (so 10%). Positions are in the "RV" format; ID numbers and kernel
density estimates are in the "PID" format.

The HealPix pixels are computed using +\ *z* as the North Pole, i.e., the
usual (*x*\,\ *y*\,\ *z*\) coordinate system. We choose Nside=16384 and store the
resulting pixel numbers as int32. We output HealPix from all particles.
Particle pixel numbers from each slab in the box are sorted prior to
output; this permits better compression (down to 1/3 byte per
particle!).

For the huge boxes, the light cone is simply one copy of the box,
centered at (0,0,0). This provides a full-sky light cone to the the
half-distance of the box (about 4 Gpc/*h*), and further toward the eight
corners.


Initial Conditions
------------------
The initial density fields are saved in configuration space at two resolutions,
576\ :sup:`3` and 1152\ :sup:`3`.  The resulting particle displacements under the
Zel'dovich approximation are also saved (Abacus applies 2LPT on-the-fly,
so the files only contain ZA).  For the covariance suite of 500 Mpc/*h* boxes,
only the lower resolution is available.

The ICs are saved in ASDF files and should have a discoverable data structure.
In addition to the usual parameter set, a set of growth factors D(*z*)/D(*z*\ :sub:`init`)
are saved as the parameter name ``GrowthTable``.  The input linear power spectrum
is also saved in the file.

The initial density field is in units of fractional overdensity at *z*\ :sub:`init`.
The ``[0,0,0]`` element of the field is at location ``(x,y,z)=(-L/2,-L/2,-L/2)``,
where ``L`` is the box size, following the Abacus convention of zero-centered domain.
Note that this is like a "cell corner" convention, keeping in mind that there actually
are no "cells" at this point in the computation, just a lattice—the entire problem is
discrete.

The displacements are in units of comoving Mpc/*h*.

These publicly available ICs are, of course, lower resolution than those used in
the full simulation.  These lower resolutions are generated by running the IC generator
with a smaller FFT mesh, and therefore only filling modes to the Nyquist wavenumber of
this mesh.  The result is equivalent to a sharp k-space filter on the high-resolution ICs.

Likewise, the proper procedure for users to produce even lower resolution density fields
is to Fourier transform the field and band-limit to the desired resolution.

Note that the IC density fields (``ic_dens_*.asdf``) are a direct output of the Gaussian random
field in the IC code, \*before\* any particles are created. Therefore, there is no mass assignment
window function to deconvolve when taking the Fourier transform.

These ICs have modes filled to the Nyquist cube; that is, they contain corner modes.
The full resolution ICs did not.

Late-time particle samples (e.g. from halo catalogs) can be connected to their
location in the ICs via the PID.  Pass ``unpack_bits="lagr_pos"`` or ``unpack_bits="lagr_idx"``
to the :doc:`CompaSOHaloCatalog constructor <abacusutils:compaso>`, or to the ``load`` parameter
of  :doc:`read_asdf <abacusutils:abacusnbody.data>`.

Fixed-and-paired ICs
~~~~~~~~~~~~~~~~~~~~
The ``fixedbase`` simulations use fixed-amplitude initial conditions (``ZD_qPk_fix_to_mean = 1``), with ``ph098`` the
inverse of ``ph099``.  This inversion was implemented with a flag to Abacus that flipped
the Zel'dovich displacements as they were ingested (``FlipZelDisp = 1``); the actual IC files were the same for
``ph098`` and ``ph099``. As a consequence, the IC data products are identical for ``ph098``
and ``ph099``, even though one might expect them to be inverted.  We recommend users of
``ph098`` invert the density field and displacements themselves, which in both cases is
as simple as multiplying the fields by :math:`-1`.
