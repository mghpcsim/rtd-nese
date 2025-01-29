# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Project NESE'
copyright = '2023, Team NESE'
author = 'csim'

release = '0.1'
version = '0.1.0'

# -- General configuration 

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'notfound.extension',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'


# -- Options for EPUB output
epub_show_urls = 'footnote'

# notfound.extension custom 404 page to allow nesedev -> nese
notfound_context = {
        'title': 'NESE Documentation has been Moved',
        'body': "<h1>NESE Documentation Relocated on ReadTheDocs</h1>\n\nDocumentation for the NESE, the Northeast Storage Exchange, has been moved to a new ReadTheDocs page.\n\nYou can update your bookmarks by changing <em>nesedev.readthedocs.io</em> with <em>nese.readthedocs.io</em>."
}

