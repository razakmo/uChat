from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField(
        'username_label', validators=[InputRequired(
            message="Username required"), Length(
            min=2, max=25, message="Username must be between 2 and 25 chars")])
    password = PasswordField(
        'password_label', validators=[InputRequired(
            message="Password required"), Length(
            min=4, max=25, message="Password must be at least 8 chars")])
    confirm_password = PasswordField(
        'confirm_password_label', validators=[InputRequired(
            message="Useraname required"), EqualTo(
            'password', message="Passwords must match")])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("This username has already been taken!")
