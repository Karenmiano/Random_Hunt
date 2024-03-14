from flask import Blueprint, flash, render_template, request
from flask_login import current_user, login_user
from src import db, bcrypt
from src.accounts.forms import RegistrationForm, LoginForm
from src.accounts.models import User


accounts_bp = Blueprint("accounts", __name__)

@accounts_bp.route("/register", methods=["GET", "POST"])
def register():
    # if current_user.is_authenticated:
    #     return render_template("home.html")
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash("You are now a registered user. Welcome!")
        return render_template("home.html")
    return render_template("register.html", title="Register", form=form)
