#This bluepint will deal with all user management functionality
from flask import Blueprint
main_blueprint = Blueprint('main', __name__, template_folder='templates', static_folder='static', static_url_path='static')

from . import views


