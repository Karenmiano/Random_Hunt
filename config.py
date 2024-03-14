"""
Separates app settings for development and production
"""
from decouple import config


class Config():
    """General configurations for development and production"""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = config("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = config("DATABASE_URL")
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 13


class DevelopmentConfig(Config):
    """Overrides Config's settings to allow debug mode"""
    DEBUG = True
