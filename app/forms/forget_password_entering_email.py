from wtforms import StringField
from flask_wtf import FlaskForm
from wtforms.validators import Email, \
                               Length, \
                               DataRequired


class ForgetPasswordEnteringEmail(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=50)])