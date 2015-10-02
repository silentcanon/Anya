__author__ = 'Canon'
from . import photo
from flask import redirect, render_template, url_for, request
from flask.ext.login import login_required, current_user
from app.decorators import admin_required, admin_required_json
from .forms import photoForm
from ..utils import crop_save_img

from app import db
import json

@photo.route('/upload', methods=['GET','POST'])
@login_required
@admin_required
def photo_uploder():
    photo_form = photoForm()
    if not photo_form.validate_on_submit():
        return render_template('photo_uploader.html', photoForm=photo_form)
    title = photo_form.title.data
    description = photo_form.description.data
    x1 = photo_form.x1.data
    y1 = photo_form.y1.data
    x2 = photo_form.x2.data
    y2 = photo_form.y2.data
    photo = request.files['image_upload']
    filename = photo.filename
    photo_byte = photo.read()

    crop_save_img(filename, photo_byte, x1, y1, x2, y2)

    return redirect(url_for('gallery.index'))

