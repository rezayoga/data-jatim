from . import main_blueprint
from app.models import Ptsl, KualitasDataLengkap, DataSiapElektronik, RekapWarkahDigital
import io
import xlwt
import random
from flask import render_template, abort, redirect, url_for, Response, request, session
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import datetime
from datetime import timedelta
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
    # abort(404)
    return redirect(url_for('main.ptsl'))


@main_blueprint.route('/ptsl', defaults={'year': None, 'month': None, 'date': None})
@main_blueprint.route('/ptsl/<year>/<month>', defaults={'date': None})
@main_blueprint.route('/ptsl/<year>/<month>/<date>')
def ptsl(year=None, month=None, date=None):

    y = time.strftime('%Y')
    m = time.strftime('%m')
    d = time.strftime('%d')

    # session.pop('y', None)
    # session.pop('m', None)
    # session.pop('d', None)

    y_now = time.strftime('%Y')
    m_now = time.strftime('%m')
    d_now = time.strftime('%d')

    data = Ptsl.query.filter_by(y=y, m=m, d=d).all()
    if year != None and month != None and date != None:
        y = year
        m = month
        d = date
        data = Ptsl.query.filter_by(y=year, m=month, d=date).all()
    elif year != None and month != None and date == None:
        abort(404)

    if session.get('y') == None:
        session['y'] = y
        session['m'] = '09'
        session['d'] = '01'

    # print(f"{session['y']}-{session['m']}-{session['d']}")

    # current_app.logger.info("Index page loading")
    shat = request.args.get('shat') if request.args.get(
        'shat') != None else 'puldadis'
    return render_template('index.html', data=data, y=y, m=m, d=d, base_url='/ptsl', shat=shat)


@main_blueprint.route('/ptsl/graph/<shat>/<type>')
def trend(shat, type):
    mysql_host = 'pusakha.id'  # 'rezayogaswara.com' #
    mysql_port = 3306
    mysql_user = 'reza'  # 'reza' #
    mysql_password = 'pmnP_AkjWk26x2020'  # 'password' #
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
            f"SELECT {shat} AS y, DATE(created_at) AS ds from tb_progres_ptsl WHERE kabupaten_kota = 'Total' ORDER BY id DESC", connection)
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

    # fig.suptitle(f"{shat.upper()}", fontsize=16, y=0.8)
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


def getCurrentDate(withTime=False):
    if (withTime):
        return '%s-%s-%s %s:%s:%s' % (time.strftime('%Y'), time.strftime('%m'), time.strftime('%d'), time.strftime('%H'), time.strftime('%M'), time.strftime('%S'))
    return '%s-%s-%s' % (time.strftime('%d'), month[int(time.strftime('%m')) - 1].upper(), now.year)


@main_blueprint.route('/transformasi_digital/kualitas_data_lengkap', defaults={'year': None, 'month': None, 'date': None})
@main_blueprint.route('/transformasi_digital/kualitas_data_lengkap/<year>/<month>', defaults={'date': None})
@main_blueprint.route('/transformasi_digital/kualitas_data_lengkap/<year>/<month>/<date>')
def transformasi_digital_kualitas_data_lengkap(year=None, month=None, date=None):
    return 'kualitas_data_lengkap'


@main_blueprint.route('/transformasi_digital/data_siap_elektronik', defaults={'year': None, 'month': None, 'date': None})
@main_blueprint.route('/transformasi_digital/data_siap_elektronik/<year>/<month>', defaults={'date': None})
@main_blueprint.route('/transformasi_digital/data_siap_elektronik/<year>/<month>/<date>')
def transformasi_digital_data_siap_elektronik(year=None, month=None, date=None):
    y = time.strftime('%Y')
    m = time.strftime('%m')
    d = time.strftime('%d')

    mysql_host = 'pusakha.id'  # 'rezayogaswara.com' #
    mysql_port = 3306
    mysql_user = 'reza'  # 'reza' #
    mysql_password = 'pmnP_AkjWk26x2020'  # 'password' #
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
    data = None
    try:
        with connection.cursor() as cur:
            # sql = f"SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));"
            # cur.execute(sql)

            sql = "SELECT * FROM `tb_data_siap_elektronik`"
            cur.execute(sql)
            data = cur.fetchall()
    finally:
        connection.close()

    return render_template('index_transformasi_digital_data_siap_elektronik.html', data=data, y=y, m=m, d=d, base_url='/transformasi_digital/data_siap_elektronik')


@main_blueprint.route('/download/data_siap_elektronik/excel')
def download_data_siap_elektronik_excel():
    mysql_host = 'pusakha.id'  # 'rezayogaswara.com' #
    mysql_port = 3306
    mysql_user = 'reza'  # 'reza' #
    mysql_password = 'pmnP_AkjWk26x2020'  # 'password' #
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
    data = None

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM tb_data_siap_elektronik_per_desa ORDER by id ASC")
            result = cursor.fetchall()

            """
            sql = f"INSERT INTO `tb_data_siap_elektronik_per_desa`(
                `id_kantah`,
                `kantor`,
                `desa_kelurahan`,
                `jumlah_bt`,
                `persen_bt_valid`,
                `jumlah_persil`,
                `persen_persil_valid`,
                `jumlah_siap_elektronik`,
                `persen_siap_elektronik`,
                `jumlah_su`,
                `persen_su_valid`,
                `jumlah_data_valid`,
                `persen_data_valid`,
                `bt_layanan_elektronik`,
                `persen_bt_layanan_elektronik`, `y`, `m`, `d`, `created_at`) VALUES
                ('{str(row['id_kantah'])}',
                '{str(index)}',
                '{ib}',
                '{float(row_berkas['Jumlah BT'])}',
                '{float(row_berkas['% BT Valid'])}',
                '{float(row_berkas['Jumlah Persil'])}',
                '{float(row_berkas['% Persil Valid'])}',
                '{float(row_berkas['Jumlah Siap Elektronik'])}',
                '{float(row_berkas['% Siap Elektronik'])}',
                '{float(row_berkas['Jumlah SU'])}',
                '{float(row_berkas['% SU Valid'])}',
                '{float(row_berkas['Jumlah Data Valid'])}',
                '{float(row_berkas['% Data Valid'])}',
                '{float(row_berkas['BT Layanan Elektronik'])}',
                '{float(row_berkas['% BT Layanan Elektronik'])}', '{getYear()}', '{getMonth()}', '{getDay()}', '{now}')"

            """
            # output in bytes
            output = io.BytesIO()
            # create WorkBook object
            workbook = xlwt.Workbook()
            # add a sheet
            sh = workbook.add_sheet(
                f'Data Siap Elektronik per {getCurrentDate()}')

            # add headers
            sh.write(0, 0, 'Id Kantor')
            sh.write(0, 1, 'Kantor')
            sh.write(0, 2, 'Desa / Kelurahan')
            sh.write(0, 3, 'Jumlah BT')
            sh.write(0, 4, '% BT Valid')
            sh.write(0, 5, 'Jumlah Persil')
            sh.write(0, 6, '% Persil Valid')
            sh.write(0, 7, 'Jumlah Siap Elektronik')
            sh.write(0, 8, '% Siap Elektronik')
            sh.write(0, 9, 'Jumlah SU')
            sh.write(0, 10, '% SU Valid')
            sh.write(0, 11, 'Jumlah Data Valid')
            sh.write(0, 12, '% Data Valid')
            sh.write(0, 13, 'BT Layanan Elektronik')
            sh.write(0, 14, '% BT Layanan Elektronik')

            idx = 0
            for row in result:
                sh.write(idx+1, 0, str(row['id_kantah']))
                sh.write(idx+1, 1, str(row['kantor']))
                sh.write(idx+1, 2, str(row['desa_kelurahan']))
                sh.write(idx+1, 3, str(row['jumlah_bt']))
                sh.write(idx+1, 4, str(row['persen_bt_valid']))
                sh.write(idx+1, 5, str(row['jumlah_persil']))
                sh.write(idx+1, 6, str(row['persen_persil_valid']))
                sh.write(idx+1, 7, str(row['jumlah_siap_elektronik']))
                sh.write(idx+1, 8, str(row['persen_siap_elektronik']))
                sh.write(idx+1, 9, str(row['jumlah_su']))
                sh.write(idx+1, 10, str(row['persen_su_valid']))
                sh.write(idx+1, 11, str(row['jumlah_data_valid']))
                sh.write(idx+1, 12, str(row['persen_data_valid']))
                sh.write(idx+1, 13, str(row['bt_layanan_elektronik']))
                sh.write(idx+1, 14, str(row['persen_bt_layanan_elektronik']))
                idx += 1

            workbook.save(output)
            output.seek(0)

            return Response(output, mimetype="application/ms-excel", headers={"Content-Disposition": "attachment;filename=employee_report.xls"})

    except Exception as e:
        print(e)

    finally:
        connection.close()


@ main_blueprint.route('/transformasi_digital', defaults={'year': None, 'month': None, 'date': None})
@ main_blueprint.route('/transformasi_digital/<year>/<month>', defaults={'date': None})
@ main_blueprint.route('/transformasi_digital/<year>/<month>/<date>')
def transformasi_digital(year=None, month=None, date=None):
    y=time.strftime('%Y')
    m=time.strftime('%m')
    d=time.strftime('%d')

    kdl=KualitasDataLengkap.query.filter_by(y=y, m=m, d=d).all()
    if year != None and month != None and date != None:
        y=year
        m=month
        d=date
        kdl=KualitasDataLengkap.query.filter_by(
            y=year, m=month, d=date).all()
    elif year != None and month != None and date == None:
        abort(404)

    dse=DataSiapElektronik.query.filter_by(y=y, m=m, d=d).all()
    if year != None and month != None and date != None:
        y=year
        m=month
        d=date
        dse=DataSiapElektronik.query.filter_by(
            y=year, m=month, d=date).all()
    elif year != None and month != None and date == None:
        abort(404)

    rwd=RekapWarkahDigital.query.filter_by(y=y, m=m, d=d).all()
    if year != None and month != None and date != None:
        y=year
        m=month
        d=date
        rwd=RekapWarkahDigital.query.filter_by(
            y=year, m=month, d=date).all()
    elif year != None and month != None and date == None:
        abort(404)

    return render_template('index_transformasi_digital.html', kdl=kdl, dse=dse, rwd=rwd, y=y, m=m, d=d, base_url='/transformasi_digital')
