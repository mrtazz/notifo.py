# encoding: utf-8

from notifo import Notifo

__author__ = "Daniel Schauenberg"
__version__ = "0.3.0"
__license__ = "MIT"

def send_notification(login, pw, to=None, msg=None, label=None,
                      title=None, uri=None):
    return Notifo(login, pw).send_notification(to,msg,label,title,uri)

def subscribe_user(login, pw, user):
    return Notifo(login, pw).subscribe_user(user)

def send_message(login, pw, to, msg):
    return Notifo(login, pw).send_message(to, msg)
