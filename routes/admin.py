from .. import bp
from flask import render_template

@bp.route('/dashboard/contents', methods=['GET'])
def contents():
    return render_template('dashboard/contents.html')


@bp.route('/dashboard/contents/create', methods=['GET'])
def create_content():
    return render_template('dashboard/contents/create.html')