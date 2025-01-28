

from load.load_to_csv import load_to_csv

def transform_coin_base(data):
    processed_data = [
        data[1] ,
        data[4],
        data[2],
        data[5],
        data[1],
        data[1],
        data[1],
        data[1],
        "Coin Base",
    ]
    
    print(processed_data)
    
    return processed_data
    