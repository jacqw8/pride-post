from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class ReusableForm(FlaskForm):
    search = StringField('Post a Kind Message!', validators=[DataRequired()])
    submit = SubmitField('Submit')