#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Configuration module
# Copyright (C) 2009  Yesudeep Mangalapilly.
#
# The MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os

# Debug mode.
DEBUG = True

# Store this configuration in the datastore, never in your code.
# Use memcached for fast read-access to avoid hitting the datastore.
EBS_ACCOUNT_ID = '2349'
EBS_SECRET_KEY = 'ebskey'

# Enable the following secure URL for the actual integration.
#EBS_SECURE_URL = 'https://secure.ebs.in/pg/ma/sale/pay/'
EBS_SECURE_URL = '/ebs/'

EBS_SUPPORT_EMAIL = 'support@ebs.in'
EBS_SUPPORT_URL = 'http://support.ebs.in'

SERVER_PORT = os.environ['SERVER_PORT']
SERVER_NAME = os.environ['SERVER_NAME']

if SERVER_PORT and SERVER_PORT != '80':
    HOST_NAME = '%s:%s' % (SERVER_NAME, SERVER_PORT)
    MINIFIED = ''
else:
    HOST_NAME = SERVER_NAME
    MINIFIED = '-min'

# Media URL for use with templates.
MEDIA_URL = "http://%s/s/" % (HOST_NAME, )

BILLING_RETURN_URL = "http://%s/billing?DR={DR}" % (HOST_NAME, )

# Template builtins.
TEMPLATE_BUILTINS = {
    'DEBUG': DEBUG,
    'HOST_NAME': HOST_NAME,
    'MEDIA_URL': MEDIA_URL,
    'TEMPLATE_DEBUG': DEBUG,
    'BILLING_RETURN_URL': BILLING_RETURN_URL,
    'MINIFIED': MINIFIED,
}

