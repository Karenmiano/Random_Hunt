"""
Defines the login and registration forms of app
"""
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from src.models.user import User


class RegistrationForm(FlaskForm):
    """Defines entries for the registration form"""
    email = EmailField(
        "Email", validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired()]
    )

    def validate(self, extra_validators=None):
        """Automatically called when form is submitted"""
        initial_validation = super(RegistrationForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("An account with this email already exists.")
            return False
        if self.password.data != self.confirm_password.data:
            self.password.errors.append("Passwords must match!")
            self.confirm_password.errors.append("Passwords must match!")
            return False
        return True


class LoginForm(FlaskForm):
    """Defines entries for login form"""
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
