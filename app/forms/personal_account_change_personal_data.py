from wtforms import StringField, \
                    DateField
from flask_wtf import FlaskForm
from wtforms.validators import Length, \
                               DataRequired


class PersonalAccountChangePersonalData(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(), Length(max=50)])
    surname = StringField('Фамилия', validators=[DataRequired(), Length(max=50)])
    patronymic = StringField('Отчество', validators=[Length(max=50)])
    date_birth = DateField('Дата рождения', validators=[DataRequired()])