from .. import bp
from flask import render_template

@bp.route('/dashboard/contents', methods=['GET'])
def contents():
    return render_template('dashboard/contents.html')
