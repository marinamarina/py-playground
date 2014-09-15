#! /usr/bin/env python

import re
import sys
from urllib import urlopen
from urlparse import urlparse

LINK_REGEX = re.compile(
           "<a [^>]*href=['\"]([^'\"]+)['\"][^>]*>")

class LinkCollector:

    def __init__(self, url):
        'passing the base url'
        self.url = "http://%s" % urlparse('http://' + url).netloc
        self.collected_links = set()
        self.visited_links = set()

    def normalize_url(self, path, link):
        'This method converts all URLs to complete URLs with protocol and hostname.'
        if link.startswith("http://"):
            return link
        elif link.startswith("/"):
            return self.url + link
        else:
            return self.url + path.rpartition('/')[0] + '/' + link

    def collect_links(self, path='/'):
        full_url = self.url + path
        print full_url
        self.visited_links.add(full_url)

        # load my html
        html = urlopen(full_url).read()
        # find all links
        links = LINK_REGEX.findall(html)
        links = {self.normalize_url(path, link) for link in links}
        # union
        self.collected_links = links.union(self.collected_links)
        # difference
        unvisited_links = links.difference(self.visited_links)

        for link in unvisited_links:
            if link.startswith(self.url):
                self.collect_links(urlparse(link).path)

        print "Visited links: %r \n\nCollected links: %r\n\nUnvisited: %r" % (self.visited_links, self.collected_links, unvisited_links)

if ( __name__ == "__main__" ):
    LinkCollector(sys.argv[1]).collect_links()
