from . import main_blueprint
from flask import render_template, request, redirect, url_for, current_app, abort
from app.models import Ptsl
import time
import datetime
import calendar
import os
now = datetime.datetime.now()
#print now.year, now.month, now.day, now.hour, now.minute, now.second
os.environ['TZ'] = 'Asia/Jakarta'
time.tzset()

@main_blueprint.route('/ptsl/', defaults={'year': None, 'month': None, 'date': None})
@main_blueprint.route('/ptsl/<string:year>/<string:month>/<string:date>')
def ptsl(year=None, month=None, date=None):
    data = Ptsl.query.filter_by(y=time.strftime('%Y'), m=time.strftime('%m'), d=time.strftime('%d')).all()
    if year != None and month != None:
        data = Ptsl.query.filter_by(y=year, m=month, d=date).all()
    #current_app.logger.info("Index page loading")
    return render_template('index.html', data=data)


@main_blueprint.route('/admin')
def admin():
    abort(500)
