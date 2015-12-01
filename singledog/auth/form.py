from flask_wtf import Form
from wtforms import BooleanField, StringField, PasswordField, validators


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=1, max=25)])
    email = StringField('Email Address', [validators.Length(min=1, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    # accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

class LoginForm(Form):
    email = StringField('Email Address', [validators.Length(min=1, max=35, message='email form error')])
    password = PasswordField('New Password', [validators.DataRequired()])

