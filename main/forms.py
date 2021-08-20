from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
import email_validator
# even though pycharm greys this out python will give an error unless this is here. ¯\_(ツ)_/¯

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=25)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')]) # lower case p, refers to python variable

    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    # if you want username login instead of email just put that instead
    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()]) # can do length to, but not for this example
    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')