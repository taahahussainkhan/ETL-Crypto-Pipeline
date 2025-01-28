def extract_coin_name_and_symbol(raw_text):
    parts = raw_text.split("\n")  
    if len(parts) >= 2:
        coin_name = parts[1].strip()  
        symbol = parts[2].strip()  
        return coin_name + symbol
    return None, None  