#!/usr/bin/env python
# encoding: utf-8

""" executable to interact with notifo.com using the notifo.py library """

import notifo
from optparse import OptionParser


def init_parser():
    """ function to init option parser """
    usage = "usage: %prog -u user -s secret -n name [-l label] \
[-t title] [-c callback] [TEXT]"

    parser = OptionParser(usage, version="%prog " + notifo.__version__)
    parser.add_option("-u", "--user", action="store", dest="user",
                      help="your notifo username")
    parser.add_option("-s", "--secret", action="store", dest="secret",
                      help="your notifo API secret")
    parser.add_option("-n", "--name", action="store", dest="name",
                      help="recipient for the notification")
    parser.add_option("-l", "--label", action="store", dest="label",
                      help="label for the notification")
    parser.add_option("-t", "--title", action="store", dest="title",
                      help="title of the notification")
    parser.add_option("-c", "--callback", action="store", dest="callback",
                      help="callback URL to call")

    (options, args) = parser.parse_args()
    return (parser, options, args)

def main():
    """ main function """
    # get options and arguments
    (parser, options, args) = init_parser()

    # initialize result variable
    result = None

    # check for values which are always needed
    if not options.user:
        parser.error("No user given.")
    if not options.secret:
        parser.error("No API secret given.")
    if not options.name:
        parser.error("No recipient given.")

    # If there is no message, we probably want to subscribe a user
    if len(args) < 1:
        result = notifo.subscribe_user(options.user, options.secret, options.name)
    else:
        params = {}
        params["to"] = options.name
	m = ''
	for a in args:
		m = "%s %s" %(m, a)
        params["msg"] = m
        if options.label:
            params["label"] = options.label
        if options.title:
            params["title"] = options.title
        if options.callback:
            params["uri"] = options.callback

        # send notification
        result = notifo.send_notification(options.user,
                                          options.secret,
                                          **params)

    if result is None:
        print "Something went wrong. Check parameters and try again."

if __name__ == '__main__':
    main()

