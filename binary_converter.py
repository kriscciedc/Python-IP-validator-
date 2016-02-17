#!/usr/bin/env python

import sys

binary_octets = []

# Verify number of arguments passed to script
if len(sys.argv) != 2:
	print "Invalid number of arguments"
else:
	ip_addr = sys.argv[1]
	print "The IP address is: %s" % ip_addr
	octets = ip_addr.split(".")
	for i in range(len(octets)):
		current = bin(int(octets[i]))
		current = current[2:]
		while len(current) < 8:
			current = '0' + current
		binary_octets.append(current)
binary_addr = ".".join(binary_octets)

print "%-18s %-40s" % ("IP Address","Binary Address")
print "%-18s %-40s" % (ip_addr, binary_addr)
