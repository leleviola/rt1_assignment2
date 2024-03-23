# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import subprocess
import sys
sys.path.insert(0, os.path.abspath('../'))
show_authors = True

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'rt1_assignment2'
copyright = '2024, samuele viola'
author = 'samuele viola'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
highlight_language = 'python'
source_suffix = '.rst'
master_doc = 'index'
#html_theme = 'sphinx_rtd_theme'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    "sphinx.ext.napoleon",
    'sphinx.ext.inheritance_diagram',
    'breathe'
]

templates_path = ['_templates']
exclude_patterns = []

# Options for intersphinx extension
interspinx_mapping = {'python':('https://docs.python.org/3', None)}

todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


# Options for breathe
breathe_projects = {
    "rt1_assignment2":"../build/xml/"
}
breathe_default_projects = "turtlebot_controller"
breathe_default_members = ('members', 'undoc-members')