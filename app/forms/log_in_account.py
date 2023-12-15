"""
This module is responsible for the form for entering the email
address and password during user authentication.
"""
from wtforms import StringField, \
                    BooleanField, \
                    PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import Email, \
                               Length, \
                               Regexp, \
                               DataRequired


class UserLogIn(FlaskForm):
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
    password = PasswordField('Пароль',
                             validators=[DataRequired(), Length(min=8, max=20),
                                         Regexp(r'(?=.*[a-zA-Z])(?=.*\d)',
                             message='Пароль должен содержать хотя бы одну букву и одну цифру')])
    remember = BooleanField("Запомнить меня")