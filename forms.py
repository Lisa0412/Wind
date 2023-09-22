from flask_wtf import Form
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class WeatherData(Form):
    latitude = StringField(u'ширина', [DataRequired(), Length(min=6, max=15)])
    longitude = StringField(u'довгота', [DataRequired(), Length(min=6, max=15)])
    submit = SubmitField('Прогноз')