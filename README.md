# crypto-etl
# Crypto ETL

A small ETL pipeline that extracts cryptocurrency market data from  COINPAPRIKA, transforms it with pandas,
and loads it into a PostgreSQL database.

## How it works

1. Extract: fetch ticker data for each coin in `COINS`
   (e.g. `btc-bitcoin`, `xrp-xrp`)
3. Transform: flatten the JSON with `pd.json_normalize` and drop
   unneeded columns (rank, supply fields, timestamps, etc.).
4. Load: write the cleaned DataFrame to a PostgreSQL table.
