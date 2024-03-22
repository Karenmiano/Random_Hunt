"""
Defines blueprint used to display pages to user.
"""
from flask import Blueprint, url_for, render_template, redirect
from flask_login import login_required, current_user
from sqlalchemy.sql.expression import func
from src import db
from src.models.files import user_files_read, File

voyages_bp = Blueprint("voyages", __name__)


@voyages_bp.route("/displays")
@login_required
def displays():
    """
    Route for choosing the content to display to user
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
