#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Utility functions.

import configuration

from google.appengine.ext import webapp
from google.appengine.ext.webapp.template import render
from urllib import urlencode, _is_unicode, quote as quote_plus
from appengine_utilities.sessions import Session
import sys


class SessionRequestHandler(webapp.RequestHandler):
    """
    A SessionRequestHandler handler contains information about
    the current session.  It depends on the appengine_utilities.sessions
    package to maintain a session.
    """
    def __init__(self):
        webapp.RequestHandler.__init__(self)
        self.session = Session()
        if not 'ebs_mode' in self.session:
            self.session['ebs_mode'] = configuration.EBS_MODE


def render_template(template_name, **values):
    """
        Render a template given its filename from the templates/ directory.
    """
    context = configuration.TEMPLATE_BUILTINS
    context.update(values)
    return render('templates/' + template_name, context)


def ebs_urlencode(query,doseq=0):
    """Encode a sequence of two-element tuples or dictionary into a URL query string.

    If any values in the query arg are sequences and doseq is true, each
    sequence element is converted to a separate parameter.

    If the query arg is a sequence of two-element tuples, the order of the
    parameters in the output will match the order of parameters in the
    input.

    This is different from the Python version in urllib as it uses quote instead
    of quote_plus for compatibility with the EBS payment gateway.
    """

    if hasattr(query,"items"):
        # mapping objects
        query = query.items()
    else:
        # it's a bother at times that strings and string-like objects are
        # sequences...
        try:
            # non-sequence items should not work with len()
            # non-empty strings will fail this
            if len(query) and not isinstance(query[0], tuple):
                raise TypeError
            # zero-length sequences of all types will get here and succeed,
            # but that's a minor nit - since the original implementation
            # allowed empty dicts that type of behavior probably should be
            # preserved for consistency
        except TypeError:
            ty,va,tb = sys.exc_info()
            raise TypeError, "not a valid non-string sequence or mapping object", tb

    l = []
    if not doseq:
        # preserve old behavior
        for k, v in query:
            k = quote_plus(str(k))
            v = quote_plus(str(v))
            l.append(k + '=' + v)
    else:
        for k, v in query:
            k = quote_plus(str(k))
            if isinstance(v, str):
                v = quote_plus(v)
                l.append(k + '=' + v)
            elif _is_unicode(v):
                # is there a reasonable way to convert to ASCII?
                # encode generates a string, but "replace" or "ignore"
                # lose information and "strict" can raise UnicodeError
                v = quote_plus(v.encode("ASCII","replace"))
                l.append(k + '=' + v)
            else:
                try:
                    # is this a sufficient test for sequence-ness?
                    x = len(v)
                except TypeError:
                    # not a sequence
                    v = quote_plus(str(v))
                    l.append(k + '=' + v)
                else:
                    # loop over the sequence
                    for elt in v:
                        l.append(k + '=' + quote_plus(str(elt)))
    return '&'.join(l)

