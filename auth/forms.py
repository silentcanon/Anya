__author__ = 'Canon'
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from ..models import User

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
        print self.username.data
        self.user = User.query.filter_by(username=self.username.data).first()
        if not self.user:
            self.username.errors = ("Invalid username",)
            return False
        if not self.user.verify_password(self.password.data):
            self.password.errors = ("Invalid password",)
            return False
        return True