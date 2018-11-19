#!/usr/bin/env python

import requests
from requests_oauthlib import OAuth1
import time

CLIENT_KEY = u'REDACTED'
CLIENT_SECRET = u'REDACTED'
BASE_URL = u'https://api.projectplace.com/'
access_token_key = u'REDACTED'
access_token_secret = u'REDACTED'

oauth = OAuth1(CLIENT_KEY, client_secret=CLIENT_SECRET, resource_owner_key=access_token_key,
              resource_owner_secret=access_token_secret)
ts = time.time()
r = requests.get(url=BASE_URL + '1/boards/465262/cards', auth=oauth)
te = time.time()
print "Fetched %d cards in %f seconds" % (len(r.json()), te-ts)