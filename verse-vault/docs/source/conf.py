# Configuration file for the Sphinx documentation builder.
#

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))


# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Verse Vault'
copyright = '2025, Bernardo Fernandes'
author = 'Bernardo Fernandes'
release = '1.0'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',  # Auto-generate docs from docstrings
    'sphinx.ext.napoleon',  # Support for Google-style docstrings
    'sphinx.ext.viewcode'  # Adds links to source code
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# Set theme (optional)
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
