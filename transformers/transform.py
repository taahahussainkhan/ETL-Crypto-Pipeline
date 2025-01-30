

from transformers.money_converter import pkr_to_usd
from transformers.utils import extract_coin_name_and_symbol
sr_no = 1

def transform_coin_base(data):
    global sr_no
    processed_data = [
        sr_no,
        extract_coin_name_and_symbol(data[1] ),
        pkr_to_usd(data[2]),
        "1h change",
        data[5],
        data[1],
        data[1],
        pkr_to_usd(data[4]),
        "Coin Base",
    ] 
    
    print("Processed data",processed_data)
    sr_no += 1
    return processed_data
    
    
def transform_coin_gecko(data):
    processed_data = [
        data[1] ,
        data[2],
        data[4],
        data[5],
        data[6],
        data[7],
        data[9],
        data[10],
        "Coin Gecko",
    ]
    
    # print(processed_data)
    
    return processed_data