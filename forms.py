from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    email = StringField("E-mail adress", validators=[DataRequired(), Email()])
    password1 = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=80)])
    password2 = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password1")])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField("E-mail adress", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Log in")