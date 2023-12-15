"""
This module is responsible for the form for entering
new personal data in the user's personal account.
"""
from wtforms import StringField, \
                    DateField
from flask_wtf import FlaskForm
from wtforms.validators import Length, \
                               DataRequired


class PersonalAccountChangePersonalData(FlaskForm):
    """
    Form for changing personal data in the personal account.

    Attributes:
    - name: StringField - the field for entering the name
    - surname: StringField - the field for entering the surname
    - patronymic: StringField - the field for entering the patronymic
    - date_birth: DateField - the field for entering the date of birth

    Validators:
    - name: DataRequired, Length(max=50) - ensures that the name is provided and not longer than 50 characters
    - surname: DataRequired, Length(max=50) - ensures that the surname is provided and not longer than 50 characters
    - patronymic: Length(max=50) - ensures that the patronymic is not longer than 50 characters
    - date_birth: DataRequired - ensures that the date of birth is provided
    """

    name = StringField('Имя', validators=[DataRequired(), Length(max=50)])
    surname = StringField('Фамилия', validators=[DataRequired(), Length(max=50)])
    patronymic = StringField('Отчество', validators=[Length(max=50)])
    date_birth = DateField('Дата рождения', validators=[DataRequired()])