from pprint import pprint
from dotenv import load_dotenv
import requests
import os

load_dotenv()


def get_current_weather(city="Houston"):
    request_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid=f4680ad47cb410bad4f6e25baac19d83'
    weather_data = requests.get(request_url).json()
    # if the city search provided no data
    if weather_data == []:
        return weather_data
    new_request = f'https://api.openweathermap.org/data/2.5/weather?lat={ weather_data[0]["lat"]}&lon={weather_data[0]["lon"]}&appid=f4680ad47cb410bad4f6e25baac19d83'
    weather_data = requests.get(new_request).json()
    return weather_data


if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')
    city = input("\nPlease enter a city name: ")

    #check for empty strings or only spaces
    if not bool(city.strip()):
        city = "Houston"
    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)

    