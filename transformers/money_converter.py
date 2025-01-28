from forex_python.converter import CurrencyRates

def pkr_to_usd(amount_pkr):
    try:
        c = CurrencyRates()
        rate = c.get_rate('PKR', 'USD')
        amount_usd = amount_pkr * rate
        return round(amount_usd,2)
    except Exception as e:
        print("Error converting PKR to USD")
        print(e)
        return amount_pkr