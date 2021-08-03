.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

.. image:: https://github.com/collective/collective.googlecloudlogging/actions/workflows/plone-package.yml/badge.svg
    :target: https://github.com/collective/collective.googlecloudlogging/actions/workflows/plone-package.yml

.. image:: https://coveralls.io/repos/github/collective/collective.googlecloudlogging/badge.svg?branch=main
    :target: https://coveralls.io/github/collective/collective.googlecloudlogging?branch=main
    :alt: Coveralls

.. image:: https://codecov.io/gh/collective/collective.googlecloudlogging/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/collective/collective.googlecloudlogging

.. image:: https://img.shields.io/pypi/v/collective.googlecloudlogging.svg
    :target: https://pypi.python.org/pypi/collective.googlecloudlogging/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/collective.googlecloudlogging.svg
    :target: https://pypi.python.org/pypi/collective.googlecloudlogging
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/collective.googlecloudlogging.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/collective.googlecloudlogging.svg
    :target: https://pypi.python.org/pypi/collective.googlecloudlogging/
    :alt: License


=============================
collective.googlecloudlogging
=============================

Google Cloud Logging Integration

Description
-----------

This library includes logging handlers to connect Python's standard logging module to Logging, as well as an API client library to access Cloud Logging manually.


Configuration
-------------

- Within Google Cloud no extra configuration should be needed.
- Todo: To use the Cloud Logging library for Python outside of Google Cloud, including running the library on your own workstation, on your data center's computers, or on the VM instances of another cloud provider, you must supply your Google Cloud project ID and appropriate service account credentials directly to the Cloud Logging library for Python.


Documentation
-------------

More information at https://cloud.google.com/logging/docs/setup/python#connecting_the_library_to_python_logging


Requirements
------------

* Plone 5.2
* Python 3.7


Installation
------------

Install collective.googlecloudlogging by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.googlecloudlogging


and then running ``bin/buildout``


Maintainers
-----------

- Peter Holzer

Contact: `dev@bluedynamics.com <mailto:dev@bluedynamics.com>`_


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.googlecloudlogging/issues
- Source Code: https://github.com/collective/collective.googlecloudlogging


License
-------

The project is licensed under the GPLv2.
