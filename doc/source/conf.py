# -*- coding: utf-8 -*-
#
# Octavia documentation build configuration file, created by
# sphinx-quickstart on Tue May 21 17:43:32 2013.
#
# This file is execfile()d with the current directory set to its containing
# dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys

import openstackdocstheme
from pydotplus import graphviz
import sadisplay

import octavia.db.models as models

sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(0, os.path.abspath('.'))

from tools import create_flow_docs

# Generate our flow diagrams
create_flow_docs.generate(
    'tools/flow-list.txt', 'doc/source/contributor/devref/flow_diagrams')

# Generate entity relationship diagram
desc = sadisplay.describe(
    [getattr(models, attr) for attr in dir(models)],
    show_methods=True,
    show_properties=True,
    show_indexes=True,
)
graph = graphviz.graph_from_dot_data(sadisplay.dot(desc).encode('utf-8'))
graph.write('contributor/devref/erd.svg', format='svg')

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.actdiag',
    'sphinxcontrib.seqdiag',
    'sphinxcontrib.nwdiag',
    'sphinx.ext.graphviz',
    'sphinx_feature_classification.support_matrix',
    'openstackdocstheme',
    'oslo_config.sphinxext',
    'oslo_policy.sphinxpolicygen',
    'sphinxcontrib.apidoc'
]

todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
copyright = u'2014, OpenStack Octavia Team'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    '_build',
    'contributor/specs/skeleton.rst',
    'contributor/specs/template.rst'
]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ['octavia.']

# -- Options for man page output ----------------------------------------------
man_pages = []

# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'openstackdocs'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}
html_theme_options = {'show_other_versions': True}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

html_static_path = ['_static']

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Octavia-Specsdoc'


# -- Options for LaTeX output -------------------------------------------------

pdf_theme_path = openstackdocstheme.get_pdf_theme_path('openstackdocs')
openstack_logo = openstackdocstheme.get_theme_logo_path('openstackdocs')

latex_custom_template = r"""
\newcommand{\openstacklogo}{%s}
\usepackage{%s}
""" % (openstack_logo, pdf_theme_path)

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto/manual]).
latex_documents = [(
    'index',
    'Octavia.tex',
    u'Octavia Documentation',
    u'OpenStack Octavia Team',
    'manual'
)]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True

# -- Options for Texinfo output -----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [(
    'index',
    'Octavia-specs',
    u'Octavia Design Specs',
    u'OpenStack Octavia Team',
    'octavia-specs',
    'Design specifications for the Octavia project.',
    'Miscellaneous'
)]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'


# -- Options for Epub output --------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'Octavia Specs'
epub_author = u'OpenStack Octavia Team'
epub_publisher = u'OpenStack Octavia Team'
epub_copyright = u'2014, OpenStack Octavia Team'

# The language of the text. It defaults to the language option
# or en if the language is not set.
# epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
# epub_scheme = ''

# The unique identifier of the text. This can be an ISBN number
# or the project homepage.
# epub_identifier = ''

# A unique identification for the text.
# epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
# epub_cover = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_post_files = []

# A list of files that should not be packed into the epub file.
# epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
# epub_tocdepth = 3

# Allow duplicate toc entries.
# epub_tocdup = True

# RBAC sample policy file generation
policy_generator_config_file = '../../etc/policy/octavia-policy-generator.conf'
sample_policy_basename = 'configuration/_static/octavia'

repository_name = 'openstack/octavia'
bug_project = '908'
bug_tag = 'docs'

apidoc_output_dir = 'contributor/modules'
apidoc_module_dir = '../../octavia'
apidoc_excluded_paths = [
  'tests',
  'db/migration'
]
