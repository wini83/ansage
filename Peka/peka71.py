#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2 sty 2018


'''

import json
import urllib2
import time
import urllib


def now_milliseconds():
    return int(time.time() * 1000)

lcdUrl = "http://192.168.1.200/control?cmd=lcd,"

def peka_vm_get(met,p0):
    url = "http://www.peka.poznan.pl/vm/method.vm?ts="+str(now_milliseconds())
    headers = {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8"}
    payload = urllib.urlencode({'method' : met,
                                'p0'  : p0})
    req = urllib2.Request(url, payload, headers)
    response = urllib2.urlopen(req)

    # Parse Json
    data = json.load(response)
    return data

# Preety print the result
#print json.dumps(peka_vm_get('getStopPoints','{"pattern":"IPN"}'), indent=4, sort_keys=True)

#print json.dumps(peka_vm_get('getBollardsByStopPoint','{"name":"IPN"}'), indent=4, sort_keys=True)

ipn01 = peka_vm_get('getTimes','{"symbol":"IPNZ01"}')
#ipn02 = peka_vm_get('getTimes','{"symbol":"IPNZ02"}')

l1 = ipn01["success"]["times"][0]
#l2 = ipn02["success"]["times"][0]
#print (json.dumps(l1, indent=4, sort_keys=True, ensure_ascii=False).encode('UTF-8'))
print('{}>{}:{}m'.format(l1["line"],l1["direction"].encode('UTF-8'),l1["minutes"]))
#print('{}>{}:{}m'.format(l2["line"],l2["direction"].encode('UTF-8'),l2["minutes"]))


