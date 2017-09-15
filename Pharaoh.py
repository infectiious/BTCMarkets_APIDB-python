#!/usr/bin/env python3
import os
import threading
import time
import datetime
from multiprocessing import Process
from Markets.BTCMarkets.btcmarkets_api import Market

BCH = Market("/market/BCH/AUD/tick", "BCH", "btcmarkets")
BTC = Market("/market/BTC/AUD/tick", "BTC", "btcmarkets")
ETC = Market("/market/ETC/AUD/tick", "ETC", "btcmarkets")
ETH = Market("/market/ETH/AUD/tick", "ETH", "btcmarkets")
LTC = Market("/market/LTC/AUD/tick", "LTC", "btcmarkets")
XRP = Market("/market/XRO/AUD/tick", "XRP", "btcmarkets")


def APICollect():
    if __name__ == '__main__':
        Process(target=BCH.update_data()).start()
        Process(target=BTC.update_data()).start()
        Process(target=ETC.update_data()).start()
        Process(target=ETH.update_data()).start()
        Process(target=LTC.update_data()).start()
        Process(target=XRP.update_data()).start()
        time.sleep(5)


while True:
    APICollect()
