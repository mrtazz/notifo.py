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

	from notifo import Notifo

	# create a Notifo object
	notifo = Notifo('username','apikey') #fill in your username and api key here

	# Tell your object to send a notification
	notifo.send_notification('to','Message','label','title','uri') #fill in your username

	# Successful Transmission response
	# Return data is the parsed json status code::
	
	{u'status': u'success', u'response_code': 2201, u'response_message': u'OK'}

	# Examples of all three methods.
	
    notifo.send_notification(recipient, msg, label, title, uri)
    notifo.send_message(to, msg)
    notifo.subscribe_user(user)

	
There is also a cli client included::

    notifo_cli.py -u user -s secret -n name [-m] [-l label] [-t title] [-c callback] [TEXT]

Contribute
===========
If you want to contribute:

* Fork the project.
* Make your feature addition or bug fix.
* Add tests for it. This is important so I don’t break it in a future version unintentionally.
* Commit, do not mess with version
* Send me a pull request. Bonus points for topic branches.

.. _notifo.com: http://notifo.com
