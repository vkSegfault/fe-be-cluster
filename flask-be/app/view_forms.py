from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class RegisterForm(FlaskForm):
    username = StringField(label="Username:", validators=[Length(min=2, max=30)])
    email = StringField(label="email")
    password = PasswordField(label="password")
    submit = SubmitField(label="Register")