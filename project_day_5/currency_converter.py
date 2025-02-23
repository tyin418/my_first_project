# currency_converter.py

# Predefined exchange rates
exchange_rates = {"EUR": 0.91, "JPY": 140.25, "GBP": 0.76}

# Function to convert currency
def convert_currency(amount, currency):
    if currency in exchange_rates:
        return amount * exchange_rates[currency]
    else:
        return "Currency not supported."

# Convert 100 USD to different currencies
print("Currency Conversion:")
for cur in exchange_rates.keys():
    print(f"100 USD = {convert_currency(100, cur)} {cur}")
