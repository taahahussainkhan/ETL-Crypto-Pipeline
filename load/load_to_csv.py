
import csv



def load_to_csv(data):
    with open("crypto-data.csv", mode="w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(
                [
                    "Serial No",
                    "Coin",
                    "Price",
                    "1h Change",
                    "24h Change",
                    "7d Change",
                    "24h Volume",
                    "Market Cap",
                    "Source",
                ]
            )
                
            writer.writerows(data)