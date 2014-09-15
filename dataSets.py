#!/usr/bin/env python
"""
    Learning data sets in Python
"""
from collections import namedtuple

Tuple1 = namedtuple('Tuple1', 'low high medium')
tuple1 = Tuple1(12, 13, 12.5)

def calculate(tuple):
    value1, value2, value3 = tuple
    #print tuple[2]
    return tuple.high

#print calculate(tuple1)

# DICTIONARIES
dict = {}
dict = {'GOOG' : (200, 300, 100),
        'KOOF' : (50, 60, 30)
        }
dict.setdefault('DOOD', (30, 2, 3))
#for stock, value in dict.items():
#    print value, stock
#for stock in dict.values():
    #print stock

#for key, values in dict.items():
    #print("{} last value is {}".format(key, values[0]))

# LISTS
class weirdSortee:
    def __init__(self, string, number, sort_number):
        self.string = string
        self.number = number
        self.sort_number = sort_number

    def __lt__(self, other_object):

        # if sort_number is defined, sort by numbers
        if self.sort_number:
            return self.number < other_object.number
        # otherwise sort by strings
        return self.string < other_object.string

    def __repr__(self):
        return "String %s, int %d" % (self.string, self.number)


a = weirdSortee('wee', 34, False)
b = weirdSortee('rt', 334, False)
v = weirdSortee('vv', 35, False)
d = weirdSortee('awee', 4, False)

my_list = [a,b,v,d]
my_list.sort()
#for i in my_list:
#    print i

set1 = set()
# list of tuples representing songs & artists
song_library = [("Phantom Of The Opera", "Sarah Brightman"),
           ("Knocking On Heaven's Door", "Guns N' Roses"),
           ("Captain Nemo", "Sarah Brightman"),
           ("Patterns In The Ivy", "Opeth"),
           ("November Rain", "Guns N' Roses"),
           ("Beautiful", "Sarah Brightman"),
           ("Mal's Song", "Vixy and Tony")]
# add the artists to the set
for song, artist in song_library:
    set1.add(artist)

# sort the artists, create a list
a = list(set1)
a.sort()
#print a

my_artists = {"Sarah Brightman", "Guns N' Roses",
           "Opeth", "Vixy and Tony"}
auburns_artists = {"Opeth", "Guns N' Roses"}
#print 'All %r' % my_artists.union(auburns_artists)
#print 'Not in both: %r' % my_artists.symmetric_difference(auburns_artists)
#print 'In both: %r' % my_artists.intersection(auburns_artists)
#print 'Is superset? %r' % my_artists.issuperset(auburns_artists)
#print 'Is subset? %r' % auburns_artists.issubset(my_artists)
#print 'Difference: %r' % my_artists.difference(auburns_artists)

# convert a list of strings to a list of integers
list1 = ['1', '2', '3', '4', '5']
list2 = []
#print list1

list2 = [int(n) for n in list1 if int(n) != 3]

#print list2

from collections import namedtuple

Book = namedtuple('book', 'author bookName genre')
books_tuples = [Book("Ivanov", "Gannet feeding", "nature"),
          Book("Petrov", "My book", "fantasy"),
          Book("Sidorov", "My cleva gannet", "nature")
          ]
# output a set of nature writers
output_set = {book.author for book in books_tuples if book.genre == 'nature'}

# output a dictionary
output_dictionary = {book.author:book.bookName for book in books_tuples if book.genre == 'nature'}

print output_dictionary




