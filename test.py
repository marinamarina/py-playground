#!/usr/bin/env python
# """ Implementation on classmethod and staticmethod """

class MyDate(object):
    day = 0
    month = 0
    year = 0

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    # providing the "overloading" feature, another constructor
    @classmethod
    def from_string(cls, my_date_string):
        day, month, year = map(int, my_date_string.split('-'))
        date1 = MyDate(day, month, year)
        return date1

    # using static method I have no access to the class
    @staticmethod
    def is_valid(my_date_string):
        day, month, year = map(int, my_date_string.split('-'))

        if (day <= 31):
            return True
        else:
            return False

    def printDate(self):
       print 'Day: %s, Month: %s, Year: %s' % (self.day, self.month, self.year)

v_date = '23-04-2014'
MyDate.from_string('23-01-2015').printDate()