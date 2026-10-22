Changelog
=========

This page contains changes to data, data products, or data availability that users might want to be aware of.

Granular changes to the documentation are always available in the `repo history <https://github.com/abacusorg/AbacusSummit/commits/main/>`_.

2026 Oct
--------
The redshift-space power spectrum multipoles were discovered to be faulty. When originally measured, the
particles were displaced along the x-axis to apply the redshift-space distortion, but the multipoles were
measured with the z-axis as the line of sight. Statistically, the monopole is still correct, though with
displacement in x rather than z. Some information may be recoverable from the quadrupole, but the hexadecapole
should probably not be used.

Consequently, the affected files ``power_*_zspace.*`` were renamed to ``faulty_power_*_zspace.*``.

The following simulations were *not* affected:

* All Abacus_DESI2 and Abacus_pngbase simulations
* AbacusSummit_base_c003_ph002, c003_ph005, c004_ph004, c004_ph005, c141_ph000, c154_ph000, and c169_ph000
* AbacusSummit_fixedbase_c000_ph099

All other simulations were affected, meaning:

* AbacusSummit base, fixedbase, high, highbase, huge, hugebase, and small, plus HighZ

Thanks to Thiago Pereira for reporting this.

Separately, the subsample power spectra computed in 2025 May (see below) were measured from the A particle
subsample (3%) alone, rather than A and B together (10%) as in the other simulations. Their shot noise (which is
not subtracted) is therefore about 3.3 times higher. Their directories have been renamed from ``AB`` to ``A``
accordingly.

2025 May
--------
* Missing power spectra computed for:

  * AbacusSummit_base_c003_ph002
  * AbacusSummit_base_c003_ph005
  * AbacusSummit_base_c004_ph004
  * AbacusSummit_base_c004_ph005
  * AbacusSummit_base_c141_ph000
  * AbacusSummit_base_c154_ph000
  * AbacusSummit_base_c169_ph000
  * AbacusSummit_fixedbase_c000_ph099

2024 Dec. 14
------------
* Description of cosmology c116 fixed. Thanks to David Weinberg for pointing this out.

2024 July
---------
* New BinderHub data access option added

2023 Oct
--------
* DESI2 simulations added
* pngbase simulations added

2021 Oct. 21
------------
* AbacusSummit public release (paper submitted to arXiv)
