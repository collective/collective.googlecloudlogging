=============================
collective.googlecloudlogging
=============================

This library connects to Python's standard logging module and will log to Googles Cloud Logging via API. More information at https://cloud.google.com/logging/docs/setup/python#connecting_the_library_to_python_logging

Configuration
-------------

- Within Google Cloud no extra configuration should be needed.
- If you want to use the Cloud Logging outside of Google Cloud, you have to supply your Google Cloud project ID and appropriate service account credentials.

Note
----

As soon as it's loaded, and only then, it will remove the StreamHandler from root logger and no longer write to stdout.
If you want no instance logging to stdout at all in your Google Cloud Logs, you have to disable it in your ``wsgi.ini``::


    [logger_root]
    level = INFO
    handlers = console, eventlog


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


For Python 2.7.x
----------------

You can try with these version pinnings::

    google_cloud_logging = 1.15.1
    pyasn1_modules = 0.2.8
    rsa = 4.5
    googleapis_common_protos = 1.53.0
    packaging = 21.0
    protobuf = 3.17.3
    grpcio = 1.39.0
    google_auth = 1.34.0
    google_api_core = 1.31.1
    google_cloud_core = 1.7.2


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
