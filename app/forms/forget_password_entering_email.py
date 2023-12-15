"""
This module is responsible for the form for entering an email
address in the password recovery procedure.
"""
from wtforms import StringField
from flask_wtf import FlaskForm
from wtforms.validators import Email, \
                               Length, \
                               DataRequired


class ForgetPasswordEnteringEmail(FlaskForm):
    """
    Form for entering the email address for the forget password feature.

    Attributes:
    - email: StringField - the field for entering the email address

    Validators:
    - DataRequired: ensures that the field is not empty
    - Email: ensures that the email address is valid
    - Length(max=50): ensures that the email address is not longer than 50 characters
    """
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=50)])