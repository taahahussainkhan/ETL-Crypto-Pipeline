from scrappers.coingecko import scrape_gecko
from database.database import insert_data
from scrappers.coinmarketcap import scrape_coin_market_cap
from scrappers.coinbase import scrape_coin_base
from load.load_to_csv import load_to_csv


crypto_data = []

# coingecko = scrape_gecko()
# print("Coin Gecko: ", coingecko)

# crypto_data.extend(coingecko)
# scrape_coin_market_cap()


print("Scraping Coin Market Cap...")


coin_base = scrape_coin_base()
# print("Coin Base: ", coin_base)
crypto_data.extend(coin_base)




try:
    print("Inserting data to csv...")
    load_to_csv(crypto_data)
    # insert_data(crypto_data)
except Exception as e:
    print("Error loading data to csv in main.py")
    print(e)
