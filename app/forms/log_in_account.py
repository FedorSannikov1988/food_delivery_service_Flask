from wtforms import StringField, \
                    BooleanField, \
                    PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import Email, \
                               Length, \
                               Regexp, \
                               DataRequired


class UserLogIn(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=50)])
    password = PasswordField('Пароль',
                             validators=[DataRequired(), Length(min=8, max=20),
                                         Regexp(r'(?=.*[a-zA-Z])(?=.*\d)',
                             message='Пароль должен содержать хотя бы одну букву и одну цифру')])
    remember = BooleanField("Запомнить меня")