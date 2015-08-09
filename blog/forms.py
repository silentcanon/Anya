__author__ = 'Canon'

from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask.ext.pagedown.fields import PageDownField
from flask import request
import json
import urllib2
import urllib


class PostForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    content_markdown = PageDownField("Write something here", validators=[DataRequired()])
    allow_comment = BooleanField('Allow comment?', default=True)
    public = BooleanField('Public?', default=True)
    submit = SubmitField("Submit")

class EditForm(Form):
    title = StringField('Title', validators=[DataRequired('Title should not be empty')])
    content_html = StringField('Content', validators=[DataRequired('Content should not be empty')])
    allow_comment = BooleanField('Allow comment?', default=True)
    public = BooleanField('Public?', default=True)
    ##submit = SubmitField("Submit")

    # def validate(self):
    #     rv = Form.validate(self)
    #     if not rv:
    #         return False
    #     ar = Article.query.filter_by(url_title=self.title.data).first()
    #     if ar is not None:
    #         self.title.errors.append("This title is existed, please try another one")
    #         return False
    #     return True

    @staticmethod
    def constructFrom(article):
        editForm = EditForm
        editForm.title = article.title
        editForm.allow_comment = article.allow_comment
        editForm.public = article.public
        editForm.content_html = article.content_html
        return editForm


class CommentForm(Form):
    url_title = StringField('url_title', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired('Name should not be empty')])
    email = StringField('email', validators=[DataRequired('Email should not be empty')])
    comment = StringField('comment', validators=[DataRequired('Email should not be empty')])
    reply_to = StringField('reply_to')
    user_id = StringField('user_id')

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        recaptcha = request.form.get("g-recaptcha-response")

        data = {'secret': "6Lf6vQoTAAAAAIcVbvcQbJmrWyWV6FKsPDwdZ6_I",
                'response': recaptcha
                }
        req = urllib2.Request("https://www.google.com/recaptcha/api/siteverify")
        req.add_header("Content-type", "application/x-www-form-urlencoded")
        response = urllib2.urlopen(req, urllib.urlencode(data))
        res = json.load(response)
        if not res['success']:
            if res.get('error-codes'):
                self.errors.update({'recaptcha': res.get('error-codes')})
            return False
        return True


