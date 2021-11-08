from .database import get_user, save_user
from .checks import check_email, check_password_match
from flask_login import login_user, login_required, logout_user, current_user
from flask import Blueprint, render_template, redirect, request, flash, url_for


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return render_template("home.html", user=current_user)
    
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not check_email(email):
            return render_template("login.html", user=current_user)

        user = get_user(email)
        if user and user.check_password(password):
            flash("Logged in successfully!", category="success")
            login_user(user, remember=True)

            return redirect(url_for("views.home"))
        else:
            flash("Incorrect email or password.", category="error")

    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return render_template("home.html", user=current_user)
    
    if request.method == "POST":
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = get_user(email)
        
        if user is not None:
            flash("Email already in use!", category="error")
            
            return render_template("signup.html", user=current_user)
        

        if check_email(email) and check_password_match(password1, password2):
            new_user = save_user(email, password1)  

            login_user(new_user, remember=True)
            flash("Account created!", category="success")

            return redirect(url_for("views.home"))

    return render_template("signup.html", user=current_user)
