__author__ = 'Canon'
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask.ext.pagedown.fields import PageDownField
from .models import User



class LoginForm(Form):
    username = StringField("Username",validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    submit = SubmitField("Login")
    user = None

    def validate(self):
        ##if not Form.validate_on_submit(self):
        ##    return False
        self.user = User.query.filter_by(username = self.username.data, password = self.password.data).first()
        if not self.user:
            self.username.errors = ("Invalid username or password",)
            return False
        return True


class PostForm(Form):
    title = StringField('Title',validators=[DataRequired()])
    content_markdown = PageDownField("Write something here", validators=[DataRequired()])
    allow_comment = BooleanField('Allow Comment?', default=True)
    public = BooleanField('Public?', default=True)
    submit = SubmitField("Submit")


