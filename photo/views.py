__author__ = 'Canon'
from . import photo
from flask import redirect, render_template, url_for, request
from flask.ext.login import login_required, current_user
import datetime
from app.decorators import admin_required, admin_required_json
from .forms import photoForm

from app import db
import json

@photo.route('/upload', methods=['GET','POST'])
@login_required
@admin_required
def photo_uploder():
    photo_form = photoForm()
    if not photo_form.validate_on_submit():
        return render_template('photo_uploader.html')