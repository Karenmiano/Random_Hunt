#!/usr/bin/env python
"""
Defines blueprint that holds route used to display pages to user.
"""
from flask import Blueprint, url_for, render_template, redirect
from flask_login import login_required, current_user
from sqlalchemy.sql.expression import func
from app import db
from app.models.files import user_files_read, File

voyages_bp = Blueprint("voyages", __name__)


@voyages_bp.route("/displays")
@login_required
def displays():
    """
    Route for choosing the content to display to user.

    The content displayed is random and mostly unique to user.

    Pages already seen by user are determined from junction table
    between user and files, then used to isolate them from all existing
    files. The random_page is then chosen from the remaining files.

    If no unseen files are found the user's seen files list is emptied to
    allow the process to start again
    """
    seen_pages_ids = db.session.query(user_files_read.c.file_id) \
                     .filter(user_files_read.c.user_id == current_user.id) \
                     .subquery()
    random_page = File.query.filter(File.id.notin_(seen_pages_ids)) \
                  .order_by(func.random()).first()
    if random_page:
        current_user.files.append(random_page)
        db.session.commit()
        return render_template(f'voyages/{random_page.file_name}')
    else:
        current_user.files = []
        db.session.commit()
        return redirect(url_for("voyages.displays"))
