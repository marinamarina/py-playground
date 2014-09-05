#!/usr/bin/env python
# """ lists tuples dictionaries """

list = ['the', 'holy', 'grail', 'the']
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

# SETS unordered collections with unique elements, no duplicates allowed
set1 = set(list)

# Dictionaries
dict1 = {'alisa':'sleeps', 'scarlett':'playing', 'zoja': 'chilling'}
#dict1['zmeja'] = 'hissing'
#del dict1['alisa']
print 'alisa' in dict1.keys()

list_numbers = [1,2,3,4,5]

for n in range(0,len(list_numbers)):
    if (list_numbers[n]%2 != 0):
        print list_numbers[n]

