# -*- coding: utf-8 -*-
"""
Spyder Editor

In this script, I will create a notification for the bitcoin price. 
I will use GBP price from coingecko API. 

https://www.coingecko.com/en/api#explore-api
"""

import requests
import json
from win10toast import ToastNotifier
import time
import sys

toaster = ToastNotifier()

while True:
    r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=gbp").text
    r = json.loads(r)
    price = str(r['bitcoin']['gbp']) 
    try:
        toaster.show_toast("The price of BTC: ","{} GBP".format(price))
    except:
        print("Unexpected error:", sys.exc_info()[0])
    time.sleep(120)











