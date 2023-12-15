"""
This module is responsible for the form for entering a new password
in the user's personal account.
"""
from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms.validators import Length, \
                               Regexp, \
                               EqualTo, \
                               DataRequired


class PersonalAccountChangePassword(FlaskForm):
    """
    Form for changing the password in the personal account.

    Attributes:
    - password: PasswordField - the field for entering the new password
    - confirm_password: PasswordField - the field for confirming the new password

    Validators:
    - password: DataRequired, Length(min=8, max=20), Regexp - ensures that the new password is provided, between 8 and 20 characters long, and contains at least one letter and one digit
    - confirm_password: DataRequired, EqualTo('password') - ensures that the value of this field matches the value of the 'password' field
    """

    password = PasswordField('Пароль',
                             validators=[DataRequired(), Length(min=8, max=20),
                                         Regexp(r'(?=.*[a-zA-Z])(?=.*\d)',
                                                message=
                                                'Пароль должен содержать хотя бы одну букву и одну цифру')
                                         ])
    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password')])
