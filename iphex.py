ip_list = list()
while True:
    inp = raw_input('Enter an IP Address as: xxx.xxx.xxx.xxx, or type "done":')
    if inp == 'done': break
    addy = str(inp)
    ip_list = addy.split('.')
    f = ip_list[0]
    f = int(f)
    f = bin(f)
    s = ip_list[1]
    s = int(s)
    s = bin(s)
    t = ip_list[2]
    t = int(t)
    t = bin(t)
    l = ip_list[3]
    l = int(l)
    l = bin(l)
print " "
print "%-15s %-15s %-15s %-15s" % ("First Octet","Second Octet","Third Octet", "Last Ocetet")    
print "%-15s %-15s %-15s %-15s" % (f, s, t, l)

    
