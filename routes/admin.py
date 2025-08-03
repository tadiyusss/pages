from .. import bp
from flask import render_template
from core.utils.decorators import role_required
from flask_login import login_required


@bp.route('/dashboard/contents', methods=['GET'])
@role_required(['Administrator', 'Editor'])
@login_required
def contents():
    return render_template('dashboard/contents.html')


@bp.route('/dashboard/contents/create', methods=['GET'])
@role_required(['Administrator', 'Editor'])
@login_required
def create_content():
    return render_template('dashboard/contents/create.html')