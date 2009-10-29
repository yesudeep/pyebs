#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Models for the example integration application.
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

from ebs.merchant.data import MODE_PRODUCTION, MODE_DEVELOPMENT
from google.appengine.api import memcache
from google.appengine.ext import db

MODES = [
    MODE_DEVELOPMENT,
    MODE_PRODUCTION,
]

TRANSACTION_DESCRIPTIONS = [
    'A cat got curious and ended up in heaven.',
    'Man is a social animal. Dogs are social people.',
    'Once upon a time, there was a storyteller who told boring stories to the villagers.  He was stoned--drunk, I mean.',
    'An apple a day keeps the doctor starving.  So go to your doctor today--apples are expensive and doctors are cute.',
]

FIRST_NAMES = [
    'John',
    'David',
    'Paula',
    'Jim',
    'Jane',
    'Windows',
]

LAST_NAMES = [
    'Doe',
    'Jones',
    'Pando',
    'Landy',
    'Shone',
    'Sucks',
]

EMAILS = []
FULL_NAMES = []
for first_name in FIRST_NAMES:
    for last_name in LAST_NAMES:
        FULL_NAMES.append(first_name + ' ' + last_name)
        EMAILS.append(first_name.lower() + '@' + last_name.lower() + '.com')

STATES = [
    'Maharashtra',
    'Kerala',
    'Madhya Pradesh',
    'Himanchal Pradesh',
    'New York',
    'Arunachal Pradesh',
    'Orissa',
    'Karnataka',
    'Tamil Nadu',
    'Gujarat',
    'Assam',
    'Goa',
    'Washington',
    'Utah',
    'California',
    'Idaho',
    'Wyoming',
    'Kentucky',
    'Texas',
]

CITIES = [
    'New York',
    'London',
    'Paris',
    'Mumbai',
    'Tokyo',
    'New Delhi',
    'Chennai',
    'Bengaluru',
    'Kolkata',
    'Bombay',
    'Wagga Wagga',
    'Mori',
    'Sydney',
    'Canberra',
    'Washington DC',
    'Frankfurt',
    'Berlin',
]

POSTAL_ADDRESSES = [
    'Wherever you want us to be man',
    '1-Two Ways, Go Everywhere Building, But Here Street',
    'Anywhere, but here',
    '0x80f4e8a3, In Memory of RAM',
]

COUNTRIES_MAP = {
    u"AFG": u"Afghanistan",
    u"ALA": u"Åland Islands",
    u"ALB": u"Albania",
    u"DZA": u"Algeria",
    u"ASM": u"American Samoa",
    u"AND": u"Andorra",
    u"AGO": u"Angola",
    u"AIA": u"Anguilla",
    u"ATA": u"Antarctica",
    u"ATG": u"Antigua and Barbuda",
    u"ARG": u"Argentina",
    u"ARM": u"Armenia",
    u"ABW": u"Aruba",
    u"AUS": u"Australia",
    u"AUT": u"Austria",
    u"AZE": u"Azerbaijan",
    u"BHS": u"Bahamas",
    u"BHR": u"Bahrain",
    u"BGD": u"Bangladesh",
    u"BRB": u"Barbados",
    u"BLR": u"Belarus",
    u"BEL": u"Belgium",
    u"BLZ": u"Belize",
    u"BEN": u"Benin",
    u"BMU": u"Bermuda",
    u"BTN": u"Bhutan",
    u"BOL": u"Bolivia",
    u"BIH": u"Bosnia and Herzegovina",
    u"BWA": u"Botswana",
    u"BVT": u"Bouvet Island",
    u"BRA": u"Brazil",
    u"IOT": u"British Indian Ocean Territory",
    u"BRN": u"Brunei Darussalam",
    u"BGR": u"Bulgaria",
    u"BFA": u"Burkina Faso",
    u"BDI": u"Burundi",
    u"KHM": u"Cambodia",
    u"CMR": u"Cameroon",
    u"CAN": u"Canada",
    u"CPV": u"Cape Verde",
    u"CYM": u"Cayman Islands",
    u"CAF": u"Central African Republic",
    u"TCD": u"Chad",
    u"CHL": u"Chile",
    u"CHN": u"China",
    u"CXR": u"Christmas Island",
    u"CCK": u"Cocos (Keeling) Islands",
    u"COL": u"Colombia",
    u"COM": u"Comoros",
    u"COG": u"Congo",
    u"COD": u"Congo, Democratic Republic of the",
    u"COK": u"Cook Islands",
    u"CRI": u"Costa Rica",
    u"CIV": u"Cote d'Ivoire Côte d'Ivoire",
    u"HRV": u"Croatia",
    u"CUB": u"Cuba",
    u"CYP": u"Cyprus",
    u"CZE": u"Czech Republic",
    u"DNK": u"Denmark",
    u"DJI": u"Djibouti",
    u"DMA": u"Dominica",
    u"DOM": u"Dominican Republic",
    u"ECU": u"Ecuador",
    u"EGY": u"Egypt",
    u"SLV": u"El Salvador",
    u"GNQ": u"Equatorial Guinea",
    u"ERI": u"Eritrea",
    u"EST": u"Estonia",
    u"ETH": u"Ethiopia",
    u"FLK": u"Falkland Islands (Malvinas)",
    u"FRO": u"Faroe Islands",
    u"FJI": u"Fiji",
    u"FIN": u"Finland",
    u"FRA": u"France",
    u"GUF": u"French Guiana",
    u"PYF": u"French Polynesia",
    u"ATF": u"French Southern Territories",
    u"GAB": u"Gabon",
    u"GMB": u"Gambia",
    u"GEO": u"Georgia",
    u"DEU": u"Germany",
    u"GHA": u"Ghana",
    u"GIB": u"Gibraltar",
    u"GRC": u"Greece",
    u"GRL": u"Greenland",
    u"GRD": u"Grenada",
    u"GLP": u"Guadeloupe",
    u"GUM": u"Guam",
    u"GTM": u"Guatemala",
    u"GGY": u"Guernsey",
    u"GIN": u"Guinea",
    u"GNB": u"Guinea-Bissau",
    u"GUY": u"Guyana",
    u"HTI": u"Haiti",
    u"HMD": u"Heard Island and McDonald Islands",
    u"VAT": u"Holy See (Vatican City State)",
    u"HND": u"Honduras",
    u"HKG": u"Hong Kong",
    u"HUN": u"Hungary",
    u"ISL": u"Iceland",
    u"IND": u"India",
    u"IDN": u"Indonesia",
    u"IRN": u"Iran, Islamic Republic of",
    u"IRQ": u"Iraq",
    u"IRL": u"Ireland",
    u"IMN": u"Isle of Man",
    u"ISR": u"Israel",
    u"ITA": u"Italy",
    u"JAM": u"Jamaica",
    u"JPN": u"Japan",
    u"JEY": u"Jersey",
    u"JOR": u"Jordan",
    u"KAZ": u"Kazakhstan",
    u"KEN": u"Kenya",
    u"KIR": u"Kiribati",
    u"PRK": u"Korea, Democratic People's Republic of",
    u"KOR": u"Korea, Republic of",
    u"KWT": u"Kuwait",
    u"KGZ": u"Kyrgyzstan",
    u"LAO": u"Lao People's Democratic Republic",
    u"LVA": u"Latvia",
    u"LBN": u"Lebanon",
    u"LSO": u"Lesotho",
    u"LBR": u"Liberia",
    u"LBY": u"Libyan Arab Jamahiriya",
    u"LIE": u"Liechtenstein",
    u"LTU": u"Lithuania",
    u"LUX": u"Luxembourg",
    u"MAC": u"Macao",
    u"MKD": u"Macedonia, the former Yugoslav Republic of",
    u"MDG": u"Madagascar",
    u"MWI": u"Malawi",
    u"MYS": u"Malaysia",
    u"MDV": u"Maldives",
    u"MLI": u"Mali",
    u"MLT": u"Malta",
    u"MHL": u"Marshall Islands",
    u"MTQ": u"Martinique",
    u"MRT": u"Mauritania",
    u"MUS": u"Mauritius",
    u"MYT": u"Mayotte",
    u"MEX": u"Mexico",
    u"FSM": u"Micronesia, Federated States of",
    u"MDA": u"Moldova, Republic of",
    u"MCO": u"Monaco",
    u"MNG": u"Mongolia",
    u"MNE": u"Montenegro",
    u"MSR": u"Montserrat",
    u"MAR": u"Morocco",
    u"MOZ": u"Mozambique",
    u"MMR": u"Myanmar",
    u"NAM": u"Namibia",
    u"NRU": u"Nauru",
    u"NPL": u"Nepal",
    u"NLD": u"Netherlands",
    u"ANT": u"Netherlands Antilles",
    u"NCL": u"New Caledonia",
    u"NZL": u"New Zealand",
    u"NIC": u"Nicaragua",
    u"NER": u"Niger",
    u"NGA": u"Nigeria",
    u"NIU": u"Niue",
    u"NFK": u"Norfolk Island",
    u"MNP": u"Northern Mariana Islands",
    u"NOR": u"Norway",
    u"OMN": u"Oman",
    u"PAK": u"Pakistan",
    u"PLW": u"Palau",
    u"PSE": u"Palestinian Territory, Occupied",
    u"PAN": u"Panama",
    u"PNG": u"Papua New Guinea",
    u"PRY": u"Paraguay",
    u"PER": u"Peru",
    u"PHL": u"Philippines",
    u"PCN": u"Pitcairn",
    u"POL": u"Poland",
    u"PRT": u"Portugal",
    u"PRI": u"Puerto Rico",
    u"QAT": u"Qatar",
    u"REU": u"Reunion Réunion",
    u"ROU": u"Romania",
    u"RUS": u"Russian Federation",
    u"RWA": u"Rwanda",
    u"BLM": u"Saint Barthélemy",
    u"SHN": u"Saint Helena",
    u"KNA": u"Saint Kitts and Nevis",
    u"LCA": u"Saint Lucia",
    u"MAF": u"Saint Martin (French part)",
    u"SPM": u"Saint Pierre and Miquelon",
    u"VCT": u"Saint Vincent and the Grenadines",
    u"WSM": u"Samoa",
    u"SMR": u"San Marino",
    u"STP": u"Sao Tome and Principe",
    u"SAU": u"Saudi Arabia",
    u"SEN": u"Senegal",
    u"SRB": u"Serbia",
    u"SYC": u"Seychelles",
    u"SLE": u"Sierra Leone",
    u"SGP": u"Singapore",
    u"SVK": u"Slovakia",
    u"SVN": u"Slovenia",
    u"SLB": u"Solomon Islands",
    u"SOM": u"Somalia",
    u"ZAF": u"South Africa",
    u"SGS": u"South Georgia and the South Sandwich Islands",
    u"ESP": u"Spain",
    u"LKA": u"Sri Lanka",
    u"SDN": u"Sudan",
    u"SUR": u"Suriname",
    u"SJM": u"Svalbard and Jan Mayen",
    u"SWZ": u"Swaziland",
    u"SWE": u"Sweden",
    u"CHE": u"Switzerland",
    u"SYR": u"Syrian Arab Republic",
    u"TWN": u"Taiwan, Province of China",
    u"TJK": u"Tajikistan",
    u"TZA": u"Tanzania, United Republic of",
    u"THA": u"Thailand",
    u"TLS": u"Timor-Leste",
    u"TGO": u"Togo",
    u"TKL": u"Tokelau",
    u"TON": u"Tonga",
    u"TTO": u"Trinidad and Tobago",
    u"TUN": u"Tunisia",
    u"TUR": u"Turkey",
    u"TKM": u"Turkmenistan",
    u"TCA": u"Turks and Caicos Islands",
    u"TUV": u"Tuvalu",
    u"UGA": u"Uganda",
    u"UKR": u"Ukraine",
    u"ARE": u"United Arab Emirates",
    u"GBR": u"United Kingdom",
    u"USA": u"United States",
    u"UMI": u"United States Minor Outlying Islands",
    u"URY": u"Uruguay",
    u"UZB": u"Uzbekistan",
    u"VUT": u"Vanuatu",
    u"VEN": u"Venezuela",
    u"VNM": u"Viet Nam",
    u"VGB": u"Virgin Islands, British",
    u"VIR": u"Virgin Islands, U.S.",
    u"WLF": u"Wallis and Futuna",
    u"ESH": u"Western Sahara",
    u"YEM": u"Yemen",
    u"ZMB": u"Zambia",
    u"ZWE": u"Zimbabwe",
}

COUNTRIES_TUPLE_MAP = [(code,name) for code, name in COUNTRIES_MAP.iteritems()]
def compare_countries(c1, c2):
    if c1[1] < c2[1]:
        return -1
    elif c1[1] > c2[1]:
        return 1
    else:
        return 0
COUNTRIES_TUPLE_MAP.sort(cmp=compare_countries)

# Models
class BillingSettings(db.Model):
    """
    Billing settings for EBS.
    """
    mode = db.StringProperty(choices=MODES)
    account_id = db.StringProperty()
    secret_key = db.StringProperty()

    @classmethod
    def get_settings(cls, mode=MODE_PRODUCTION):
        """
        Given a deployment mode returns the first available settings object
        for that mode.  When not given any arguments, it will attempt to 
        return the production mode settings object.
        """
        cache_key = 'BillingSettings.get_settings: ' + mode
        settings = memcache.get(cache_key)
        if not settings:
            settings = db.Query(BillingSettings).filter("mode =", mode).get()
            if not settings:
                settings = BillingSettings(mode=mode)
                settings.put()
            memcache.set(cache_key, settings, 120)
        return settings

class BillingTransaction(db.Model):
    """
    Transaction object that stores all responses obtained from EBS.
    """
    response = db.TextProperty()
