#!/usr/bin/env python
# """ Test domainr api wrapper """

from urllib import urlopen
import json
import urllib3
import certifi

__author__ = 'marinashchukina'

domain_name = 'alisa'
link = 'https://domai.nr/api/json/search?&client_id=marinashchukina&q=' + domain_name
http = urllib3.PoolManager()
r = http.request('GET', link)

my_json = json.loads(r.data)
results = my_json['results']

list_available = []
list_unavailable = []
#if results[]

for result in results:
    if result['availability'] == 'taken':
        list_unavailable.append(result['domain'])
    else:
        list_available.append(result['domain'])

print list_available, list_unavailable