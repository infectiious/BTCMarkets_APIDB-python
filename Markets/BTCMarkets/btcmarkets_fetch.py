#!/usr/bin/env python3
from btcmarkets_api import Market

BTC = Market("/market/BTC/AUD/tick", "BTC")
LTC = Market("/market/LTC/AUD/tick", "LTC")
ETH = Market("/market/ETH/AUD/tick", "ETH")
ETC = Market("/market/ETC/AUD/tick", "ETC")
XRP = Market("/market/XRP/AUD/tick", "XRP")
BCH = Market("/market/BCH/AUD/tick", "BCH")

BTC.update_data()
LTC.update_data()
ETH.update_data()
ETC.update_data()
XRP.update_data()
BCH.update_data()
