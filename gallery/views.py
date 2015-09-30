__author__ = 'Canon'

from . import gallery
import urllib
import urllib2

from flask import redirect, render_template, url_for, request
from flask.ext.login import login_required, current_user
import datetime
from app import utils
from app.decorators import admin_required, admin_required_json
from ..models import Article, Comment, User, BlogStat
from app import db
import json

@gallery.route('/',methods=['GET'])
def index():
    return render_template("gallery.html")

