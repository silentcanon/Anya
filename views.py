__author__ = 'Canon'
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from .forms import LoginForm, PostForm, EditForm
from .models import User, Article, Permission
from decorators import admin_required
from utils import allowed_file
import datetime



@app.route('/')
@app.route('/index')
def index():
    user = g.user
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
                           user=user,
                           posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if not form.validate_on_submit():
        ##flash("Username or password invalid", 'Error')
        return render_template('login.html', title='Login', form=form)
    user = form.user
    login_user(user, remember=form.remember_me.data)
    flash("Login successfully")
    return redirect(url_for("hello"))

@app.route('/logout')
def logout():
    flash("%s, you have been logged out" % g.user.username)
    logout_user()
    return redirect(url_for('index'))


@app.route('/post', methods=['GET', 'POST'])
@login_required
@admin_required
def post():
    user = g.user
    print user.id
    form = PostForm()
    if not form.validate_on_submit():
        return render_template('post.html', title='Add a post', form=form)
    title = form.title.data
    content_markdown = form.content_markdown.data
    allow_comment = form.allow_comment.data
    public = form.public.data
    create_time = datetime.datetime.utcnow()
    modified_time = create_time
    newArticle = Article(url_title=title, title=title, content_markdown=content_markdown,
                         allow_comment=allow_comment, create_time=create_time,
                         modified_time=modified_time, user_id=user.id,
                         public=public)
    db.session.add(newArticle)
    db.session.commit()
    return redirect(url_for(request.args.next) or url_for("hello"))

@app.route('/postnew', methods=['GET','POST'])
@login_required
@admin_required
def post_article():
    user = g.user
    editForm = EditForm(request.form)
    if request.method == 'POST' and editForm.validate():
        print(editForm.content_html.data)
        return redirect(url_for('index'))
    elif editForm.errors is not None:
        flash('Unknown error', 'error')

    return render_template('blog_edit.html', editForm=editForm, func='new')




@app.route("/blog/archives/<url_title>")
def blog(url_title):
    article = Article.query.filter_by(url_title=url_title).first()
    if article is None:
        return redirect(url_for("index"))
    return render_template("blog.html", article=article)

@app.route("/blog/archives/<url_title>/edit", methods=['GET','POST'])
@login_required
@admin_required
def blog_edit(url_title):
    article = Article.query.filter_by(url_title=url_title).first()
    if article is None:
        return redirect(url_for("index"))

    editForm = EditForm(request.form)
    editForm.title.data = article.title
    editForm.content_html.data = article.content_html
    editForm.public.data = article.public
    editForm.allow_comment.data = article.allow_comment
    if request.method == 'POST' and editForm.validate():
        print(editForm.content_html.data)
        return redirect(url_for('index'))
    else:
        if editForm.errors:
            print editForm.errors
    return render_template("blog_edit.html", editForm=editForm, func='edit')


    # article.content_html = editForm.content_html.data
    # article.title = editForm.title.data
    # article.modified_time = datetime.datetime.utcnow()
    # db.session.commit()


@app.route("/blog/", defaults={'page_id': 1})
@app.route("/blog/page/", defaults={'page_id': 1})
@app.route("/blog/page/<int:page_id>")
def blog_overview(page_id):
    pagination = Article.query.order_by(Article.create_time.desc()).paginate(page_id, per_page=2, error_out=False)
    articles = pagination.items
    return render_template("blog_overview.html", articles=articles, pagination=pagination)

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

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))



@app.before_request
def before_request():
    g.user = current_user


