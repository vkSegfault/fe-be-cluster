from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from .model import User

class RegisterForm(FlaskForm):
    # below func is called automatically
    # def validate_username(self, username_to_check):   # we must mix `validate_` and name of the field we want to automatically validate
    #     user = User.query.filter_by(name=username_to_check.data).first()   # this line produces Weak Ref error in Flask, might be bug in flask-sqlalchemy, supposedly downgrade to 2.5.1 helps
    #     if user:
    #         raise ValidationError(F"{username_to_check} already exists")

    username = StringField(label="Username:", validators=[Length(min=2, max=30)])
    email = StringField(label="email")
    password = PasswordField(label="password")
    submit = SubmitField(label="Register")

class LoginForm(FlaskForm):
    username = StringField(label="Username:", validators=[Length(min=2, max=30)])
    password = PasswordField(label="password")
    submit = SubmitField(label="Sign In")