from scrappers.coingecko import scrape_gecko
from database.database import insert_data
from scrappers.coinmarketcap import scrape_coin_market_cap
# coingecko = scrape_gecko()
# print("Coin Gecko: ", coingecko)


scrape_coin_market_cap()
