from . import main_blueprint
from app.models import Ptsl
import io
import random
from flask import render_template, abort, redirect, url_for, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import datetime
import os
import time
import pymysql
import pandas as pd
from neuralprophet import NeuralProphet, set_log_level
set_log_level("ERROR")


now = datetime.datetime.now()
# print now.year, now.month, now.day, now.hour, now.minute, now.second
os.environ['TZ'] = 'Asia/Jakarta'
time.tzset()


@main_blueprint.route('/')
def index():
    return redirect(url_for('main.ptsl'))


@main_blueprint.route('/ptsl', defaults={'year': None, 'month': None, 'date': None})
@main_blueprint.route('/ptsl/<year>/<month>', defaults={'date': None})
@main_blueprint.route('/ptsl/<year>/<month>/<date>')
def ptsl(year=None, month=None, date=None):
    y = time.strftime('%Y')
    m = time.strftime('%m')
    d = time.strftime('%d')

    data = Ptsl.query.filter_by(y=y, m=m, d=d).all()
    if year != None and month != None and date != None:
        y = year
        m = month
        d = date
        data = Ptsl.query.filter_by(y=year, m=month, d=date).all()
    elif year != None and month != None and date == None:
        abort(404)
    # current_app.logger.info("Index page loading")
    return render_template('index.html', data=data, y=y, m=m, d=d, base_url='/ptsl')


@main_blueprint.route('/ptsl/graph/<type>')
def trend(type):
    mysql_host = 'localhost'  # 'rezayogaswara.com'
    mysql_port = 3306
    mysql_user = 'root'  # 'reza'
    mysql_password = 'rezareza1985'  # 'password'
    mysql_database = 'db_data_jatim'

    config_mysql = {
        "host": mysql_host,
        "port": mysql_port,
        "user": mysql_user,
        "passwd": mysql_password,
        "charset": "utf8mb4",
        "cursorclass": pymysql.cursors.DictCursor,
        "database": mysql_database
    }

    connection = pymysql.connect(**config_mysql)
    df = None
    try:
        SQL_Query = pd.read_sql_query(
            '''SELECT
            puldadis AS y, DATE(created_at) AS ds
            from tb_progres_ptsl_kanwil WHERE kabupaten_kota = 'Total' ORDER BY id DESC''', connection)
        df = pd.DataFrame(SQL_Query, columns=['y', 'ds'])
        print(df)
        print('The data type of df is: ', type(df))
    except:
        print("Error: unable to convert the data")

    connection.close()
    m = NeuralProphet(trend_reg=1,
                      learning_rate=0.01,
                      yearly_seasonality=False,
                      weekly_seasonality=False,
                      daily_seasonality=False,)

    metrics = m.fit(df, freq="D", progress='plot')
    future = m.make_future_dataframe(df=df, periods=10)

    forecast = m.predict(df=future)
    fig_forecast = m.plot(forecast)
    fig_param = m.plot_parameters()
    fig_comp = m.plot_components(forecast)

    if type == 'forecast':
        fig = fig_forecast
    elif type == 'params':
        fig = fig_param
    elif type == 'comps':
        fig = fig_comp

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig


@main_blueprint.route('/admin')
def admin():
    abort(500)
