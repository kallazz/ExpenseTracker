from flask import Flask, render_template
app = Flask(__name__)

@app.route("/register")
def register():
    return render_template("register.html", title="Sign up")

@app.route("/")
@app.route("/home")
@app.route("/login")
def login():
    return render_template("login.html", title="Sign in")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

if __name__ == "__main__":
    app.run(debug=True)


