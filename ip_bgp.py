entry1 = ["1.0.192.0/18",   "157.130.10.233" ,       "0 701 38040 9737 i"]
entry2 = ["1.1.1.0/24",       "157.130.10.233" ,        "0 701 1299 15169 i"]
entry3 = ["1.1.42.0/24",     "157.130.10.233",        "0 701 9505 17408 2.1465 i"]
entry4 = ["  1.0.192.0/19",   "157.130.10.233",        "0 701 6762 6762 6762 6762 38040 9737 i"]


a_ip = entry1[0]
c_ip = entry1[2]
c_ip = c_ip.split(" ")
c_ip = c_ip[1:4]

b_ip = entry2[0]
d_ip = entry2[2]
d_ip = d_ip.split(' ')
d_ip = d_ip[1:4]

C_ip = entry3[0]
D_ip = entry3[2]
D_ip = D_ip.split(' ')
D_ip = D_ip[1:5]

L_ip = entry4[0]
E_ip = entry4[2]
E_ip = E_ip.split(' ')
E_ip = E_ip[1:8]

print " "
print "%-15s %-15s" % ("IP_PREFIX ", "AS_PATH")
print "%-15s %-15s" % (a_ip, c_ip)
print "%-15s %-15s" % (b_ip, d_ip)
print "%-15s %-15s" % (C_ip, D_ip)
print "%-15s %-15s" % (L_ip, E_ip)
