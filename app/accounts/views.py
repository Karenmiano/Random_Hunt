#!/usr/bin/env python3
"""
Defines blueprint used to handle user account
    - Registration
    - Login
    - Logout
"""
from flask import Blueprint, flash, render_template, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import db, bcrypt
from app.accounts.forms import RegistrationForm, LoginForm
from app.models.user import User


accounts_bp = Blueprint("accounts", __name__)

@accounts_bp.route("/register", methods=["GET", "POST"])
def register():
    """
    Handles user Registration.
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        # show registration status and then redirect again to displays
        return render_template("accounts/success.html")
    return render_template("accounts/register.html",
                           title="Register",
                           form=form)


@accounts_bp.route("/login", methods=["GET", "POST"])
def login():
    """
    Login existing users

    Redirects to the voyage pages if successful, else renders
    the login page again.
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for("voyages.displays"))
        else:
            flash('Invalid email and/or password', 'signin')
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
