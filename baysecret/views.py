__author__ = 'Canon'
from . import baysecret
from flask import redirect, render_template, url_for, request
from flask.ext.login import login_required, current_user
import datetime
from app import utils
from app.decorators import admin_required, admin_required_json
from app import db
import json