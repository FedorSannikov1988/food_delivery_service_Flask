"""
This module is responsible for the form for entering
a new user password in the password recovery procedure.
"""
from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms.validators import Length, \
                               Regexp, \
                               EqualTo, \
                               DataRequired


class ForgetPasswordEnterNewPassword(FlaskForm):
    """
    Form for entering a new password for the forget password feature.

    Attributes:
    - password: PasswordField - the field for entering the new password
    - confirm_password: PasswordField - the field for confirming the new password
    """

    password = PasswordField('Пароль',
                             validators=[DataRequired(), Length(min=8, max=20),
                                         Regexp(r'(?=.*[a-zA-Z])(?=.*\d)',
                                                message=
                                                'Пароль должен содержать хотя бы одну букву и одну цифру')
                                         ])
    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password')])
