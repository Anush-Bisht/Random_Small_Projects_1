CURRENCIES = {
    'USD' : 1,
    'EUR' : 1.06,
    'YEN' : 0.0067,
    'GBP' : 1.23,
    'AUD' : 0.64,
    'CAD' : 0.74  
}

def to_usd(currency_code, amount):
    if currency_code not in CURRENCIES:
        raise Exception(f"{currency_code} is not supported")
    elif(amount < 0):
        raise Exception("Invalid amount")
    
    value = CURRENCIES[currency_code] * amount
    return value


def from_usd(currency_code, amount):
    if currency_code not in CURRENCIES:
        raise Exception(f"{currency_code} is not supported")
    elif(amount < 0):
        raise Exception("Invalid amount")
    
    value = amount / CURRENCIES[currency_code]
    return round(value, 4)

def convert(from_currency, amount, to_currency):
    try:
        amount_in_usd = to_usd(amount, from_currency)        
        converted_amount = from_usd(amount_in_usd, to_currency)
        
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        
    except Exception as e:
        print(e)


# curr_cov = to_usd(input().upper(), input())
curr_cov = from_usd(input().upper(), input())
print(curr_cov)