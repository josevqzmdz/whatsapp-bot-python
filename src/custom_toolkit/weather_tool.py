from langchain.tools import BaseTool
from datetime import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()
OPENWEATHER_API_KEY = os.environ["OPENWEATHER_API_KEY"]

desc = """
    use this tool to get info about the weather. it provides all the info given by 'open weather' in its free tier.
    It takes CITY as a parameter and returns the weather data for that specific city
"""

class WeatherTool(BaseTool):
    name = "weather status tool"
    description = desc

    def _run(self, city: str):
        try:
            CITY = city['title']
        except TypeError:
            CITY = city
    
    if CITY is not None and isInstance(CITY, str):
        BASE_URL = os.environ['OPENWEATHER_WEBHOOK']
        URL = BASE_URL + "appid=" + OPENWEATHER_API_KEY + "&q=" + CITY + "&units=metric"

        response = requests.get(URL).json()
        weather_list = []
        temp_celsius = str(response['main']['temp']) + "°C"
        wind_speed = str(response['wind']['speed']) + " km/h"
        humidity = str(response['main']['humidity']) + "%"
        air_pressure = str(response['main']['pressure']) + " hPa"
        clouds_coverage = str(response['clouds']['all']) + "%"
        description = response['weather'][0]['description']
        current_local_time = datetime.utcfromtimestamp(response['dt'] + response['timezone'])
        sunrise_time = datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
        sunset_time  = datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])

        weather_list.append({
            'temp_celcius': temp_celcius,
            'wind_speed': wind_speed,
            'humidity': humidity,
            'air_pressure': air_pressure,
            'clouds_coverage': clouds_coverage,
            'description': description,
            'local_time': current_local_time,
            'sunrise_time': sunrise_time,
            'sunset_time': sunset_time
        })
        return weather_list
    else:
        return "please provide a valid name of a city"

    #end of _run

    def _arun(self, query: str):
        raise NotImplementedError("this tool does not support async")
