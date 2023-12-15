"""
This module is responsible for the user registration form on the resource.
"""
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
    """
    Form for user registration.

    Attributes:
    - name: StringField - the field for entering the name
    - surname: StringField - the field for entering the surname
    - patronymic: StringField - the field for entering the patronymic
    - date_birth: DateField - the field for entering the date of birth
    - telephone: StringField - the field for entering the telephone number
    - email: StringField - the field for entering the email address
    - default_shipping_address: TextAreaField - the field for entering the default shipping address
    - password: PasswordField - the field for entering the password
    - confirm_password: PasswordField - the field for confirming the password

    Validators:
    - name: DataRequired, Length(max=50) - ensures that the name is provided and not longer than 50 characters
    - surname: DataRequired, Length(max=50) - ensures that the surname is provided and not longer than 50 characters
    - patronymic: Length(max=50) - ensures that the patronymic is not longer than 50 characters
    - date_birth: DataRequired - ensures that the date of birth is provided
    - telephone: DataRequired, Length(min=6, max=11), Regexp - ensures that the telephone number is provided, between
    6 and 11 digits long, and contains only digits
    - email: DataRequired, Email, Length(max=50) - ensures that the email address is provided, valid, and not longer
    than 50 characters
    - default_shipping_address: DataRequired, Length(max=1000) - ensures that the default shipping address is provided
    and not longer than 1000 characters
    - password: DataRequired, Length(min=8, max=20), Regexp - ensures that the password is provided, between 8 and 20
    characters long, and contains at least one letter and one digit
    - confirm_password: DataRequired, EqualTo('password') - ensures that the value of this field matches the value of
    the 'password' field
    """

    name = StringField('Имя', validators=[DataRequired(), Length(max=50)])
    surname = StringField('Фамилия', validators=[DataRequired(), Length(max=50)])
    patronymic = StringField('Отчество', validators=[Length(max=50)])
    date_birth = DateField('Дата рождения', validators=[DataRequired()])
    telephone = StringField('Телефон',
                            validators=[DataRequired(),
                                        Length(min=6, max=11),
                                        Regexp(r'^\d+$',
                                        message=
                                        'Номер телефона толжен содержать только цифры')])
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
