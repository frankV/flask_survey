# -*- coding: utf-8 -*-

import os

PROJECT = "survey"

# Get app root path, also can use flask.root_path
PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

DEBUG = True
TESTING = False

ADMINS = ['youremail@yourdomain.com']

# http://flask.pocoo.org/docs/quickstart/#sessions
SECRET_KEY = 'youshouldreplacethis'

SQLALCHEMY_ECHO = True
DATABASE_QUERY_TIMEOUT = 15
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + PROJECT_ROOT + '/%s.sqlite' % PROJECT

MAIL_DEBUG = DEBUG
MAIL_SERVER = 'smtp.gmail.com'
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'gmail_username'
MAIL_PASSWORD = 'gmail_password'
DEFAULT_MAIL_SENDER = '%s@gmail.com' % MAIL_USERNAME
