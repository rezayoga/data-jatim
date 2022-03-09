"""
This contains the application factory for creating flask application instances.
Using the application factory allows for the creation of flask applications configured 
for different environments based on the value of the CONFIG_TYPE environment variable
"""

from asyncio.log import logger
import os
from flask import Flask, render_template
from flask_mail import Mail
from celery import Celery  # NEW!!!!!
from config import Config  # NEW!!!!!
import logging
from flask.logging import default_handler
from logging.handlers import RotatingFileHandler
from flask_sqlalchemy import SQLAlchemy
import bugsnag
from bugsnag.flask import handle_exceptions
from bugsnag.handlers import BugsnagHandler
import click

### Flask extension objects instantiation ###
mail = Mail()
db = SQLAlchemy()
### Instantiate Celery ###
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL,
                result_backend=Config.CELERY_RESULT_BACKEND)  # NEW!!!!!

bugsnag.configure(
    api_key="809b696a1aee8628288d17b65985c198",
    project_root=os.getcwd(),
)

### Application Factory ###


def create_app():

    app = Flask(__name__)

    # bug snag
    handle_exceptions(app)

    # Configure the flask app instance
    CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(CONFIG_TYPE)

    # Configure celery
    celery.conf.update(app.config)              # NEW!!!!!

    # Register blueprints
    register_blueprints(app)

    # Initialize flask extension objects
    initialize_extensions(app)

    # Configure logging
    configure_logging(app)

    # Register error handlers
    register_error_handlers(app)

    # Register SQLAlchemy
    initialize_database(app)

    @app.cli.command("create-user")
    @click.argument("username", nargs=1)
    @click.argument("fullname", nargs=1)
    @click.argument("password", nargs=1)
    def create_user(username, fullname, password):
        """Create a user."""
        print("Creating user: {}, {}, {}".format(username, fullname, password))
        from app.models import User
        from app.models import db
        db.create_all()
        user = User(username=username, fullname=fullname, password=password)
        db.session.add(user)
        db.session.commit()
        print("Created user: {}".format(user))

    return app


### Helper Functions ###
def register_blueprints(app):
    from app.auth import auth_blueprint
    from app.main import main_blueprint
    from app.api import api_blueprint

    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(auth_blueprint, url_prefix='/users')
    app.register_blueprint(main_blueprint)


def initialize_extensions(app):
    mail.init_app(app)


def initialize_database(app):
    from app.models import db
    db.init_app(app)


def register_error_handlers(app):

    # 400 - Bad Request
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('400.html'), 400

    # 403 - Forbidden
    @app.errorhandler(403)
    def forbidden(e):
        return render_template('403.html'), 403

    # 404 - Page Not Found
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    # 405 - Method Not Allowed
    @app.errorhandler(405)
    def method_not_allowed(e):
        return render_template('405.html'), 405

    # 500 - Internal Server Error
    @app.errorhandler(500)
    def server_error(e):
        return render_template('500.html'), 500


def configure_logging(app):

    # Deactivate the default flask logger so that log messages don't get duplicated
    # app.logger.removeHandler(default_handler)

    # Create a file handler object
    #file_handler = RotatingFileHandler('flaskapp.log', maxBytes=16384, backupCount=20)

    # Set the logging level of the file handler object so that it logs INFO and up
    # file_handler.setLevel(logging.INFO)

    # Create a file formatter object
    #file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s: %(lineno)d]')

    # Apply the file formatter object to the file handler object
    # file_handler.setFormatter(file_formatter)

    # Add file handler object to the logger
    # app.logger.addHandler(file_handler)

    logger = logging.getLogger("test.logger")

    handler = BugsnagHandler()
    # send only ERROR-level logs and above
    # handler.setLevel(logging.ERROR)
    # logger.addHandler(handler)

    logger.addFilter(handler.leave_breadcrumbs)
