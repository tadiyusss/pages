from flask import Blueprint
from .metadata import TEMPLATE_FOLDER, STATIC_FOLDER
from .initialization.sidebar import register_sidebar_items

bp = Blueprint('pages', __name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER) 

from .routes import admin, public

def init_extension(app, db):
    with app.app_context():
        db.create_all()
        register_sidebar_items()
    return bp 
