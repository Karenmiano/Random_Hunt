#!/usr/bin/env python3
"""
Contains the class File and defines an association table
user_files_read
"""
from datetime import datetime
from src import db

# association table
# will keep a clean record of files already displayed to user
user_files_read = db.Table(
    'user_files_read',
    db.Column('user_id', db.Integer,
              db.ForeignKey('users.id', onupdate='CASCADE',
                            ondelete='CASCADE'),
              primary_key=True),
    db.Column('file_id', db.Integer,
              db.ForeignKey('files.id', onupdate='CASCADE',
                            ondelete='CASCADE'),
              primary_key=True)
)


class File(db.Model):
    """
    Defines files table which will keep a record of pages
    available for display in templates/voyages
    """
    __tablename__ = "files"
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(128), unique=True, nullable=False)
    recorded_on = db.Column(db.DateTime, default=datetime.utcnow())
    users = db.relationship('User', secondary="user_files_read",
                            backref="files", viewonly=False)

    def __repr__(self):
        """
        Gives a more descriptive representation of the File instance
        """
        return f'Filename: {self.file_name}'
