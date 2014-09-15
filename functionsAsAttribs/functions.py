#!/usr/bin/env python

# functions can be used as attributes
class A:
    def printMe(self):
        print "Hello from the class A"

def fakeFunction():
    print "I am not from the class A"

a = A()
a.printMe()
a.printMe = fakeFunction
a.printMe()