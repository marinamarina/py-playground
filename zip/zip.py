#!/usr/bin/env python

'''A simple parser for this file can use zip to create lists of tuples that map headers to values.
These lists can be used to create a dictionary, a much easier object to work with in Python than a file!'''
import sys

filename = sys.argv[1]
contacts = []

with open(filename) as file:
    header = file.readline().strip("\n").split(" ")

    # creating tuples mapping each line

    contacts = [
        dict(
            zip(header, line.strip().split(" "))
    ) for line in file
    ]

print contacts

