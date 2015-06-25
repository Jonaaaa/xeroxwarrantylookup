#!/usr/bin/python

import sys
import requests
import math

serials = "xerox.serials"
count = 0

def check_warranty(serial):
    payload = {'serial': serial}
    r = requests.post('https://www.office.xerox.com/smart/entitlements/index.cfm?fuseaction=entitlements.findEntitlement', params=payload)
    if "Active" not in r.content:
        print '[*]', serial, 'is: \033[1;31mExpired\033[1;m'
    else:
        print '[*]', serial, 'is: \033[1;32mActive\033[1;m'

print "********************************"
print " Xerox Warranty Checker v0.1"
print "********************************"
print "[*] Opening Serial list:",
try:
    with open(serials, "r") as f:
        print "Success"
        for serial in f:
            count +=1
            check_warranty(serial.strip())
    print "[*] Checked Xerox Warranty for", count , "Supplied Serials"
except Exception:
    print "[!] Failed while accesing or sending serials"
