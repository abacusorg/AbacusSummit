# AbacusSummit

[![Documentation Status](https://readthedocs.org/projects/abacussummit/badge/?version=latest)](https://abacussummit.readthedocs.io/en/latest/?badge=latest)

This is the public repository for the specification, utilization,
and documentation of the AbacusSummit suite of high-performance
cosmological N-body simulations.  These simulations were designed
to meet (and exceed) the Cosmological Simulation Requirements of
the Dark Energy Spectroscopic Instrument (DESI) survey.  AbacusSummit
is being run on the Summit supercomputer at the Oak Ridge Leadership
Computing Facility under a time allocation from the DOE's ALCC
program.

Here we give a summary of the AbacusSummit simulation suite and
the data products that will be made available.

The cosmology grid is specified [here](https://github.com/abacusorg/AbacusSummit/blob/master/Cosmologies/README.md).

The simulations themselves are specified [here](https://github.com/abacusorg/AbacusSummit/blob/master/Simulations/README.md).

Code to read the data products is located [here](https://github.com/abacusorg/AbacusSummit/blob/master/readers); this code is still in beta!

## What is Abacus?

Abacus is a high-accuracy cosmological N-body simulation code.  It
is optimized for GPU architectures and for large volume, moderately
clustered simulations.  It is extremely fast: we clock over 30
million particle updates per second on commodity dual-Xeon, dual-GPU
computers and nearly 70 million particle updates per second on each
node of the Summit supercomputer.  But it is also extremely accurate:
typical force accuracy is below 1e-5 and we are using global
timesteps, so the leapfrog timesteps away from the cluster cores
are much smaller than the dynamical time.

Abacus is described in [Garrison et al. (2019, MNRAS, 485, 3370)](https://academic.oup.com/mnras/article/485/3/3370/5371170),
where we detail its performance on the [Schneider et al. (2016)](https://iopscience.iop.org/article/10.1088/1475-7516/2016/04/047) code
comparison simulation, and in [Garrison et al. (2018, ApJS, 236,
43)](https://iopscience.iop.org/article/10.3847/1538-4365/aabfd3), which released an early suite of 125 simulations from 40
cosmologies (https://lgarrison.github.io/AbacusCosmos/).

Abacus is currently actively developed by Lehman Garrison, Nina
Maksimova, and Daniel Eisenstein, with contributions from Boryana
Hadzhiyska and Sownak Bose and consulting from Philip Pinto.  Abacus
was initially developed by Marc Metchnik and Philip Pinto, with
contributions from Daniel Eisenstein and later development led by
Douglas Ferrer.

Abacus development has been supported by NSF AST-1313285 and more
recently by DOE-SC0013718, as well as by Simons Foundation funds
and Harvard University startup funds.  NM was supported as a NSF
Graduate Research Fellow.  The AbacusCosmos simulations were run
on the El Gato supercomputer at the University of Arizona, supported
by grant 1228509 from the NSF; the AbacusSummit simulations have
been supported by OLCF projects AST135 and AST145, the latter through
the Department of Energy ALCC program.

Use of AbacusSummit should cite Maksimova et al. (in prep) for the
simulation suite and the aforementioned Garrison et al. (2019) and Garrison et al.
(2018) for the Abacus code, and [Metchnik (2009)](https://ui.adsabs.harvard.edu/abs/2009PhDT.......175M/abstract) for the initial
method.  Other citations may be requested as we publish more of the
numerical methods.  [Garrison et al. (2016, MNRAS, 461, 4125)](https://academic.oup.com/mnras/article/461/4/4125/2608725) describes
our initial condition methods.  Hadzhiyska et al. (in prep) will
describe our SO group finding method.  Pinto et al. (in prep) will
describe the Abacus far-field method.  Joyce et al. (submitted)
describes accuracy tests using scale-free simulations.


## What is AbacusSummit?

Most of the simulations in AbacusSummit will be 6912<sup>3</sup> = 330 billion 
particles in 2 Gpc/h volume, yielding a particle mass of about 2e9 Msun/h.  

We will run about 150 of these simulations, totaling about 50 trillion
particles.  Detailed specifications of the 
[simulation parameters](https://github.com/abacusorg/AbacusSummit/blob/master/Simulations/README.md)
and 
[cosmological parameters](https://github.com/abacusorg/AbacusSummit/blob/master/Cosmologies/README.md) are available on other pages.
We note that these are only plans and are subject to change.

We will run 25 simulations in one LCDM cosmology (Planck2018),
6 simulations each in 4 other cosmologies, and then 1 simulation
in a spread of other cosmologies, suitable for emulator grids and
blind mock challenges.  We will also likely run some simulations
at 6x higher and 27x lower mass resolutions to support a wider range
of applications and numerical/systematic tests.

All of the simulations start at z=99 utilizing second-order Lagrangian
Perturbation Theory initial conditions following corrections of
first-order particle linear theory; these are described in Garrison
et al. (2016) and have a target correction redshift of 5.  The 
particles are displaced from a cubic grid.

The simulations use spline force softening, described in Garrison
et al. (2018).  Force softening for the standard boxes is 7.2 kpc/h
(Plummer equivalent), fixed in proper (not comoving) distance
and capped at 0.3 of the interparticle spacing at early times.

We use global time steps that begin capped at d(ln a)=0.03 but
quickly drop, tied to a criteria on the ratio of the Mpc-scale
velocity dispersion to the Mpc-scale maximum acceleration, with 
the simulation obeying the most stringent case.  This is scaled
by a parameter eta, which is 0.25 in these simulations.  Simulations
require about 1100 time steps to reach z=0.1.

Users of the outputs probably don't need to know much of the numerical
details of the code, but there is one numerical concept that enter
into the data products.  Abacus uses a cubic grid of size CPD<sup>3</sup>,
chosen to tune code speed.  For AbacusSummit, CPD=1701.  Processing
proceeds in y-z slabs of cells, and particle outputs are ordered
into these cells and slabs.

## AbacusSummit Group Finding

All group finding in AbacusSummit is done on the fly.  We are using
a hybrid algorithm, summarized as follows.

First, we compute a kernel density estimate around all particles.
This uses a weighting (1-r<sup>2</sup>/b<sup>2</sup>), where b is 0.4 of the interparticle
spacing.  We note that the effective volume of this kernel is
equivalent to a top-hat of 0.737b, so 85 kpc/h comoving, and that
the mean weighted counts at an overdensity delta is about delta/10
with a variance of 4/7 of the mean.

Second, we segment the particle set into what we call L0 halos.
This is done with the FOF algorithm with linking length 0.25 of the
interparticle spacing, but only for particles with Delta>60.  We
note that b_FOF=0.25 normally would percolate at a noticeably lower
density, Delta~41 (More et al. 2011, ApJS, 195, 4).  The intention is that
the bounds of the L0 halo set be set by the kernel density estimate,
which has lower variance than the nearest neighbor method of FOF
and imposes a physical smoothing scale.

We stress that all L1/L2 finding and all halo statistics are based
solely on the particles in the L0 halo.  

Third, within each L0 halo, we construct L1 halos by a competitive
spherical overdensity algorithm.  We begin by selecting the particle
with the highest kernel density; this is a nucleus.  We then search
outward to find the innermost radius in which the enclosed density
(of L0 particles only!) dips below 200.  Particles interior to that
radius are tentatively assigned to that group.  Particles interior to 
80% of R200 are marked as ineligible to be a future nucleus.  We
then search the remaining eligible particles to find the one with
the highest remaining kernel density that also meets the criteria of
being a density maximum.  This latter condition is that a particle
must be denser than all other particles (eligible or not) within 0.4 
of the interparticle spacing.  Once located, if this particle has
a high enough density (a condition set by estimating what density would
be generated by a singular isothermal sphere of M200=35 particles), 
we start another nucleus.  

With each successive nucleus, we again search for the SO(200) radius,
using all L0 particles.  Now a particle is assigned to the new group
if is previously unassigned OR if it is estimated to have an enclosed
density with respect to the new group that is twice that of the
enclosed density with respect to its assigned group.  In detail,
these enclosed densities are not computed exactly, but rather scaled
from the SO radius assuming a inverse square density profile.

The idea here is to allow nearby nuclei to divide particles by a
principle similar to that of tidal radii.  However, we stress that
it is not our goal to find subhalos, and so we do not allow new
nuclei to form inside 80% of the SO(200) radius of other L1 halos.  That
said, large substructure just inside this radius may yield a
nucleus away from the center of the secondary object, and the
subsequent enclosed density competition can result in some deblending
of the two objects.

We do not perform any unbinding of particles, such as is sometimes
done with estimates of the gravitational potential and resulting
particle energy.

Fourth, within each L1 halo (and limited to only those particles),
we repeat the SO algorithm to find L2 halos with an enclosed radius
of 800.  We store the masses of the 5 largest such subhalos, which may 
help to mark cases of over-merged L1 halos.  But the main purpose
is that we use the center of mass of the largest L2 subhalo to define 
a center for the output of the L1 statistics.  We do not otherwise
store information about the L2 subhalos.

All density thresholds are scaled upward as the cosmology departs
from Einstein-deSitter, in keeping with spherical collapse estimates
for low density universes.  The FOF linking length is scaled as the
inverse cube root of that change.  The kernel density scale is not
changed.

We output properties for all L1 halos with more than 35 particles.


## AbacusSummit Data Products

We have designed a set of data products aimed at supporting mock
catalogs to be constructed using halo occupation distributions, as
well as efficient access to measurements of the density fields.
Minimization of data volume has been a high priority.  Indeed, we
have stored full particle snapshots only for a few simulations.
Even with this economy, we are producing 2 PB of data products.

The key data products are:
1) Halo catalogs with various statistics computed on-the-fly
from the full particle set.
2) 10% subsamples of particles, consistently selected across redshift,
output with position, velocity, kernel density, and particle ID,
organized so as to preserve halo membership.
3) A light cone stretching from the corner of the box and including
a single second periodic copy of the box.  This provides an octant of
sky to z=0.8 and about 800 sq deg to z=2.4.  The outputs are the 
subsample of particles, as well as the Nside=16384 healpix pixel 
number for all particles.  
4) Full particle catalogs for a few timeslices of a few boxes.

We perform group finding at 12 primary redshifts and 24 secondary
redshifts.  The primary set is z=0.1, 0.2, 0.3, 0.4, 0.5, 0.8, 1.1, 
1.4, 1.7, 2.0, 2.5, and 3.0, and this will be where most users
should focus.

At each primary redshift, we output the properties computed for the
L1 halos in `halo_info` files.  The list of properties is below.

We also output a subsample of the particle, split into 3% and 7%
sets (so 10% total), called A and B, so that users can minimize
their data access depending on application.  These subsamples are
consistent across redshift and are selected based on a hash of the
particle id number, so effectively randomly.

The particles are further split into files based on whether the
particle is in a L0 halo or not.  The particles belonging to a given
L1 halo are contiguous in each of the A and B files, and the start
and number of the two sets are in in the `halo_info` files.  This
allows a user to easily fetch a random subsample of particles from
the L1 halo; we use these for satellite galaxy positions.

Particle positions and velocities are output in one file.  A separate
file contains the unique particle id number, which is easily parsed
as the initial grid position, as well as the kernel density estimate
and a sticky bit that is set if the particle has ever been in the most
massive L2 halo of a L1 halo with more than 35 particles.

Hence, each primary redshift yields 9 set of files: `halo_info` and then
{A,B} x {field,halo} x {RV,PID}.

Each set of files is split into 34 files, containing 50 slabs each 
(51 for the last), to permit users to work on portions of the
simulation.  

A potential confusing aspect is that field particles are assigned
to a file based on the slab number of their cell, but halo particles
are assigned to a file based on the slab number of their L0 halo.
L0 halos can span up to 20 slabs (though most are much smaller, as
a slab is just over 1 Mpc wide) and can involve hundreds of cells.
A L0 halo is assigned to a slab based on the lowest x-value of its
cells.  In other words, if a halo has particles from slabs C..D,
it will be in the file for slab C.  So one cannot simply take the
halo and field files of matching slab range and get the union of
all particles.


For the 24 secondary redshifts, we output the halo catalogs and the 
halo subsample particle IDs (w/densities and sticky L2 tag) only, 
so not the positions/velocities nor the field particles.  

The purpose of the secondary redshifts is to support generation 
of merger trees, as the PIDs can be used to associate halos between
snapshots.  It may also be possible to use the finer redshift sampling
to associate halo catalogs to the light cones, as the subsample of 
particles are the same.  For example, one could use the halo catalog
to generate a HOD at a redshift, assign a given PID to be a satellite
galaxy, then go find that PID in the light cone files.

## AbacusSummit Halo Statistics

Here we list the statistics computed for each halo.

* `uint64_t id`: A unique halo number.

* `uint64_t npstartA`: Where to start counting in the particle output for subsample A

* `uint64_t npstartB`: Where to start counting in the particle output for subsample B

* `uint32_t npoutA`: Number of taggable particles pos/vel/aux written out in subsample A

* `uint32_t npoutB`: Number of taggable particles pos/vel/aux written out in subsample B

* `uint32_t ntaggedA`: Number of tagged particle PIDs written out in subsample A. A particle is tagged if it is taggable and is in the largest L2 halo for a given L1 halo. 

* `uint32_t ntaggedB`; 

* `uint32_t N`: The number of particles in this halo

* `uint32_t L2_N[N_LARGEST_SUBHALOS]`: The number of particles in the largest L2 subhalos

* `uint32_t L0_N`: The number of particles in the L0 parent group

* `float SO_central_particle[3]`: Coordinates of the SO central particle

* `float SO_central_density`: Density of the SO central particle. 

* `float SO_radius`: Radius of SO halo (distance to particle furthest from central particle) 

* `float SO_L2max_central_particle[3]`: Coordinates of the SO central particle for the largest L2 subhalo. 

* `float SO_L2max_central_density`: Density of the SO central particle of the largest L2 subhalo. 

* `float SO_L2max_radius`: Radius of SO halo (distance to particle furthest from central particle) for the largest L2 subhalo


The following quantities are computed using a center defined by 
the center of mass position and velocity of the largest L2 subhalo.
In addition, the same quantities with `_com` use a center defined
by the center of mass position and velocity of the full L1 halo.

All second moments and mean speeds are computed only using
particles in the inner 90% of the mass relative to this center.

* `float x_L2com[3]`: Center of mass pos of the largest L2 subhalo

* `float v_L2com[3]`: Center of mass vel of the largest L2 subhalo

* `float sigmav3d_L2com`: Sum of eigenvalues

* `float meanSpeed_L2com`: Mean speed

* `float sigmav3d_r50_L2com`: Velocity dispersion of the inner 50% of particles

* `float meanSpeed_r50_L2com`: Mean speed of the inner 50% of particles

* `float r100_L2com`: Radius of 100% of mass, relative to L2 center. 

* `float vcirc_max_L2com`: max circular velocity, based on the particles in this L1 halo 

* `int16_t sigmavMin_to_sigmav3d_L2com`: Min(sigmav_eigenvalue) / sigmav3d, compressed

* `int16_t sigmavMax_to_sigmav3d_L2com`: Max(sigmav_eigenvalue) / sigmav3d, compressed

* `uint16_t sigmav_eigenvecs_L2com`: Eigenvectors of the velocity dispersion tensor, compressed into 16 bits. 

* `int16_t sigmavrad_to_sigmav3d_L2com`: sigmav_rad / sigmav3d, compressed

* `int16_t sigmavtan_to_sigmav3d_L2com`: sigmav_tan / sigmav3d, compressed

* `int16_t r10_L2com`, `r25_L2com`, `r33_L2com`, `r50_L2com`, `r67_L2com`, `r75_L2com`, `r90_L2com`, `r95_L2com`, `r98_L2com`: Radii of this percentage of mass, relative to L2 center. Expressed as ratios of r100 and compressed to int16. 

* `int16_t sigmar_L2com[3]`: The eigenvalues of the moment of inertia tensor

* `int16_t sigman_L2com[3]`: The eigenvalues of the weighted moment of inertia tensor, in which we have computed the mean square of the normal vector between the COM and each particle.

* `uint16_t sigmar_eigenvecs_L2com`: The eigenvectors of the inertia tensor, compressed

* `uint16_t sigman_eigenvecs_L2com`: The eigenvectors of the weighted inertia tensor, compressed

* `int16_t rvcirc_max_L2com`: radius of max circular velocity, stored as ratio to r100, relative to L2 center

In most cases, these quantities are compressed or bit truncated to save space.  
Sometimes this is simple: e.g., when we have the chance to store a ratio in the range [0,1], we
multiply by 32000 and store as an int16.  Others are more complicated, e.g., 
the Euler angles of the eigenvectors are stored to about 4 degree precision and
all packed into an uint16.

We are providing a Python package to undo this compression and expose
Astropy tables (and therefore NumPy arrays) to the user.


## AbacusSummit Light Cones

The light cone is structured as three periodic copies of the box,
centered at (0,0,0), (0,0,2000), and (0,2000,0) in Mpc/h units.  This is observed
from the location (-950, -950, -950), i.e., 50 Mpc inside a corner.
This provides an octant to a distance of 1950 Mpc/h (z=0.8), shrinking
to two patches each about 800 square degrees at a distance of 3950 Mpc/h (z=2.4).

The three boxes are output separately and the positions are referred
to the center of each periodic copy, so the particles from the higher
redshift box need to have 2000 Mpc/h added to their z coordinate.

Particles are output from every time step (recall that these
simulations use global time steps for each particle).  In each step,
we linearly interpolate to find the time when the light cone
intersects this each particle, and then linearly update the position
and velocity to this time.

The HealPix pixels are computed using +z as the North Pole, i.e., 
the usual (x,y,z) coordinate system.


## AbacusSummit Data Model

Here we describe the data model of the AbacusSummit data products.

Nearly all files are stored as ASDF files, which is a successor to
FITS.  Inside each binary block of ASDF, we have applied BLOSC
compression using the ZSTD algorithm, typically with a byte or bit
shuffle.  BLOSC+ZSTD provides fast decompression and good compression
ratios.  We provide a custom fork of the ASDF python library that 
will apply the BLOSC decompression on the fly.  [GIVE URL]
If one doesn't have the custom fork, then one will need to read 
the ASDF binary blocks and pipe through the BLOSC decompression.

The ASDF header is human-readable, meaning one can use a Linux
command line tool like `less` to examine the simulation metadata
stored in every ASDF file.

The halo statistics are in `halo_info` files.  These are stored as
ASDF files, where each column is in a contiguous binary portion.
Importantly, ASDF allows one to load only a subset of columns, 
which can be important to save both memory and time.  

The particles position and velocities are stored in RV files in a
bit-truncated and compressed format.  What is revealed to the user
is three 32-bit integers, for x, y, and z.  The positions map
[-0.5,0.5] to +-500,000 and are stored in the upper 20 bits.  The
velocites are mapped from [-6000,6000) km/s to [0,4096) and stored
in the lower 12 bits.

The particle id numbers and kernel densities are stored in PID files
packed into a 64-bit integer.  The id numbers are simply the (i,j,k)
index from the initial grid, and these 3 numbers are placed as the
lower three 16-bit integers.  The kernel density is stored as the
square root of the density in cosmic density units in bits 1..12
of the upper 16-bit integer.  Bit 0 is used to mark whether the
particle has ever been inside the largest L2 halo of a L1 halo with
more than 35 particles; this is available to aid in merger tree
construction.

The timeslice positions are stored at mildly higher bit resolution using
a format we call pack9.  Here, particles are stored contiguously in
their cells.  Each cell starts with a 9-byte header that indicates
the cell index and velocity scaling, and then each particle is
stored as 9-bytes with 12 bits for each position and each velocity.
We provide a C code to undo this compression.

CRC32 checksums are provided for all files.  These should match the
GNU `cksum` utility, pre-installed in most Linux environments.
We also offer a fast implementation of `cksum` with about 10x better performance:
https://github.com/abacusorg/fast-cksum.
