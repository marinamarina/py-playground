#!/usr/bin/env python
# """ lists tuples dictionaries """

__author__ = 'marinashchukina'

list = ['the', 'holy', 'grail']
nested_list = ['monty', 'python', 'and',\
               list]
input_list = ['alisa', 'zoja']
nested_list[-1:] = input_list
tuple = ('cat1', 'cat2', 'cat3')

# append element
nested_list.append(tuple)
nested_list.insert(0, tuple)
nested_list.extend(list)

new_tuple = tuple[0:-2]

# Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).


list_numbers = [1,2,3,4,5]

for n in range(0,len(list_numbers)):
    if (list_numbers[n]%2 != 0):
        print list_numbers[n]

