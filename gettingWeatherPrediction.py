import requests 
from pprint import pprint


API_KEY = '2fb14fb55bfb999c556230d84a51b81f'

city = input("Enter a city: ")

baseUrl = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+API_KEY

weatherData = requests.get(baseUrl).json()

pprint(weatherData)