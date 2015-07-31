__author__ = 'Canon'
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required

from utils import allowed_file
import datetime










@app.route("/api/photo/upload", methods=['GET','POST'])
def _photo_upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            print(filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "{success: 0}"
        return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form action="" method=post enctype=multipart/form-data>
          <p><input type=file name=file>
             <input type=submit value=Upload>
        </form>
        '''

@app.route("/photo/upload", methods=['GET','POST'])
def photo_upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            print(filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "{success: 0}"
        else:
            return "{error: 1}"
    return render_template('photo_upload.html')


@app.route('/hello', methods=['GET','POST'])
@login_required
def hello():
    return render_template('index.html')




@app.before_request
def before_request():
    g.user = current_user


