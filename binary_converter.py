#!/usr/bin/env python

#
import sys

#initialize the list to store the binary octets
binary_octets = []

# validate that the correct number of arguments are being passed to the script
if len(sys.argv) != 2:
	print "Invalid number of arguments"
else:
        # the first argument should be the IP address (argument[0] is the script name)
	ip_addr = sys.argv[1]

	#for sanity, we will print the IP address back to the user
	print "The IP address is: %s" % ip_addr

	# use the string.split(".") function to separate the octets along the "." delimiters and store in a new list variable called octets
	octets = ip_addr.split(".")

	# iterate over the items in octets
	for i in range(len(octets)):
                # the list will contain string values so here we convert the string to an integer and then conver the integer to binary format
		current = bin(int(octets[i]))
		
		# the binary format is a string with '0b' as the first 2 characters.
		# we can't use those so we need to return a slice starting from position 3 to the end of the string
		current = current[2:]

		# the binary conversion drops leading zeroes so we need to pad the beginning of the string to reach 8 digits
		while len(current) < 8:
			current = '0' + current

		# we place the binary octets into a list by appending them to the list we initialized at the beginning of the script
		binary_octets.append(current)

# we use the join function to conver the list into a string with "." delimiters
binary_addr = ".".join(binary_octets)

# print the output including the original base-10 IP address and the binary form of that IP address
# we use the %(#)s style to give it some nice formatting.
print "%-18s %-40s" % ("IP Address","Binary Address")
print "%-18s %-40s" % (ip_addr, binary_addr)
