from flask_wtf import Form
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class WeatherData(Form):
    latitude = StringField(u'latitude', [DataRequired(), Length(min=6, max=10)])
    longitude = StringField(u'longitude', [DataRequired(), Length(min=6, max=10)])
    submit = SubmitField('Submit')