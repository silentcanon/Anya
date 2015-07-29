__author__ = 'Canon'
from flask import flash
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask.ext.pagedown.fields import PageDownField
from .models import User, Article



class LoginForm(Form):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in', default=False)
    submit = SubmitField("Login")
    user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        self.user = User.query.filter_by(username = self.username.data).first()
        if not self.user:
            self.username.errors = ("Invalid username",)
            return False
        if not self.user.verify_password(self.password.data):
            self.password.errors = ("Invalid password",)
            return False
        return True


class PostForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    content_markdown = PageDownField("Write something here", validators=[DataRequired()])
    allow_comment = BooleanField('Allow Comment?', default=True)
    public = BooleanField('Public?', default=True)
    submit = SubmitField("Submit")

class EditForm(Form):
    title = StringField('Title', validators=[DataRequired('Title should not be empty')])
    content_html = StringField('Content', validators=[DataRequired('Content should not be empty')])
    allow_comment = BooleanField('Allow Comment?', default=True)
    public = BooleanField('Public?', default=True)
    ##submit = SubmitField("Submit")

    @staticmethod
    def constructFrom(article):
        editForm = EditForm
        editForm.title = article.title
        editForm.allow_comment = article.allow_comment
        editForm.public = article.public
        editForm.content_html = article.content_html
        return editForm











