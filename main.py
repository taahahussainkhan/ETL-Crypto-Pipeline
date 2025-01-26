from scrappers.coingecko import scrape_gecko
from database.database import insert_data

coingecko = scrape_gecko()
# print("Coin Gecko: ", coingecko)
