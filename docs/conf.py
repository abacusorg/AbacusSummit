# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

# LHG: this is the author order of the AbacusSummit paper, plus the Phil from the ALCC proposal
project = 'AbacusSummit'
copyright = '2023, Nina Maksimova, Lehman Garrison, Daniel Eisenstein, Boryana Hadzhiyska, Sownak Bose, Thomas Satterthwaite, and Philip Pinto'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.intersphinx',
              'sphinx.ext.autosectionlabel']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build']
root_doc = "index"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
#html_theme = 'default'
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['custom.css']

html_title = "AbacusSummit"
html_logo = "images/AbacusSummit_logo_bw.png"
html_favicon = 'images/icon_red.png'

html_show_sourcelink = False
html_theme_options = {
    "repository_url": "https://github.com/abacusorg/AbacusSummit",
    "repository_branch": "main",
    # "launch_buttons": {
    #     "binderhub_url": "https://mybinder.org",
    #     "notebook_interface": "jupyterlab",
    #     "colab_url": "https://colab.research.google.com/",
    # },
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_download_button": True,
    "use_fullscreen_button": False,
    "logo_only": True,
    "path_to_docs": "docs/",
}

intersphinx_mapping = {'abacusutils': ('https://abacusutils.readthedocs.io/en/latest', None)}

autosectionlabel_prefix_document = True
