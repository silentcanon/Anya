__author__ = 'Canon'
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.pagedown import PageDown
from flask.ext.bootstrap import Bootstrap

# app = Flask(__name__)
# app.config.from_object('config')
# db = SQLAlchemy(app)
#
# lm = LoginManager()
# lm.init_app(app)
# lm.login_view = 'login'
#
#
# pagedown = PageDown()
# pagedown.init_app(app)
#
# bootstrap = Bootstrap(app)
# from app import views, models

bootstrap = Bootstrap()
db = SQLAlchemy()
lm = LoginManager()
lm.session_protection = 'strong'
lm.login_view = 'auth.login'
pagedowm = PageDown()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    bootstrap.init_app(app)
    lm.init_app(app)
    db.init_app(app)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')


    return app
