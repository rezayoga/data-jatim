#!/usr/bin/env python

import os
from dotenv import load_dotenv
load_dotenv()


# Find the absolute file path to the top level project directory
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Base configuration class. Contains default configuration settings + configuration settings applicable to all environments.
    """
    # Default settings
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True
    JSONIFY_PRETTYPRINT_REGULAR = True

    # Settings applicable to all environments
    SECRET_KEY = os.getenv(
        'SECRET_KEY', default='86646d816e17821a367f0f81897a2c4851ec088723d31ae9b9e87ed967475f4b')

    MAIL_SERVER = 'mail.rezayogaswara.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    # MAIL_USERNAME = os.getenv('MAIL_USERNAME', default='me@rezayogaswara.com')
    MAIL_USERNAME = 'me@rezayogaswara.com'
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', default='Rezay0ga@85')
    MAIL_DEFAULT_SENDER = 'me@rezayogaswara.com'
    #MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME', default='Reza Yogaswara')
    MAIL_SUPPRESS_SEND = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
    CELERY_RESULT_BACKEND = os.getenv(
        'CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
    JSONIFY_PRETTYPRINT_REGULAR = True


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'dev.db')
   # SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://postgres:{os.getenv('DB_PASSWORD')}@postgres:5432/dev_db"


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    MAIL_SUPPRESS_SEND = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'test.db')
   # SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://postgres:{os.getenv('DB_PASSWORD')}@postgres:5432/test_db"


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    # Postgres database URL has the form postgresql://username:password@hostname/database
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'PROD_DATABASE_URl', default="sqlite:///" + os.path.join(basedir, 'prod.db'))
