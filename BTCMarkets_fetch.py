import os
import threading
import time
import datetime
from multiprocessing import Process

# BTCMarkets.net.

def BTCUpdate():
    print ("Updating Bitcoin prices.")
    os.system("python BTCAUDTicker.py")

def ETCUpdate():
    print ("Updating Ethereum classic prices.")
    os.system("python ETCAUDTicker.py")

def ETHUpdate():
    print ("Updating Ethereum prices.")
    os.system("python ETHAUDTicker.py")

def LTCUpdate():
    print ("Updating Litcoin prices.")
    os.system("python LTCAUDTicker.py")

def XRPUpdate():
    print ("Updating XRP prices.")
    os.system("python XRPAUDTicker.py")

def PrintTime():
    print("Time:",datetime.datetime.utcnow())

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
