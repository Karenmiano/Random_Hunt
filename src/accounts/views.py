"""
Defines blueprint used to handle user account 
    - Registration
    - Login
    - Logout
"""
from flask import Blueprint, flash, render_template, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from src import db, bcrypt
from src.accounts.forms import RegistrationForm, LoginForm
from src.models.user import User


accounts_bp = Blueprint("accounts", __name__)

@accounts_bp.route("/register", methods=["GET", "POST"])
def register():
    """Handles user Registration"""
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash("Thanks for registering!", "success")
        return redirect(url_for("voyages.displays"))
    return render_template("accounts/register.html", title="Register", form=form)

@accounts_bp.route("/login", methods=["GET", "POST"])
def login():
    """Login existing users"""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for("voyages.displays"))
        else:
            flash('Invalid email and/or password', 'signin')
            redirect(url_for("accounts.login"))
    return render_template("accounts/login.html", title="Login", form=form)

@accounts_bp.route("/logout")
@login_required
def logout():
    """
    Logs out the current user and redirects them
    to the home page.
    """
    logout_user()
    return redirect(url_for("go_home"))
