from flask import Blueprint
from .metadata import TEMPLATE_FOLDER, STATIC_FOLDER
from core.utils.registry.roles import register_role
from core.utils.registry.side_navigation import register_sidebar_item, register_category

bp = Blueprint('pages', __name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER) 

from . import routes

def init_extension(app, db):
    with app.app_context():
        db.create_all()
    return bp 
