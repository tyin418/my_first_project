import requests
import json

# Free API for currency exchange rates
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

# Fetch exchange rate data
response = requests.get(API_URL)
data = response.json()

# Save to a JSON file
with open("exchange_rates.json", "w") as file:
    json.dump(data, file, indent=4)

# Print exchange rates
print("Currency Exchange Rates:")
for currency, rate in data["rates"].items():
    print(f"{currency}: {rate}")
