import requests
#import pandas as pd
#import os
#from load_dotenv import load_dotenv

#load_dotenv()




COINS  = ["btc-bitcoin", "eth-ethereum", "xrp-xrp", "sol-solana", "ada-cardano"]




for coin_id in COINS:

    url = f"https://api.coinpaprika.com/v1/coins/{coin_id}"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"successfully retrieved data for {coin_id}")
    else :
        print (f"failed to retrieve data for {coin_id} with status code {response.status_code}")


    print(response.text)