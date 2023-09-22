from flask import Flask, render_template
from forms import WeatherData
from flask import request


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def weather_forecast():
    form = WeatherData()
    if request.method =='POST':
        print(request.form['latitude'], request.form['longitude'])
    return render_template('home.html', form = form)








