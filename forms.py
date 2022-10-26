from email.policy import default
from flask_wtf import FlaskForm
from sqlalchemy import Float
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, DecimalField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
    email = StringField("E-mail adress", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Sign in")

class RegistrationForm(FlaskForm):
    email = StringField("E-mail adress", validators=[DataRequired(), Email()])
    password1 = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=80)])
    password2 = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password1", message="Passwords are not the same")])
    submit = SubmitField("Register")

class ExpenseForm(FlaskForm):
    date_added = DateField("Date", validators=[DataRequired()])
    price = DecimalField("Price", validators=[DataRequired()], places=2, rounding=None)
    product = StringField("Product", validators=[DataRequired(), Length(max=150)])
    expense_type = SelectField("Type of expense", validators=[DataRequired()], choices=[("Normal"), ("Additional")])
    vendor = StringField("Vendor", validators=[DataRequired(), Length(max=150)])
    submit = SubmitField("Add")