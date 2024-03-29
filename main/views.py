__author__ = 'Canon'
from . import main
from flask import render_template
from flask.ext.login import current_user

@main.route('/')
@main.route('/index')
def index():
    posts = [
        {
            'author': {'username': 'Canon'},
            'body': 'Beautiful day!'
        },
        {
            'author': {'username': 'Kanon'},
            'body': 'I am Canon!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           posts=posts)


@main.route('/about')
def about():
    return render_template('about.html')