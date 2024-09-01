import requests
from fuzzywuzzy import process

known_cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "New Brunswick", "San Francisco"]

def correct_city_name(city):
    best_match = process.extractOne(city, known_cities)
    return best_match[0] if best_match and best_match[1] > 80 else city

def get_weather(city, api_key, for_tomorrow=False):
    base_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=imperial" if for_tomorrow else \
               f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    response = requests.get(base_url)
    if response.status_code == 200:
        weather_data = response.json()
        weather_description = weather_data["list"][1]["weather"][0]["description"] if for_tomorrow else weather_data["weather"][0]["description"]
        temp = weather_data["list"][1]["main"]["temp"] if for_tomorrow else weather_data["main"]["temp"]
        return f"The temperature in {city} {( 'tomorrow' if for_tomorrow else '')} is {temp}°F with {weather_description}."
    return "City not found. Please check the city name and try again." if response.json().get("cod") == "404" else "Sorry, I couldn't retrieve the weather information. Please try again later."