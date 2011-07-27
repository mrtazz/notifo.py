.. notifo.py documentation master file, created by

notifo.py: python API wrapper for notifo.com
=========================================================

Contents:

.. toctree::
   :maxdepth: 2

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Quickstart
-----------
notifo.py is a python client for the notifo.com API. It supports subscribing
users to a service and sending notifications and messages::

    import notifo

    notifo.send_notification(login, token, recipient, msg, label, title, uri)
    notifo.send_message(login, token, to, msg)
    notifo.subscribe_user(login, token, user)

Return data is the parsed json status code::

    {u'status': u'success', u'response_code': 2201, u'response_message': u'OK'}

There is also a cli client included::

    notifo_cli.py -u user -s secret -n name [-m] [-l label] [-t title] [-c callback] [TEXT]



API Reference
-------------

If you are looking for information on a specific function, class or
method, you can most likely find it here.

.. toctree::
   :maxdepth: 2

   api
