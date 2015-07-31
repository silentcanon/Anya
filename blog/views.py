__author__ = 'Canon'
from . import blog
from flask import redirect, render_template, url_for, request
from flask.ext.login import login_required, current_user
from datetime import datetime
from app.decorators import admin_required
from .forms import PostForm, EditForm
from ..models import Article
from app import db



@blog.route('/post', methods=['GET', 'POST'])
@login_required
@admin_required
def post():
    user = current_user
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
    return redirect(url_for(request.args.next) or url_for("main.index"))

@blog.route('/postnew', methods=['GET','POST'])
@login_required
@admin_required
def post_article():
    editForm = EditForm(request.form)
    if editForm.validate_on_submit():
        print(editForm.content_html.data)
        return redirect(url_for('main.index'))

    return render_template('blog_edit.html', editForm=editForm, func='new')




@blog.route("/archives/<url_title>")
def blog_view(url_title):
    article = Article.query.filter_by(url_title=url_title).first()
    if article is None:
        return redirect(url_for("main.index"))
    return render_template("blog.html", article=article)


@blog.route("/archives/<url_title>/edit", methods=['GET', 'POST'])
@login_required
@admin_required
def blog_edit(url_title):
    article = Article.query.filter_by(url_title=url_title).first()
    if article is None:
        return redirect(url_for("main.index"))

    editForm = EditForm(request.form)
    editForm.title.data = article.title
    editForm.content_html.data = article.content_html
    editForm.public.data = article.public
    editForm.allow_comment.data = article.allow_comment
    if request.method == 'POST' and editForm.validate():
        print(editForm.content_html.data)
        return redirect(url_for('main.index'))
    else:
        if editForm.errors:
            print editForm.errors
    return render_template("blog_edit.html", editForm=editForm, func='edit')


    # article.content_html = editForm.content_html.data
    # article.title = editForm.title.data
    # article.modified_time = datetime.datetime.utcnow()
    # db.session.commit()


@blog.route("/", defaults={'page_id': 1})
@blog.route("/page/", defaults={'page_id': 1})
@blog.route("/page/<int:page_id>")
def blog_overview(page_id):
    pagination = Article.query.order_by(Article.create_time.desc()).paginate(page_id, per_page=2, error_out=False)
    articles = pagination.items
    return render_template("blog_overview.html", articles=articles, pagination=pagination)