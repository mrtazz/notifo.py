# encoding: utf-8

""" notifo.py - python wrapper for notifo.com """

try:
  import json
except ImportError:
  try:
    import simplejson as json
  except ImportError:
    # For Google AppEngine
    from django.utils import simplejson as json

import urllib
import urllib2
from base64 import encodestring

class Notifo:
    """ Class for wrapping notifo.com """
    def __init__(self, user, secret):
        self.user = user
        self.secret = secret
        self.root_url = "https://api.notifo.com/v1/"

    def subscribe_user(self, user):
        """ method to subscribe a user to a service
        """
        url = self.root_url + "subscribe_user"
        values = {}
        values["username"] = user
        return self._query(url, values)

    def send_notification(self, to=None, msg=None, label=None,
                          title=None, uri=None):
        """ method to send a message to a user

            Parameters:
                to -> recipient
                msg -> message to send
                label -> application description
                title -> name of the notification event
                uri -> callback uri
        """
        url = self.root_url + "send_notification"
        values = {}
        if to is not None:
            values["to"] = to
        if msg is not None:
            values["msg"] = msg
        if label is not None:
            values["label"] = label
        if title is not None:
            values["title"] = title
        if uri is not None:
            values["uri"] = uri
        return self._query(url, values)

    def send_message(self, to=None, msg=None):
        """ method to send a message to a user

            Parameters:
                to -> recipient
                msg -> message to send
        """
        url = self.root_url + "send_message"
        values = {}
        if to is not None:
            values["to"] = to
        if msg is not None:
            values["msg"] = msg
        return self._query(url, values)


    def _query(self, url, data = None):
        """ query method to do HTTP POST/GET

            Parameters:
                url -> the url to POST/GET
                data -> header_data as a dict (only for POST)

            Returns:
                Parsed JSON data as dict
                or
                None on error
        """
        auth = encodestring('%s:%s' % (self.user, self.secret)).replace('\n', '')

        if data is not None: # we have POST data if there is data
            values = urllib.urlencode(data)
            request = urllib2.Request(url, values)
            request.add_header("Authorization", "Basic %s" % auth)
        else: # do a GET otherwise
            request = urllib2.Request(url)
            request.add_header("Authorization", "Basic %s" % auth)
        try:
            response = urllib2.urlopen(request)
        except IOError, e: # no connection
            return {"status" : "error",
                    "response_code" : e.code,
                    "response_message" : e.msg
                   }
        return json.loads(response.read())

