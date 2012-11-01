#!/usr/bin/python
import dns.resolver

domains = ('www.stone-it.com', 'www.huiser.nl')

for domain in domains:
    answers = dns.resolver.query(domain, 'A')
    for rdata in answers:
        print "The IP address for %s is %s " % (domain, rdata.address)

# http://www.dnspython.org/docs/1.10.0/html/dns.rdtypes.IN.A.A-class.html

