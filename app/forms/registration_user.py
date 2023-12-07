from wtforms import DateField, \
                    StringField, \
                    PasswordField, \
                    TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import Email, \
                               Length, \
                               Regexp, \
                               EqualTo, \
                               DataRequired


class UserRegistration(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(), Length(max=50)])
    surname = StringField('Фамилия', validators=[DataRequired(), Length(max=50)])
    patronymic = StringField('Отчество', validators=[Length(max=50)])
    date_birth = DateField('Дата рождения', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=50)])
    default_shipping_address = TextAreaField('Адрес доставки по умолчанию',
                                           validators=[DataRequired(), Length(max=1000)])
    password = PasswordField('Пароль',
                             validators=[DataRequired(), Length(min=8, max=20),
                                         Regexp(r'(?=.*[a-zA-Z])(?=.*\d)',
                                                message=
                                                'Пароль должен содержать хотя бы одну букву и одну цифру')
                                         ])
    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password')])
