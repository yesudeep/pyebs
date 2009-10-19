#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Example usage for EBS using web.py
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

from base64 import urlsafe_b64encode, b64encode
from datetime import datetime
from decimal import Decimal
from ebs.merchant.api import get_ebs_request_parameters, arc4_encrypt
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from pprint import pformat
from util import ebs_urlencode, render_template
from models import MODES, COUNTRIES_TUPLE_MAP, TRANSACTION_DESCRIPTIONS, FULL_NAMES, EMAILS, STATES, CITIES, POSTAL_ADDRESSES

import logging
import random


# Set up logging.
logging.basicConfig(level=logging.DEBUG)


class IndexHandler(webapp.RequestHandler):
    """
    Payment page handler.
    """
    def get(self):
        rendered_response_text = render_template('index.html',
            account_id=configuration.EBS_ACCOUNT_ID,
            amount=Decimal(str(random.randint(1000, 40000)) + '.' + str(random.randint(10, 100))),
            billing_return_url=configuration.BILLING_RETURN_URL,
            city=random.choice(CITIES),
            countries=COUNTRIES_TUPLE_MAP,
            country_code=random.choice(COUNTRIES_TUPLE_MAP)[0],
            description=random.choice(TRANSACTION_DESCRIPTIONS),
            ebs_secure_url=configuration.EBS_SECURE_URL,
            ebs_support_email=configuration.EBS_SUPPORT_EMAIL,
            ebs_support_url=configuration.EBS_SUPPORT_URL,
            email=random.choice(EMAILS),
            full_name=random.choice(FULL_NAMES),
            modes=MODES,
            phone_number=random.randint(9800000000, 9899999999),
            postal_address=random.choice(POSTAL_ADDRESSES),
            postal_code=random.randint(400000, 500000),
            reference_number=random.randint(400000, 600000),
            state_province=random.choice(STATES),
            )
        self.response.out.write(rendered_response_text)

class PaymentGatewayEmulationHandler(webapp.RequestHandler):
    """
    Emulates the payment gateway to ease simple testing.
    """
    def post(self):
        return_url = self.request.get('return_url')
        now_string = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        amount = self.request.get('amount')
        if not '.' in amount:
            # Make sure the amount contains the fractional part.
            amount = amount + '.00'

        dr = {
            'Amount': Decimal(amount),
            'BillingAddress': self.request.get('address'),
            'BillingCity': self.request.get('city'),
            'BillingCountry': self.request.get('country'),
            'BillingEmail': self.request.get('email'),
            'BillingName': self.request.get('name'),
            'BillingPhone': self.request.get('phone'),
            'BillingPostalCode': self.request.get('postal_code'),
            'BillingState': self.request.get('state'),
            'DateCreated': now_string,
            'DeliveryAddress': '',
            'DeliveryCity': '',
            'DeliveryCountry': '',
            'DeliveryName': '',
            'DeliveryPhone': '',
            'DeliveryPostalCode': '',
            'DeliveryState': '',
            'Description': self.request.get('description'),
            'IsFlagged': 'NO',
            'MerchantRefNo': self.request.get('reference_no'),
            'Mode': self.request.get('mode'),
            'PaymentID': random.randint(400000, 600000),
            'ResponseCode': 0,
            'ResponseMessage': 'Transaction Successful',
        }
        query_string = ebs_urlencode(dr)
        cipher_text = arc4_encrypt(configuration.EBS_SECRET_KEY, query_string)
        encoded_data = b64encode(cipher_text).replace('+', ' ')
        return_url = return_url.replace('{DR}', encoded_data)
        self.redirect(return_url)

class BillingHandler(webapp.RequestHandler):
    """
        Billing transaction response handler.

        EBS sends DR data to this handler which you can use to check for a
        successful transaction and record it such in the datastore.
    """
    def get(self):
        dr = self.request.get('DR')
        self.response.out.write(pformat(get_ebs_request_parameters(dr, configuration.EBS_SECRET_KEY)))

urls = (
    ('/?', IndexHandler),
    ('/billing/?', BillingHandler),
    ('/ebs/?', PaymentGatewayEmulationHandler),
)
application = webapp.WSGIApplication(urls, debug=configuration.DEBUG)

def main():
    run_wsgi_app(application)

def console_test():
    example_dr = """IXc9laP5EPzkG8rJUEkT9GPYZKb 340d1KINeq1DJAbrqc5GeRs3RVwRJ7YShbNZUyaxTmSW46lexsfKVHpZGaEckYB9n5xHvzoFUm9WU7C3Zs6VjHu125hgs12 1Ql5ikbYxNp4M9405id0 WGoo3a3Um6pCSGxHsvDbFVY4FjMIc/QajmES ZhD9RUNn7jfjLth7D179a99uCJlqLeqmWgTM3nILZcwZHDqUWGoYWYb8D4SBHgUupPF8yXSLe6hK0iZoYwd5BkV ujpqJBmlt8oZlTnzL6Fw4sTh3s9YckZQJSGCZ5kk13SccBonrx4mugpFJ3NGJcw1P1CWlSbD8CfrcfVtUFne1YkbhvvzG33w0pMdg0CzdksGoTa0K JYR73gMtNIC PLN8wx4dObf4KADjyFc/G17i7VIsyKI0SdY11VUEVL5JrKa1cBTziaYxlawWOyG0J0wblnZus7a8OVu04aX7g7FIWDXMDmBWsuyaBg5znjJj5At4Q0zdlIzrJ8iopQcaDICu2G5koJVv3HOaTigJ nXm7J6OzlZoY9Ke4eizkHXW8NWVMMrG/p YHLF9kRK1zHYuRBGS3HYOmjXwTW1qJ cTQ6zlXCUzjbZm7rzAHtmuaOWly0iN0kTM4mNY XziWeWyzeo0UjT7GC2ObGrRc4BVUW Fb/L9Zgx3aJMWQICzk1Hj78alALUqZJR8RafT7A=="""
    flattened_params = get_ebs_request_parameters(example_dr, configuration.EBS_SECRET_KEY, flatten_values=True, typed_values=True)
    print flattened_params

if __name__ == '__main__':
    main()

