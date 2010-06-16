# encoding: utf-8

from notifo import Notifo

__author__ = "Daniel Schauenberg"
__version__ = "0.1.0"
__license__ = "MIT"

def send_notification(login, pw, **kwargs):
    return Notifo(login, pw).send_notification(**kwargs)

def subscribe_user(login, pw, user):
    return Notifo(login, pw).subscribe_user(user)
