from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class RestaurantForm(FlaskForm):
    name = StringField("Restaurant name", [validators.Length(min=3)])
    address = StringField("Address", [validators.Length(min=3)])
    city = StringField("City", [validators.Length(min=2)])
    postcode = IntegerField("Postcode")

    class Meta:
        csrf = False