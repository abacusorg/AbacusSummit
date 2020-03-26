# AbacusSummit/readers

This directory contains code to read AbacusSummit data products, like halo catalogs.
This is a temporary way to distribute these utilities until they've matured to the
point that we upload them to a package manager.

## Dependencies

Essentially all AbacusSummit data products are packaged in [ASDF](https://asdf.readthedocs.io/)
files with blosc compression.  The compression should be transparent to the user, but for now
we require users to run our fork of ASDF that supports blosc.  This is a temporary solution until
ASDF supports blosc upstream, or we package the decompressor in a pluggable manner.

Our fork of ASDF can be installed with:
```console
~$ git clone --recursive https://github.com/lgarrison/asdf.git
~$ cd asdf
~/asdf$ pip install .  # << note the dot
~/asdf$ pip install blosc  # another dependency
```

In Python, we load the ASDF files into [Astropy tables](http://docs.astropy.org/en/stable/table/),
so Astropy is another dependency.

## `abacus_halo_catalog.py`
Use `abacus_halo_catalog.py` to read Abacus halo catalogs.  Place this file in the directory
from which you are running Python, or place the directory in your `PYTHONPATH` environment variable.
This is a temporary solution for installing this module until we move to a package manager.

Here is a brief example of how to use this module; the file itself contains more documentation.
More detailed documentation and examples will eventually be available online.

```pycon
>>> from abacus_halo_catalog import AbacusHaloCatalog
>>> # Load the halo catalog and particle subsample A for redshift 0.1
>>> cat = AbacusHaloCatalog('/storage/AbacusSummit/AbacusSummit_000/halos/z0.100', load_subsamples='A_all')
>>> print(cat.halos[:5])  # cat.halos is an Astropy Table, print the first 5 rows
   id    npstartA npstartB ... sigmavrad_L2com sigmavtan_L2com rvcirc_max_L2com
-------- -------- -------- ... --------------- --------------- ----------------
25000000        0        2 ...       0.9473971      0.96568024      0.042019103
25000001       11       12 ...      0.86480814       0.8435805      0.046611086
48000000       18       15 ...      0.66734606      0.68342227      0.033434115
58000000       31       18 ...      0.52170926       0.5387341      0.042292822
58001000       38       23 ...       0.4689916      0.40759262      0.034498636
>>> print(cat.halos['N','x_com'][:5])  # print the position and mass of the first 5 halos
  N         x_com [3]        
--- ------------------------
278 -998.88525 .. -972.95404
 45  -998.9751 .. -972.88416
101   -999.7485 .. -947.8377
 82    -998.904 .. -937.6313
 43   -999.3252 .. -937.5813
>>> # Examine the particle subsamples associated with the 5th halo
>>> h5 = cat.halos[4]
>>> print(cat.subsamples['pos'][h5['npstartA']:h5['npstartA'] + h5['npoutA']])
        pos [3]         
------------------------
  -999.3019 .. -937.5229
 -999.33435 .. -937.5515
-999.38965 .. -937.58777
>>> # At a glance, the pos fields match that of the 5th halo above, so it appears we have indexed correctly!
```

