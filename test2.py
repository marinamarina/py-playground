#!/usr/bin/env python
# """ 2^ 179 into output file """

print 'Task 1'
a=1
b=5
for x in range (a, b+1):
    print x

list1, list2 = [3,7], [2,2]

max1 = max(list1)
max2 = max(list2)

for x in range (1, 16):
    print '-',

print '\nTask 2\n'
# if value max1 is the maximum, assign it to the value, otherwise assign max2
value = max1 if max1 > max2 else max2

print "This is the value: %d" % value

for x in range (1, 16):
    print '-',
print '\nTask 3\n'