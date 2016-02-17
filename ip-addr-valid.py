#!/usr/bin/env python

import sys

valid = True

# Check for valid number of arugments
# Program should be called with a single IPv4 address as an argument

if len(sys.argv) == 2:
  ip_addr = sys.argv[1]
  print ip_addr
  octets = ip_addr.split(".")
  print octets
  if len(octets) != 4:
    print 'Invalid number of octets'
    exit
  elif (int(octets[0]) < 1) | (int(octets[0]) > 223):
    print octets[0]
    valid = False
    print 'Invalid first octet. (Cannot be less than 1 or greater than 223)'
    exit
  elif (int(octets[0])) == 127:
    print octets[0]
    valid = False
    print 'Invalid first octet. (Cannot be 127)'
  elif (int(octets[0]) == 169) & (int(octets[1]) == 254):
    valid = False
    print 'IP address must not be in the 169.254.0.0/16 range'
    exit
  else:
    for x in range(1,4):
      if (int(octets[x]) < 0) | (int(octets[x]) > 255):
        valid = False
        print "Octet %i is out of range (0 - 255)" % (x + 1)
        exit
  if valid:
    print "IP address %s is a valid address." % ip_addr
else:
  print 'Invalid number of arguments'

