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

from src.models.user import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()

@app.route("/")
def home():
    if current_user.is_authenticated:
        return redirect(url_for("voyages.displays"))
    return render_template("home.html", title="Home")

from src.models.files import File


from src.accounts.views import accounts_bp
from src.voyages.views import voyages_bp
app.register_blueprint(accounts_bp)
app.register_blueprint(voyages_bp)