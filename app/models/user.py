#!/usr/bin/env python3
"""
Holds the User class for model.
"""
from datetime import datetime
from flask_login import UserMixin
from app import bcrypt, db


class User(UserMixin, db.Model):
    """User model for recording users in database."""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, email, password):
        """
        Initializes a new User instance, accomodates password hashing.
        """
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def __repr__(self):
        """
        Gives a more descriptive representation of the User instance.
        """
        return f'<email: {self.email}>'
