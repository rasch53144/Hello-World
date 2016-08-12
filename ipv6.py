
ipv6 = 'FE80:0000:0000:0000:0101:A3EF:EE1E:1719'
ipv6split = ipv6.split(":")


ipv6join = ".".join(ipv6split)

print '''We typed in an ipv6 address of
... FE80:0000:0000:0000:0101:A3EF:EE1E:1719'''
print " "
print "First we spit the address"
print " "
print ipv6split
print " "
print " "
print "Then we rejoined them"
print " "
print ipv6join

print "Is 0101 in eith file?  True or False?"
print " "
a = '0101'
b = a in ipv6split
print b
c = a in ipv6join
print c
