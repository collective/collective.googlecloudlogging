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

This library connects to Python's standard logging module will log to Googles Cloud Logging via API.
Note: As soon as it's loaded, and only then, it will remove the StreamHandler from root logger and no longer write to stdout.
If you want no stdout at all in your Google Cloud Logs, you have to disable it in your `wsgi.ini`

```
[logger_root]
level = INFO
handlers = console, eventlog
```

Configuration
-------------

- Within Google Cloud no extra configuration should be needed.
- If you want to use the Cloud Logging outside of Google Cloud, you have to supply your Google Cloud project ID and appropriate service account credentials.


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
