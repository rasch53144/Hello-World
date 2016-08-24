ip_list = list()
while True:
    inp = raw_input('Enter an IP Address as: xxx.xxx.xxx.xxx, or type "done":')
    if inp == 'done': break
    addy = str(inp)
    ip_list = addy.split('.')
    a = ip_list[0]
    a = int(a)
    b = bin(a)
    h = hex(a)

print "%-20s %-20s %-20s" % ("NETWORK_NUMBER","FIRST_OCTET_BINARY","FIRST_OCTET_HEX")    
print "%-20s %-20s %-20s" % (addy, b, h)
##print a
##print b
##print h

        
    
