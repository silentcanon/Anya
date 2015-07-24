__author__ = 'Canon'
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from flask.ext.pagedown import PageDown
from flask.ext.bootstrap import Bootstrap
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'


pagedown = PageDown()
pagedown.init_app(app)

bootstrap = Bootstrap(app)
from app import views, models