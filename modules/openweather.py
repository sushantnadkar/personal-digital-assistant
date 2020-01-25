import requests

from pprint import pprint
from speech.tts import	speak


def what_weather(city, key):

	base_url = "http://api.openweathermap.org/data/2.5/weather?"
	url = base_url + "appid=" + key + "&q=" + city
	weather_data = requests.get(url).json()

	speak("OpenWeather says: It is " + weather_data["weather"][0]["description"] + " and " + str(float(weather_data["main"]["temp"]) - float(273.15)) + " degree celcius now in " + city)
