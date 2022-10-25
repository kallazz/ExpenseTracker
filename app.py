from flask import Flask, render_template, url_for, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, RegistrationForm
import sqlite3
import os
app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY

#Login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message_category = "warning"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

#User database
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    hashed_password = db.Column(db.String(150), nullable=False)
    date_joined = db.Column(db.DateTime(), default=datetime.now, nullable=False)

    def create_password_hash(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

#Views
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_active:
        flash("You are already logged in", "warning")
        return redirect(url_for("home"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            if form.remember.data == True:
                login_user(user, remember=True)
            else:
                login_user(user, remember=False)
            next = request.args.get("next")
            return redirect(next or url_for("home"))
        flash("Invalid e-mail adress or password!", "danger")
    return render_template("login.html", title="Login", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_active:
        flash("You are already logged in", "warning")
        return redirect(url_for("home"))
        
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.create_password_hash(form.password1.data)
        db.session.add(user)
        db.session.commit()
        flash("Account created!", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/tracker")
@login_required
def tracker():
    return "Hello, logged in user!"

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))



if __name__ == "__main__":
    app.run(debug=True)

