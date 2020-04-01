from app.auth import bp
from flask import render_template
from app.auth.forms import RegistrationForm


@bp.route('/login')
def login():
    return "Login Page"


@bp.route('/logout')
def logout():
    return "Logout Page"


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return "Great All Clear"
    return render_template(
        'auth/register.html', form=form, title="Register")
