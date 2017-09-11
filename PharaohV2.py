#!/usr/bin/env python3
import os
import threading
import time
import datetime
from multiprocessing import Process
from Markets.BTCMarkets.btcmarkets_api import Market

BTC = Market("/market/BTC/AUD/tick", "BTC")
LTC = Market("/market/LTC/AUD/tick", "LTC")
ETH = Market("/market/ETH/AUD/tick", "ETH")
ETC = Market("/market/ETC/AUD/tick", "ETC")
XRP = Market("/market/XRP/AUD/tick", "XRP")
BCH = Market("/market/BCH/AUD/tick", "BCH")

def PrintTime():
    print("Time:", datetime.datetime.utcnow())

def APICollect():
    if __name__ == '__main__':
        Process(target=PrintTime).start()
        Process(target=BTC.update_data()).start()
        Process(target=LTC.update_data()).start()
        Process(target=ETH.update_data()).start()
        Process(target=ETC.update_data()).start()
        Process(target=XRP.update_data()).start()
        Process(target=BCH.update_data()).start()
        time.sleep(10)

while True:
    APICollect()
