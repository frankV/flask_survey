from flask import Flask
from flask.ext.assets import Environment, Bundle
from flask_oauthlib.client import OAuth
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from flask.ext.mail import Mail
from config import basedir
import os

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)			
# assets = Environment(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

mail = Mail(app)




from app import views, models
