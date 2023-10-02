from flask import Flask, render_template
from forms import WeatherData
from flask import request
from src import weathercode_dictionary

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def weather_forecast():
    form = WeatherData()
    if request.method =='POST':
        input_list = [request.form['latitude'], request.form['longitude']]
        latitude_longitude_dictionary_input = {"latitude": input_list[0], "longitude": input_list[1]}
        print(latitude_longitude_dictionary_input)

        with open("src/Script_V1_python.py", mode="r", encoding="utf-8") as forecast:
          code = forecast.read()
        print(exec(code, {"latitude_longitude_dictionary" : latitude_longitude_dictionary_input}))
    return render_template('home.html', form = form)








