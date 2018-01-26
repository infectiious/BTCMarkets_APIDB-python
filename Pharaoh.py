#!/usr/bin/env python3
import os
import threading
import time
import datetime
from multiprocessing import Process
from Markets.BTCMarkets.btcmarkets_api import MarketBTCMarkets
from Markets.BitFinex.bitfinex_api import MarketBitfinex
from Markets.KuCoin.kucoin_api import MarketKuCoin

# Set variables for BTCMarkets.
BCHBTCMarkets = MarketBTCMarkets("/market/BCH/AUD/tick", "BCH", "btcmarkets")
BTCBTCMarkets = MarketBTCMarkets("/market/BTC/AUD/tick", "BTC", "btcmarkets")
ETCBTCMarkets = MarketBTCMarkets("/market/ETC/AUD/tick", "ETC", "btcmarkets")
ETHBTCMarkets = MarketBTCMarkets("/market/ETH/AUD/tick", "ETH", "btcmarkets")
LTCBTCMarkets = MarketBTCMarkets("/market/LTC/AUD/tick", "LTC", "btcmarkets")
XRPBTCMarkets = MarketBTCMarkets("/market/XRO/AUD/tick", "XRP", "btcmarkets")

# Set variables for BitFinex.
BCHBitFinex = MarketBitfinex("/v2/ticker/tBCHUSD", "BCH", "bitfinex")
BTCBitFinex = MarketBitfinex("/v2/ticker/tBTCUSD", "BTC", "bitfinex")
ETCBitFinex = MarketBitfinex("/v2/ticker/tETCUSD", "ETC", "bitfinex")
ETHBitFinex = MarketBitfinex("/v2/ticker/tETHUSD", "ETH", "bitfinex")
LTCBitFinex = MarketBitfinex("/v2/ticker/tLTCUSD", "LTC", "bitfinex")
XRPBitFinex = MarketBitfinex("/v2/ticker/tXRPUSD", "XRP", "bitfinex")

# Set variables for KuCoin
BCHKuCoin = MarketKuCoin("/v1/BCH-USDT/open/tick", "BCH", "kucoin")
BTCKuCoin = MarketKuCoin("/v1/BTC-USDT/open/tick", "BTC", "kucoin")
ETCKuCoin = MarketKuCoin("/v1/ETC-USDT/open/tick", "ETC", "kucoin")
ETHKuCoin = MarketKuCoin("/v1/ETH-USDT/open/tick", "ETH", "kucoin")
LTCKuCoin = MarketKuCoin("/v1/LTC-USDT/open/tick", "LTC", "kucoin")
XRPKuCoin = MarketKuCoin("/v1/XRP-USDT/open/tick", "XRP", "kucoin")

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
