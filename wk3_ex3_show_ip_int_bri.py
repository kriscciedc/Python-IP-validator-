show_ip_int_brief = '''
Interface            IP-Address      OK?     Method      Status     Protocol
FastEthernet0   unassigned      YES     unset          up          up
FastEthernet1   unassigned      YES     unset          up          up
FastEthernet2   unassigned      YES     unset          down      down
FastEthernet3   unassigned      YES     unset          up          up
FastEthernet4    6.9.4.10          YES     NVRAM       up          up
NVI0                  6.9.4.10          YES     unset           up          up
Tunnel1            16.25.253.2     YES     NVRAM       up          down
Tunnel2            16.25.253.6     YES     NVRAM       up          down
Vlan1                unassigned      YES    NVRAM       down      down
Vlan10              10.220.88.1     YES     NVRAM       up          up
Vlan20              192.168.0.1     YES     NVRAM       down      down
Vlan100            10.220.84.1     YES     NVRAM       up          up
'''

active_ints = []
final_output = []

# Parse the output of show ip int brief into a list of lists

int_list = show_ip_int_brief.splitlines()
for x in range(len(int_list)):
  int_list[x] = int_list[x].split()


# move interfaces that are up/up into the active_ints list

for x in range(len(int_list)):
  if int_list[x] and int_list[x][-1] == 'up' and int_list[x][-2] == 'up':
    active_ints.append(int_list[x])

for line in active_ints:
  interface_name, ip_addr, ok, method, status, protocol = line
  final_output.append((interface_name, ip_addr, status, protocol))

for x in range(len(final_output)):
  print final_output[x]
