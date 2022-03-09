from . import main_blueprint
from flask import render_template, request, redirect, url_for, current_app, abort
from app.models import Ptsl


@main_blueprint.route('/ptsl', defaults={'year': None, 'month': None})
@main_blueprint.route('/ptsl', defaults={'month': None})
@main_blueprint.route('/ptsl/<string:year>/<string:month>')
def ptsl(year, month):
    data = Ptsl.query.all()
    current_app.logger.info("Index page loading")
    return render_template('index.html', data=data)


@main_blueprint.route('/admin')
def admin():
    abort(500)
