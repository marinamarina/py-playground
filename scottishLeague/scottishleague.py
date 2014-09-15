#!/usr/bin/env python

import re
import sys
from urllib import urlopen
from urlparse import urlparse
from bs4 import BeautifulSoup

url = "http://eurorivals.net/tables/scotland.html"
team = sys.argv[1]
html = urlopen(url).read()
soup = BeautifulSoup(html)

for row in soup.find_all('tr', {'style': 'height:20px;'}):
    club_name = row.findChildren()[1].findChildren()[0].findChildren()[0].renderContents().strip(" \t")
    if club_name == team:
        print "Home wins: %s " % row.findChildren()[1].findChildren()[5].renderContents().strip(" \t")