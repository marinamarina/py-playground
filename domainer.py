#!/usr/bin/env python
""" Python wrapper for the Domainr API
    https://domai.nr/
"""

from urllib import urlopen
import json
import urllib3
import certifi
import re

__author__ = 'marinashchukina'

class DomainWrapper:

    #domain_name=''
    __list_available=[]
    __list_unavailable=[]

    def __init__(self,  domain_name='alisa'):
        self.domain_name = domain_name
        self.link = 'https://domai.nr/api/json/search?&client_id=marinashchukina&q=' + domain_name

    def load_json(self):
        http = urllib3.PoolManager()
        r = http.request('GET', self.link)
        my_json = json.loads(r.data)

        # escape unicode characters in the output
        #escaped_json = re.sub(r'u.*$',my_json, re.M|re.I)
        return my_json['results']

    def load_lists(self):
        results = self.load_json()

        for result in results:
            if self.domain_name not in result['domain']:
                continue

            if result['availability'] == 'taken':
                self.__list_unavailable.append(result['domain'])
            else:
                self.__list_available.append(result['domain'])

    def printLists(self):
        self.load_lists()
        print self.__list_available, self.__list_unavailable

# Example usage
domainer = DomainWrapper('alisa')
domainer.printLists()