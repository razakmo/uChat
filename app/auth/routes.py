from app.auth import bp
from flask import render_template, flash, redirect, url_for
from app.auth.forms import RegistrationForm
from app.models import User
from app import db


@bp.route('/login')
def login():
    return "Login Page"


@bp.route('/logout')
def logout():
    return "Logout Page"


@bp.route('/register', methods=['GET', 'POST'])
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
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))

    return render_template(
        'auth/register.html', form=form, title="Register")
