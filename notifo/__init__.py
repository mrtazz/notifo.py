# -*- coding: utf-8 -*-
"""
    __init__.py
    ~~~~~~~~~~~
    API export for notifo.py
"""

from notifo import Notifo

__author__ = "Daniel Schauenberg"
__version__ = "0.3.0"
__license__ = "MIT"

def send_notification(login, pw, to=None, msg=None, label=None,
                      title=None, uri=None):
    """ exported API function to send notifications

    Arguments (all exptected as strings):
        - login: notifo account name
        - pw: notifo API secret
        - to: account name to send the notification to
        - msg: content body of the notification
        - label: label for the notification
        - title: title of the notification
        - uri: callback uri

    Returns:
        A dict containing the parsed response or error descriptions

    """
    return Notifo(login, pw).send_notification(to, msg, label, title, uri)

def subscribe_user(login, pw, user):
    """ exported API function to subscribe a user to a service

    Arguments (all exptected as strings):
        - login: notifo service provider account name
        - pw: notifo service account API token
        - user: user to subscribe to the service

    Returns:
        A dict containing the parsed response or error descriptions

    """
    return Notifo(login, pw).subscribe_user(user)

def send_message(login, pw, to, msg):
    """ exported API function to send a message to a user

    Arguments (all exptected as strings):
        - login: notifo account name
        - pw: notifo API secret
        - to: recipient to send the message to
        - msg: message content to send

    Returns:
        A dict containing the parsed response or error descriptions

    """
    return Notifo(login, pw).send_message(to, msg)
