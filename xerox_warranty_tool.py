#!/usr/bin/python

import sys
import requests
import math
from bs4 import BeautifulSoup

serials = "xerox.serials"
count = 0

def get_warranty_status(serial):

    payload = {'serial': serial}
    try:
        r = requests.post('https://www.office.xerox.com/smart/entitlements/index.cfm?fuseaction=entitlements.findEntitlement', params=payload)
    except Exception:
        print "[!] Failed while contacting the XEROX website"

    s = BeautifulSoup(r.text, 'html.parser')
    tb = s.find_all('table')[0]
    rw = tb.find_all('tr')[2:]

    print "\033[0;37;40m[*] Serial:\033[1;32;40m", serial

    for x in range(4):
        for row in rw:
            cols = row.find_all('td')
            if cols[0].get_text() == "":
                return
            if "The product is not covered" in cols[0].get_text():
                print "\033[1;37;40m[!]\033[1;31;1m WARRANTY EXPIRED!"
                return
            print "\033[0;37;40m[*]\t" + cols[0].get_text(),
            if cols[1].get_text() == "Active":
                print "\033[3;32;40m" + cols[1].get_text()
            elif cols[1].get_text() == "Expired":
                print "\033[3;31;1m" + cols[1].get_text()
            else:
                print "\033[3;37;40m" + cols[1].get_text()


print "\033[1;37;40m********************************"
print "\033[25;31;40m Xerox Warranty Checker v0.1"
print "\033[1;37;40m********************************"
print "[-] Opening Serial list:",
try:
    with open(serials, "r") as f:
        print "Success"
        print "[-] Contacting Xerox"
        for serial in f:
            count +=1
            get_warranty_status(serial.strip())
    print "\033[0;34;40m[*] Checked Xerox warranty for", count , "supplied serial number(s)"
except Exception:
    print "[!] Something Bad..."
sys.exit(0)
