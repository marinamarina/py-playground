#! usr/bin/env python

import sys
from urllib import urlopen

# a generator expression should be used whenever possible
#inname, outname = sys.argv[1:3]

'''with open(inname) as infile:
    with open(outname, "w") as outfile:
        lines = (line.replace("WARNING", "") for line in infile if 'WARNING' in line)
        for w in lines:
            outfile.write(w)'''

number = 5

def my_function(list=None):
    if list == None:
        list = []
    list.append('1')
    print list

# Variables unpacking, can be used for user input
def showArgs(arg1, arg2, arg3 = 'THREE'):
    print (arg1, arg2, arg3)

some_args = range(3)
more_args = {
    'arg1' : 'ONE',
    'arg2' : 'TWO'
}
#print ("Unpacking a sequence")
#showArgs(*some_args)

#print ("Unpacking another sequence")
#showArgs(**more_args)

#
