from . import bp
from flask import render_template, redirect, url_for
from flask_login import login_required
from core.utils.decorators import role_required

@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@bp.route('/dashboard/contents', methods=['GET'])
def contents():
    return render_template('dashboard/contents.html')