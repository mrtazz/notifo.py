============
notifo.py
============

Introduction
=============
notifo.py is a python library for the notifo.com_ notification service.

Installation
=============
Install via pip::

    pip install notifo

Or if you must::

    easy_install notifo


Usage
======
notifo.py can be imported into any python module::

    import notifo

    notifo.send_notification(login, token, recipient, msg, label, title, uri)
    notifo.subscribe_user(login, token, user)

Return data is the parsed json status code::

    {u'status': u'success', u'response_code': 2201, u'response_message': u'OK'}

.. _notifo.com: http://notifo.com
