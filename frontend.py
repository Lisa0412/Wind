from flask import Flask, render_template
from forms import WeatherData

app = Flask(__name__)

@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
@app.route("/weather")
def weather_forecast():
    form = WeatherData()
    #if form.validate_on_submit():
    return render_template('home.html', form = form)


if __name__ == '__main__':
    app.run(debug=True)





