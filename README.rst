GitHub repo for the NESE RTD site
=======================================

This GitHub repo contains the sources for the Read the Docs hosted
`NESE documentation website <https://nesedev.readthedocs.io/>`_

Resources:
----------
* `Read the Docs website <https://readthedocs.org>`_
* `NESE documentation website <https://nesedev.readthedocs.io/>`_
* `Docutil's authoritative reStructuredText reference <https://docutils.sourceforge.io/rst.html>`_
* `Sphinx's RST Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
* `Sphinx's RST Cheatsheet <https://sphinx-tutorial.readthedocs.io/cheatsheet/>`_
* `Alternative RST Cheatsheet <https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst>`_

Installing the Sphinx and RTD toolchain:
----------------------------------------

Sphinx and the RTD Sphinx theme can be installed using pip, conda, or brew (for Mac users).
In this example, we will use conda and assume miniconda is installed.

#. Clone the RTD-NESE git repo

	$ git clone git@github.com:mghpcsim/rtd-nese.git

#. Use the conda-generated environment.yml file to create your environment

	$ cd rtd-nese
        
	$ conda env create -f environment.yml

#. Whenever you need to build RTD-hosted documentation, first load the rtd environment

	$ conda activate rtd


**Note:** If you already have a conda environment named "rtd" or prefer a different name, use the -n option

	$ conda env create -n myname -f environment.yml

Previewing Changes Before Commiting
-----------------------------------

After you've made local changes to the documentation, please build and view before
checking in changes or submitting a PR.

* Change paths to the top level of the documentation 

	$ cd /path/to/git/rtd-nese/docs

* Build the documentation

	$ make html

* View the documentation in $PWD/build/docs/index.html

	$ open build/html/index.html  # works on a mac; use xdg-open on linux

* To see all build options, use `make help`::

	(rtd) csim@gedanken docs % make help
	Sphinx v5.0.2
	Please use `make target' where target is one of
  	html        to make standalone HTML files
  	dirhtml     to make HTML files named index.html in directories
  	singlehtml  to make a single large HTML file
  	pickle      to make pickle files
  	json        to make JSON files
  	htmlhelp    to make HTML files and an HTML help project
  	qthelp      to make HTML files and a qthelp project
  	devhelp     to make HTML files and a Devhelp project
  	epub        to make an epub
  	latex       to make LaTeX files, you can set PAPER=a4 or PAPER=letter
  	latexpdf    to make LaTeX and PDF files (default pdflatex)
  	latexpdfja  to make LaTeX files and run them through platex/dvipdfmx
  	text        to make text files
  	man         to make manual pages
  	texinfo     to make Texinfo files
  	info        to make Texinfo files and run them through makeinfo
  	gettext     to make PO message catalogs
  	changes     to make an overview of all changed/added/deprecated items
  	xml         to make Docutils-native XML files
  	pseudoxml   to make pseudoxml-XML files for display purposes
  	linkcheck   to check all external links for integrity
  	doctest     to run all doctests embedded in the documentation (if enabled)
  	coverage    to run coverage check of the documentation (if enabled)
  	clean       to remove everything in the build directory

Live Preview of Changes
-----------------------------------

If you'd like to automatically rebuild your local docs and view the changes,
use the "sphinx-reload" package. 

#. Activate your RTD conda environment

	$ conda activate rtd

#. Install the "sphinx-reload" package via pip

	$ pip install sphinx-reload

#. Navigate to the top level of your rtd-nese git repo checkout and start the server

	$ cd /path/to/git/rtd-nese

	$ sphinx-reload docs/

This will spawn a webserver on port 5500 and should open your default web browser and
navigate to this site. As changes are made to any .rst file under the docs directory,
the website will automatically be rebuilt and refreshed.



