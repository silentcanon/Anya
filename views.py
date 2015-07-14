__author__ = 'Canon'
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from .forms import LoginForm, PostForm
from .models import User, Article
import datetime


@app.route('/')
@app.route('/index')
def index():
    user = g.user
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if not form.validate_on_submit():
        ##flash("Username or password invalid", 'Error')
        return render_template('login.html',title='Login',form = form)
    user = form.user
    login_user(user, remember=form.remember_me.data)
    flash("Login successfully")
    return redirect(url_for("hello"))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    user = g.user
    print user.id
    form = PostForm()
    if not form.validate_on_submit():
        return render_template('post.html',title='Add a post', form = form)
    title = form.title.data
    content_markdown = form.content_markdown.data
    allow_comment = form.allow_comment.data
    public = form.public.data
    create_time = datetime.datetime.utcnow()
    modified_time = create_time
    newArticle = Article(url_title = title, title = title, content_markdown = content_markdown,
                         allow_comment = allow_comment, create_time = create_time, modified_time = modified_time,
                         user_id = user.id, public = public)
    db.session.add(newArticle)
    db.session.commit()
    return redirect(url_for("hello"))


@app.route('/hello', methods=['GET','POST'])
@login_required
def hello():
    return render_template('hello.html')

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))



@app.before_request
def before_request():
    g.user = current_user


