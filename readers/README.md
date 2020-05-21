# AbacusSummit/readers

Code to read AbacusSummit data products has moved to a new repository: https://github.com/abacusorg/abacusutils

The `abacus_halo_catalog.py` file that used to be located here is now called `compaso_halo_catalog.py`
(CompaSO is the name of the Abacus halo finder).  The `AbacusHaloCatalog` class contained within that file
is now called `CompaSOHaloCatalog`, but the API is otherwise unchanged.

abacusutils is now available on pip, which is the recommended installation method.  The halo catalog
reader can be imported with: `from abacusnbody.data.compaso_halo_catalog import CompaSOHaloCatalog`.
