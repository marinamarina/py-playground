#!/usr/bin/env python
""" OOP """

class house:
    doors=3

    def __init__(self, doors=4):
        self.doors = doors

    def slam_doors(self):
        for door in range(self.doors):
            print "Slam door %d" % door

myHouse = house()
#myHouse.slam_doors()

# Example class for @property example
# Property is a getter for a read-only attribute
class C:
    def __init__(self):
        self._x = 'Marina'

    @property
    def x(self):
        """I'm the x property"""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

    #x = property(getX,delX,setX, "I'm the x property")

""" c is an instance of class C
 c.x will invoke the getter, c.x = value will invoke the setter and del c.x the deleter.
"""
c = C()
c.x = 'KhAlisa'
#print c.x

class GetSet:
    'A class Implemented with getters and setters'
    def __init__(self):
        self._x = 'meow'

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

getset = GetSet()
getset.setX('smthelse')
print 'This is using getter/setter: ' + getset.getX()

class GetSetProp:
    'A class Implemented with decorator property'
    y = 0
    def __init__(self):
        self._x = 'meow'

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value

getsetprop = GetSetProp()
getsetprop.x = 'smthelse'
print 'This is using decorator: ' + getsetprop.x

class Person:
    'Yet another property example'
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name

    @property
    def name(self):
        return 'First name %s, second name %s' % (self.first_name, self.second_name)

    @name.setter
    def name(self, value):
        return 'First name %s, second name %s' % (self.first_name, self.second_name)




person1 = Person('Lisi', 'Kisa')
#person1.name = 'Kisi', 'Lisi'
print person1.name
from math import sqrt

class Point:
    'represents a point in two-dimensional geometric coordinates'

    def __init__(self, x =0, y=0):
        self.move(x, y)

    def reset(self):
        'resets the point to (0,0)'
        self.x = 0
        self.y = 0

    def move(self, x, y):
        'move to a given point'
        self.x = x
        self.y = y

    def checkDistance(self, point):
        """
        :param point:
        :return: the distance
        """
        xd = point.x - self.x
        yd = point.y - self.y

        return sqrt(xd*xd + yd*yd)


p = Point()
q = Point(5, 0)

print p.checkDistance(q)
assert (p.checkDistance(q) == q.checkDistance(p))
p.move(3, 4)
print p.checkDistance(q)
print p.checkDistance(p)

class SecretString:
    '''A not secure way to store a secret string'''

    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase

    def decrypt(self, pass_phrase):
        if pass_phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return 'You have not guessed'

secret = SecretString('BiG secret', 'shh')
print secret._SecretString__plain_string