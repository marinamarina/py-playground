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
my_list = [1,2,333, 4, 333, 4]
#print my_list.count(333)
my_list.insert(1, 677)
my_list.append(444)

