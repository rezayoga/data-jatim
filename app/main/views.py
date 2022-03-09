from . import main_blueprint
from flask import render_template, request, redirect, url_for, current_app, abort
from app.models import Ptsl


@main_blueprint.route('/')
def index():
    #data = Ptsl.query.all()
    current_app.logger.info("Index page loading")
    #return render_template('main/index.html', data=data)
    return "Hello, World!"


@main_blueprint.route('/admin')
def admin():
    abort(500)
