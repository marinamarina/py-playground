#!/usr/bin/env python
# """ 2^ 179 into output file """

input_file='input.txt'
output_file='output.txt'

file_handler = open(input_file, 'r')
line = file_handler.readline().rstrip()
base = int(line.split(',')[0])
power = int(line.split(',')[1])

print pow(base, power)

file_handler.close()
file_handler1 = open('ouput.txt', 'w')
file_handler1.write(str(pow(base, power)))
print "All finished!"

file_handler1.close()


