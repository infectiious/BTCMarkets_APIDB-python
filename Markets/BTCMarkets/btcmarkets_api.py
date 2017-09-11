#!/usr/bin/env python3
import argparse
import requests
import time
import datetime
import random
import pymysql
from connections import hostname, username, password, portnumber, database

class Market(object):
  domain = "https://api.btcmarkets.net"
  url = ""
  uri = ""

  def __init__(self, uri, name):
    super(Market, self).__init__()
    self.name = name
    self.uri = uri
    self.url = self.domain + uri

  def update_data(self):
    # db = pymysql.connect(host=hostname, user=username, passwd=password, port=portnumber, db=database)
    # db.autocommit(True)
    # cur = db.cursor()
    r = requests.get(self.url, verify=True)
    ask = str(r.json()["bestAsk"])
    bid = str(r.json()["bestBid"])
    last = str(r.json()["lastPrice"])
    tstamp = r.json()["timestamp"]
    ltime = time.ctime(tstamp)
    utime = time.asctime(time.gmtime(tstamp))
    print ask
    # query = "INSERT INTO %smarkets_eth(ask,bid,lastsale,recorded_time) " \
    #    "VALUES(%s,%s,%s,FROM_UNIXTIME(%s))" % ( self.name, ask, bid, last, tstamp)
    # cur.execute(query)
    # cur.close()
    # db.close()
