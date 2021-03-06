from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app
from application.auth.models import User
from application.auth.forms import LoginForm

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm()) 
    
    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()

    if not user:
        return render_template("auth/loginform.html", form = form, error = "Invalid username or password")


    login_user(user)
    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))