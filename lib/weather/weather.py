import requests
import json

class Weather:
    URL = 'http://www.weather.com.cn/data/cityinfo/101020100.html'

    def __init__(self):
        self.weather = {}

    def get_weather_data(self):
        self.weather = requests.get(self.URL)
        self.weather = self.weather.content
        print(self.weather)
        self.weather = json.loads(self.weather, encoding='urf-8')
        
        return self.weather