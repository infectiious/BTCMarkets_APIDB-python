#!/usr/bin/env python3
import os
import threading
import time
import datetime
from multiprocessing import Process
from Markets.BTCMarkets.btcmarkets_api import MarketBTCMarkets
from Markets.BitFinex.Bitfinex_api import MarketBitfinex

# Set variables for BTCMarkets.
BCHBTCMarkets = Market("/market/BCH/AUD/tick", "BCH", "btcmarkets")
BTCBTCMarkets = Market("/market/BTC/AUD/tick", "BTC", "btcmarkets")
ETCBTCMarkets = Market("/market/ETC/AUD/tick", "ETC", "btcmarkets")
ETHBTCMarkets = Market("/market/ETH/AUD/tick", "ETH", "btcmarkets")
LTCBTCMarkets = Market("/market/LTC/AUD/tick", "LTC", "btcmarkets")
XRPBTCMarkets = Market("/market/XRO/AUD/tick", "XRP", "btcmarkets")

# Set variables for BitFinex.
BCHBitFinex = Market("/v2/ticker/tBCHUSD", "BCH", "bitfinex")
BTCBitFinex = Market("/v2/ticker/tBTCUSD", "BTC", "bitfinex")
ETCBitFinex = Market("/v2/ticker/tETCUSD", "ETC", "bitfinex")
ETHBitFinex = Market("/v2/ticker/tETHUSD", "ETH", "bitfinex")
LTCBitFinex = Market("/v2/ticker/tLTCUSD", "LTC", "bitfinex")
XRPBitFinex = Market("/v2/ticker/tXRPUSD", "XRP", "bitfinex")

# Set variables for KuCoin
BCHKuCoin = Market("/v1/BCH-USDT/open/tick", "BCH", "kucoin")
BTCKuCoin = Market("/v1/BTC-USDT/open/tick", "BTC", "kucoin")
ETCKuCoin = Market("/v1/ETC-USDT/open/tick", "ETC", "kucoin")
ETHKuCoin = Market("/v1/ETH-USDT/open/tick", "ETH", "kucoin")
LTCKuCoin = Market("/v1/LTC-USDT/open/tick", "LTC", "kucoin")
XRPKuCoin = Market("/v1/XRP-USDT/open/tick", "XRP", "kucoin")

# Function to run each API script for each market.
def APICollect():
    if __name__ == '__main__':

        # Process BTCMarkets.
        Process(target=BCHBTCMarkets.update_data()).start()
        Process(target=BTCBTCMarkets.update_data()).start()
        Process(target=ETCBTCMarkets.update_data()).start()
        Process(target=ETHBTCMarkets.update_data()).start()
        Process(target=LTCBTCMarkets.update_data()).start()
        Process(target=XRPBTCMarkets.update_data()).start()

        #Process BitFinex.
        Process(target=BCHBitFinex.update_data()).start()
        Process(target=BTCBitFinex.update_data()).start()
        Process(target=ETCBitFinex.update_data()).start()
        Process(target=ETHBitFinex.update_data()).start()
        Process(target=LTCBitFinex.update_data()).start()
        Process(target=XRPBitFinex.update_data()).start()

        #Process KuCoin.
        Process(target=BCHKuCoin.update_data()).start()
        Process(target=BTCKuCoin.update_data()).start()
        Process(target=ETCKuCoin.update_data()).start()
        Process(target=ETHKuCoin.update_data()).start()
        Process(target=LTCKuCoin.update_data()).start()
        Process(target=XRPKuCoin.update_data()).start()

        time.sleep(5)

# Run function.
while True:
    APICollect()
