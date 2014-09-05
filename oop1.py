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
myHouse.slam_doors()


