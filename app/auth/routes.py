from flask import flash, redirect, render_template, url_for

from app import db
from app.auth import bp
from app.auth.forms import RegistrationForm
from app.models import User


@bp.route("/login")
def login():
    return "Login Page"


@bp.route("/logout")
def logout():
    return "Logout Page"


@bp.route("/register", methods=["GET", "POST"])
def register():
    """Registration

    Register a new user

    Decorators:
        bp.route

    Returns:
        register.html -- register template
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", form=form, title="Register")
