from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import Length, \
                               DataRequired


class PersonalAccountChangeDeliveryAddress(FlaskForm):
    default_shipping_address = TextAreaField('Адрес доставки по умолчанию',
                                           validators=[DataRequired(), Length(max=1000)])