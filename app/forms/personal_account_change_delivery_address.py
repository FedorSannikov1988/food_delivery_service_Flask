"""
This module is responsible for the form for entering
a new delivery address.
"""

from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import Length, \
                               DataRequired


class PersonalAccountChangeDeliveryAddress(FlaskForm):
    """
    Form for changing the default shipping address in the personal account.

    Attributes:
    - default_shipping_address: TextAreaField - the field for entering the default shipping address

    Validators:
    - default_shipping_address: DataRequired, Length(max=1000) - ensures that the default shipping address is provided and not longer than 1000 characters
    """

    default_shipping_address = TextAreaField('Адрес доставки по умолчанию',
                                           validators=[DataRequired(), Length(max=1000)])