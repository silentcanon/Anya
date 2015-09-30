__author__ = 'Canon'
from . import blog
from flask import redirect, render_template, url_for, request
from flask.ext.login import login_required, current_user
import datetime
from app import utils
from app.decorators import admin_required, admin_required_json
from .forms import PostForm, EditForm, CommentForm
from ..models import Article, Comment, User, BlogStat
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




@blog.route("/archives/<url_title>", methods=['GET'])
def blog_view(url_title):
    article = Article.query.filter_by(url_title=url_title).first()
    commentForm = CommentForm(request.form)
    if article is None:
        return redirect(url_for("main.index"))
    ip = request.remote_addr
    ##print ip
    article_id = article.id
    visit_time = datetime.datetime.utcnow()
    ##print article_id
    ##print visit_time

    ##blogStat = BlogStat(blog_id=int(article.id), ip=ip, visit_time=datetime.datetime.utcnow())
    ##db.session.add(blogStat)
    ##db.session.commit()
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


@blog.route("/archives/<url_title>/remove", methods=['GET'])
@login_required
@admin_required_json
def blog_remove(url_title):
    res = {"success": False}
    article = Article.query.filter_by(url_title=url_title).first()
    if article is None:
        res['error': 'Article not Existed']
        return json.dumps(res)
    db.session.delete(article)
    Comment.query.filter_by(article_url_title=url_title).delete()
    db.session.commit()
    res["success"] = True
    return json.dumps(res)




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
        if commentForm.reply_to.data:
            reply_to_id = commentForm.reply_to.data
            cmt = Comment.query.get(reply_to_id)
            assert(cmt.article_url_title == url_title)
        else:
            reply_to_id = None
        if commentForm.user_id.data:
            user_id = commentForm.user_id.data
            assert(int(user_id) == current_user.id)
        else:
            user_id = None
        now = datetime.datetime.utcnow()
        id = utils.generate_blog_comment_id(now, user_id, url_title)
        comment = Comment(id=id, user_id=user_id, username=name, timestamp=now,
                          article_url_title=url_title, content=comment, parentCmt_id=reply_to_id)
        db.session.add(comment)
        db.session.commit()
        res['success'] = True
        res['id'] = id
    else:
        res.update({'errors': commentForm.errors})
    return json.dumps(res)

@blog.route("/comments/<url_title>", methods=['GET'])
def get_comments(url_title):
    comments = Comment.query.filter_by(article_url_title=url_title).all()
    res = []
    for comment in comments:
        res.append(comment.toDict())
    json_res = json.dumps(res, indent=4, separators=(',', ':'))
    return json_res



@blog.route("/comments/test/<url_title>", methods=['GET'])
def commentViewTest(url_title):
    return render_template('commentTest.html', url_title=url_title)