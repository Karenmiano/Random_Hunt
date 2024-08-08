#!/usr/bin/env python3
"""Defines a flask app instance."""
from flask_bcrypt import Bcrypt
from decouple import config
from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, current_user
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'accounts.login'

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models.user import User


@login_manager.user_loader
def load_user(user_id):
    """
    Callback will be used by Flask-Login to determine the user object
    to set current_user to.
    """
    return User.query.get(int(user_id))



@app.route("/")
def home():
    """
    Route to home page.

    If the user is authenticated, redirect them to pagedisplays,
    otherwise render the home.html template.
    """
    if current_user.is_authenticated:
        return redirect(url_for("voyages.displays"))
    return render_template("home.html", title="Home")

@app.route("/home")
def go_home():
    """Allows already authenticated users to return to home page."""
    return render_template("home.html", title="Home")


from app.accounts.views import accounts_bp
from app.voyages.views import voyages_bp
app.register_blueprint(accounts_bp)
app.register_blueprint(voyages_bp)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
