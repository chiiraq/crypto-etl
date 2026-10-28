import os
import requests
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
#print("USER:", repr(os.getenv("DB_USER")), "| PASS set:", os.getenv("DB_PASSWORD") is not None)
engine = create_engine('postgresql+psycopg2://avnadmin:AVNS_mTnl05XSnDdiXB6-yzC@pg-20b3dd5-wangarichiiraq-6d5e.a.aivencloud.com:26444/defaultdb?sslmode=require')

COINS = ["btc-bitcoin"]

for coin_id in COINS:
    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        df = pd.json_normalize(data)
        df = df.drop(
            columns=["rank", "total_supply", 
                     "max_supply", "beta_value",
                     "quotes.USD.percent_from_price_ath", "quotes.USD.percent.ath_date",
                     "first_data_at", "last_updated", "quotes.USD.percent_change_15m",
                     "quotes.USD.percent_change_30m", "quotes.USD.percent_change_1h",
                     "quotes.USD.percent_change_6h", "quotes.USD.percent_change_12h",
                     "quotes.USD.percent_change_24h", "quotes.USD.percent_change_7d",
                     "quotes.USD.percent_change_30d", "quotes.USD.percent_change_1y",
                     "quotes.USD.ath_price", "quotes.USD.market_cap_change_24h", 
                     "quotes.USD.market_cap_change_24h_percentage", "quotes.USD.volume_24h_change_24h"],
            errors="ignore",
        )

       

        df.to_sql('crypto_market_data', con=engine, if_exists='append', index=False)

        print(df.head())
    else:
        print(f"Failed to retrieve data for {coin_id} with status code {response.status_code}")