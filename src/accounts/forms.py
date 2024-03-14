"""
Defines the login and registration forms of app
"""
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from src.accounts.models import User


class RegistrationForm(FlaskForm):
    """Defines entries for the registration form"""
    email = EmailField(
        "Email", validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm_password = PasswordField(
        "Repeat Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match")
        ]
    )

    def validate(self, extra_validators=None):
        """Automatically called when form is submitted"""
        initial_validation = super(RegistrationForm, self).validate()
        print(self.email.errors)
        print(self.password.errors)
        print(self.confirm_password.errors)
        print(initial_validation)
        if not initial_validation:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        if self.password.data != self.confirm_password.data:
            self.confirm_password.errors.append("Passwords must match")
            return False
        return True


class LoginForm(FlaskForm):
    """Defines entries for login form"""
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
