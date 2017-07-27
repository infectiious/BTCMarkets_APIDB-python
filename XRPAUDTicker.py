#!/usr/bin/env python3

import argparse
import requests
import time
import datetime
import random
import pymysql
from connections import hostname, username, password, portnumber, database

db = pymysql.connect( host=hostname, user=username, passwd=password, port=portnumber, db=database )

db.autocommit(True)
cur = db.cursor()

domain = "https://api.btcmarkets.net"
uri = "/market/XRP/AUD/tick"
url = domain + uri

r = requests.get(url, verify=True)

ask = str(r.json()["bestAsk"])
bid = str(r.json()["bestBid"])
last = str(r.json()["lastPrice"])
tstamp = r.json()["timestamp"]
ltime = time.ctime(tstamp)
utime = time.asctime(time.gmtime(tstamp))

query = "INSERT INTO btcmarkets_xrp(ask,bid,lastsale,recorded_time) " \
        "VALUES(%s,%s,%s,FROM_UNIXTIME(%s))" % (ask, bid, last,tstamp)
cur.execute(query)
cur.close()
db.close()

