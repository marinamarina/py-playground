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

# A class Implemented with getters and setters:
class GetSet:
    def __init__(self):
        self._x = 'meow'

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

getset = GetSet()
getset.setX('smthelse')
print 'This is using getter/setter: ' + getset.getX()

# A class Implemented with decorator property:
class GetSetProp:
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

# Yet another property example
class Person:
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
person1.name = 'Kisi', 'Lisi'
print person1.name