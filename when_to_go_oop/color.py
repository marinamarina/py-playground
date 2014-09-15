#! usr/bin/env python

class Color:
    def __init__(self, rgb_value, name):
        self._rgb_value = rgb_value
        self._name = name

    def set_name(self, name):
        self._name = name

    def get_name(self):
        'This is a name property'
        return self._name

    name = property(get_name, set_name)

# more realistic example
import urllib2
import time
class WebPage:

    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if self._content == None:
            print("Retrieving new page")
            self._content = urllib2.urlopen(self.url).read()
        return self._content

webpage = WebPage("http://ccphillips.net/")

startTime = time.time()
content1 = webpage.content
timer = round( (time.time() - startTime)*100, 5)
print timer

startTime = time.time()
content2 = webpage.content
timer = round( (time.time() - startTime)*100, 5)
print timer

print ("Is content 1 equal to content 2? %s") % (content1 == content2)

class AverageList(list):
    'class inheriting from the list and calculating average'
    @property
    def average(self):
        return sum(self) / len(self)

averageList = AverageList([1,2,3,4,5,6,8])

print "This is the average of my list: %s" % averageList.average
