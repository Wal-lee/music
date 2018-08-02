class Weather_data:
    def __init__(self):
        self.city = ''
        self.temp1 = ''
        self.temp2 = ''
        self.weather = ''
    
    def fill(self, weather_data):
        self.city = weather_data['city']
        self.temp1 = weather_data['temp1']
        self.temp2 = weather_data['temp2']
        self.weather = weather_data['weather']
     
    
        
