__author__ = 'Canon'

from . import gallery
from flask import jsonify
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

@gallery.route('/instagram/', methods=['GET','POST'])
def load_insta_json():
    endpoint = "https://api.instagram.com/v1/users/425261701/media/recent"
    count = request.args.get('count')
    next_max_id = request.args.get('max_id')
    client_id = "44a3704cf42b4a2eb8329cba1054b450"
    values = {'count': int(count),
              'client_id': client_id}
    if next_max_id:
        values['max_id'] = next_max_id
    data = urllib.urlencode(values)
    endpoint = endpoint + '?' + data
    req = urllib2.Request(endpoint)
    res = urllib2.urlopen(req)
    the_page = res.read()
    d = json.loads(the_page)
    return jsonify(d)
