#!/usr/bin/env python
""" Python wrapper for the Domainr API
    https://domai.nr/
    version = 0.0.1
    TODO: escape the unicode char
          add certificate
"""

from urllib import urlopen
import json
import urllib3
import certifi
import re

class DomainWrapper:
    'Python Domainr API wrapper, returns a list of available/inavailable domains with a searched name'

    def __init__(self,  client_id='marinashchukina', domain_name='google'):
        self.client_id = client_id
        self.domain_name = domain_name
        self.link = 'https://domai.nr/api/json/search?&client_id=%s&q=%s' % (self.client_id, self.domain_name)
        self._list_available = None
        self._list_unavailable = None

    def load_json(self):
        '''Load the json'''

        http = urllib3.PoolManager()
        r = http.request('GET', self.link)
        my_json = json.loads(r.data)

        # escape unicode characters in the output
        #escaped_json = re.sub(r'u.*$',my_json, re.M|re.I)
        return my_json['results']

    def load_lists(self):
        '''assign values to the availability lists'''

        self._list_available = []
        self._list_unavailable = []

        results = self.load_json()

        for result in results:

            # only interested in domains containing the searched word
            if self.domain_name not in result['domain']:
                continue

            if result['availability'] == 'taken':
                self._list_unavailable.append(result['domain'])
            else:
                self._list_available.append(result['domain'])

    @property
    def list_available(self):
        if not self._list_available:
            print 'Retrieving the result only for you, %username%...'
            self.load_lists()
        return self._list_available

    @property
    def list_unavailable(self):
        if not self._list_unavailable:
            print 'Retrieving the result only for you, %username%...'
            self.load_lists()
        return self._list_unavailable

# Example usage
import os

domainer = DomainWrapper(os.environ.get('DOMAINR_CLIENT_ID'), 'google')
#print domainer.list_available, list_unavailable

# Testing higher speed of retrieving results when using properties

import time

domainer = DomainWrapper(os.environ.get('DOMAINR_CLIENT_ID'), 'google')
startTime = time.time()
list_of_available_domains1 = domainer.list_available
print "Amount of time needed to load the lists:", (time.time() - startTime)

startTime = time.time()
list_of_available_domains2 = domainer.list_available
print "Amount of time needed to access the property: ", (time.time() - startTime)

print ("Is the content the same? %r" % (list_of_available_domains1 == list_of_available_domains2))

print list_of_available_domains1