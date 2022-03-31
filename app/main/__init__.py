# This bluepint will deal with all user management functionality
from flask import Blueprint
from sqlalchemy import text, create_engine
from app.models import Ptsl, KualitasDataLengkap, DataSiapElektronik, RekapWarkahDigital

main_blueprint = Blueprint('main', __name__, template_folder='templates', static_folder='static',
                           static_url_path='/main.static')

def get_data(string_sql):
    engine = create_engine(
        "mysql+pymysql://root:rezareza1985@localhost/db_data_jatim")
    sql = text(string_sql)
    result = engine.execute(sql).fetchone()
    return result

main_blueprint.add_app_template_global(get_data, 'get_data')
from . import views
