import os
import threading
import time
import datetime
from multiprocessing import Process

# Updating Bitcoin.
def BTCUpdate():
    print("Updating Bitcoin prices.")
    os.system(["python", "btc_update.py"], cwd="Markets")

# Updating Ethereum Classic.
def ETCUpdate():
    print("Updating Ethereum classic prices.")
    os.system(["python", "etc_update.py"], cwd="Markets")

# Updating Ethereum.
def ETHUpdate():
    print("Updating Ethereum prices.")
    os.system(["python", "eth_update.py"], cwd="Markets")

# Updating Litecoin.
def LTCUpdate():
    print("Updating Litcoin prices.")
    os.system(["python", "ltc_update.py"], cwd="Markets")

# Updating Ripple.
def XRPUpdate():
    print("Updating XRP prices.")
    os.system(["python", "xrp_update.py"], cwd="Markets")


def PrintTime():
    print("Time:", datetime.datetime.utcnow())


def APICollect():
    if __name__ == '__main__':
        Process(target=PrintTime).start()
        Process(target=BTCUpdate).start()
        Process(target=ETCUpdate).start()
        Process(target=ETHUpdate).start()
        Process(target=LTCUpdate).start()
        Process(target=XRPUpdate).start()
        time.sleep(150)


while True:
    APICollect()
