__author__ = 'Canon'
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.pagedown import PageDown
from flask.ext.bootstrap import Bootstrap
from flask_wtf.csrf import CsrfProtect
from flask_oauthlib.client import OAuth

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

oauth = OAuth()
bootstrap = Bootstrap()
csrf = CsrfProtect()
db = SQLAlchemy()
lm = LoginManager()
lm.session_protection = 'strong'
lm.login_view = 'auth.login'
pagedowm = PageDown()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    bootstrap.init_app(app)
    csrf.init_app(app)
    lm.init_app(app)
    db.init_app(app)
    oauth.init_app(app)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint, url_prefix='/blog')

    from instagram import instagram as instagram_blueprint
    app.register_blueprint(instagram_blueprint, url_prefix='/instagram')

    from gallery import gallery as gallery_blueprint
    app.register_blueprint(gallery_blueprint, url_prefix='/gallery')

    from photo import photo as photo_blueprint
    app.register_blueprint(photo_blueprint, url_prefix='/photo')

    from photo import photo as baysecret_blueprint
    app.register_blueprint(baysecret_blueprint, url_prefix='/baysecret')

    # with app.app_context():
    #     db.create_all()


    return app
