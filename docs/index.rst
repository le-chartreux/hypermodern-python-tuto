The Hypermodern Python Project
==============================

.. toctree::
   :hidden:
   :maxdepth: 1

   license
   reference


The example project for the
`Hypermodern Python <https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769>`_
article series.
The command-line interface prints random facts to your console,
using the `Wikipedia API <https://en.wikipedia.org/api/rest_v1/#/>`_.


Installation
------------

To install the Hypermodern Python project,
run this command in your terminal:

.. code-block:: console

   $ pip install hypermodern-python-tuto


Usage
-----

Hypermodern Python's usage looks like:

.. code-block:: console

   $ hypermodern-python-tuto [OPTIONS]

.. option:: --language [french|english|other]

   The Wikipedia language edition,
   as identified by its subdomain on
   `wikipedia.org <https://www.wikipedia.org/>`_.
   By default, the system preferred language is used, with English as fallback if not among supported languages.

.. option:: --version

   Show the version and exit.

.. option:: --help

   Display a short usage message and exit.
