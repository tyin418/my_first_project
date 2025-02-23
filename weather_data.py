import requests

# Your OpenWeatherMap API Key
API_KEY = "e82a7a70bd6a46e07be48cb9230f301f"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetches weather data for a given city using OpenWeatherMap API."""
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    # Print full response for debugging
    print(f"Status Code: {response.status_code}")
    print("Response JSON:", response.text)  # This will show us the error message

    if response.status_code == 200:
        data = response.json()
        city_name = data.get("name", "Unknown")
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        print(f"City: {city_name}, Temp: {temp}°C, Weather: {weather}")
    elif response.status_code == 401:
        print("Error: Invalid API Key. Please check and update your API key.")
    elif response.status_code == 404:
        print("Error: City not found. Check the city name spelling.")
    else:
        print("Error: Unable to fetch weather data. Please try again later.")

# Ask user for a city and fetch the weather
city_name = input("Enter a city name: ")
get_weather(city_name)
