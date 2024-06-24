#!/bin/python

#Ip generator 192.168.100.*

ip = 1

"""while ip < 10:
    print("192.168.100." + str(ip))
    ip += 1
"""
#Break
"""while ip < 10:
    print("192.168.100." + str(ip))
    if ip == 5:
        break
    ip += 1
"""

#Continue
"""while ip < 10:
    ip += 1
    if ip == 5:
        continue
    print("192.168.100." + str(ip))
"""

#Else
while ip < 10:
    print("192.168.100." + str(ip))
    ip += 1
else:
    print("IP generator List!")
    