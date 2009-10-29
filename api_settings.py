#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Example usage for EBS using Google App Engine SDK.
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

import configuration
from ebs.merchant.data import MODE_PRODUCTION, MODE_DEVELOPMENT
from google.appengine.api import users
from google.appengine.ext import webapp, db
from google.appengine.ext.webapp.util import run_wsgi_app
from util import render_template
from models import BillingSettings

class BillingSettingsHandler(webapp.RequestHandler):
    def get(self):
        test_settings = BillingSettings.get_settings(mode=MODE_DEVELOPMENT)
        production_settings = BillingSettings.get_settings(mode=MODE_PRODUCTION)
        response = render_template('settings.html', settings_saved=False, logout_url=users.create_logout_url('/settings/billing/'), test_settings=test_settings, production_settings=production_settings)
        self.response.out.write(response)

    def post(self):
        test_settings = BillingSettings.get_settings(mode=MODE_DEVELOPMENT)
        test_settings.account_id = self.request.get('test_account_id')
        test_settings.secret_key = self.request.get('test_secret_key')
        production_settings = BillingSettings.get_settings(mode=MODE_PRODUCTION)	        
        production_settings.account_id = self.request.get('production_account_id')
        production_settings.secret_key = self.request.get('production_secret_key')
        db.put([test_settings, production_settings])
        response = render_template('settings.html', settings_saved=True, logout_url=users.create_logout_url('/settings/billing/'), test_settings=test_settings, production_settings=production_settings)            
        self.response.out.write(response)

urls = (
    ('/settings/billing/?', BillingSettingsHandler),
)
application = webapp.WSGIApplication(urls, debug=configuration.DEBUG)

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()

