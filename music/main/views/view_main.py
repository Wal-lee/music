from . import main
from flask import render_template
from lib.weather import weather, weather_viewmodel
@main.route('/')
def main_page():
    w = weather.Weather()
    w_d = weather_viewmodel.Weather_data()
    w_d.fill(w.get_weather_data()['weatherinfo'])
    return render_template('main.html', city=w_d.city, temp1=w_d.temp1, temp2=w_d.temp2, weather=w_d.weather)
