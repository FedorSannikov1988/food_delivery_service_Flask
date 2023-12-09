from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms.validators import Length, \
                               Regexp, \
                               EqualTo, \
                               DataRequired


class ForgetPasswordEnterNewPassword(FlaskForm):
    password = PasswordField('Пароль',
                             validators=[DataRequired(), Length(min=8, max=20),
                                         Regexp(r'(?=.*[a-zA-Z])(?=.*\d)',
                                                message=
                                                'Пароль должен содержать хотя бы одну букву и одну цифру')
                                         ])
    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password')])
