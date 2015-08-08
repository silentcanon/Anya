__author__ = 'Canon'
from . import blog
from flask import redirect, render_template, url_for, request
from flask.ext.login import login_required, current_user
import datetime
from app import utils
from app.decorators import admin_required
from .forms import PostForm, EditForm, CommentForm
from ..models import Article, Comment
from app import db
import json



@blog.route('/postsimple', methods=['GET', 'POST'])
@login_required
@admin_required
def post():
    user = current_user
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

@blog.route('/post', methods=['GET','POST'])
@login_required
@admin_required
def post_article():
    user = current_user
    editForm = EditForm(request.form)
    if editForm.validate_on_submit():
        create_time = datetime.datetime.utcnow()
        title = editForm.title.data
        url_title = utils.generate_blog_url(create_time, title)
        content_html = editForm.content_html.data
        allow_comment = editForm.allow_comment.data
        public = editForm.public.data
        modified_time = create_time
        newArticle = Article(url_title=url_title, title=title, content_html=content_html,
                            allow_comment=allow_comment, create_time=create_time,
                            modified_time=modified_time, user_id=user.id, public=public)
        db.session.add(newArticle)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('blog_edit.html', editForm=editForm, func='new')




@blog.route("/archives/<url_title>")
def blog_view(url_title):
    article = Article.query.filter_by(url_title=url_title).first()
    commentForm = CommentForm(request.form)
    if article is None:
        return redirect(url_for("main.index"))
    return render_template("blog.html", article=article, commentForm=commentForm)


@blog.route("/archives/<url_title>/edit", methods=['GET', 'POST'])
@login_required
@admin_required
def blog_edit(url_title):
    article = Article.query.filter_by(url_title=url_title).first()
    if article is None:
        return redirect(url_for("main.index"))

    editForm = EditForm(request.form)

    if editForm.validate_on_submit():
        title = editForm.title.data
        content_html = editForm.content_html.data
        allow_comment = editForm.allow_comment.data
        public = editForm.public.data
        ## update article
        article.content_html = content_html
        article.title = title
        article.url_title = url_title
        article.allow_comment = allow_comment
        article.public = public
        article.modified_time = datetime.datetime.utcnow()
        db.session.commit()
        return redirect(url_for('main.index'))

    editForm.title.data = article.title
    editForm.content_html.data = article.content_html
    editForm.public.data = article.public
    editForm.allow_comment.data = article.allow_comment
    return render_template("blog_edit.html", editForm=editForm, func='edit')



@blog.route("/", defaults={'page_id': 1})
@blog.route("/page/", defaults={'page_id': 1})
@blog.route("/page/<int:page_id>")
def blog_overview(page_id):
    pagination = Article.query.order_by(Article.create_time.desc()).paginate(page_id, per_page=2, error_out=False)
    articles = pagination.items
    return render_template("blog_overview.html", articles=articles, pagination=pagination)



@blog.route("/comments/<url_title>", methods=['POST'])
def post_comment(url_title):
    commentForm = CommentForm()
    res = {"success": False}
    if commentForm.url_title.data != url_title:
        res.update({'errors': {'url_title' :'target blog inconsistent'}})
    elif commentForm.validate_on_submit():
        url_title = commentForm.url_title.data
        name = commentForm.name.data
        email = commentForm.email.data
        comment = commentForm.comment.data
        res['success'] = True
    else:
        res.update({'errors': commentForm.errors})
    return json.dumps(res)

@blog.route("/comments/<url_title>", methods=['GET'])
def get_comments(url_title):

    comments = Comment.query.filter_by(article_url_title=url_title).all()
    res = []
    for comment in comments:
        res.append(comment.toDict())
    print res
    json_res = json.dumps(res, indent=4, separators=(',', ':'))
    print json_res
    return json_res



@blog.route("/comments/test/<url_title>", methods=['GET'])
def commentViewTest(url_title):
    return render_template('commentTest.html', url_title=url_title)