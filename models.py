__author__ = 'Canon'
from app import db
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from markdown import markdown
import bleach


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    # password = db.Column(db.String(120))
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, pwd):
        self.password_hash = generate_password_hash(pwd)

    def verify_password(self, pwd):
        return check_password_hash(self.password_hash, pwd)


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3


    def __repr__(self):
        return '<User %r>' % (self.username)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    url_title = db.Column(db.Unicode(300), index = True)
    title = db.Column(db.Unicode(300))
    content_html = db.Column(db.UnicodeText)
    content_markdown = db.Column(db.UnicodeText)
    brief_content = db.Column(db.UnicodeText)
    create_time = db.Column(db.DateTime, index = True)
    modified_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    allow_comment = db.Column(db.Boolean)
    public  = db.Column(db.Boolean)

    @staticmethod
    def on_change_body(target, value, oldvalue, initiator):
        allow_tags = ['a','abbr','acronym','b','blockquote','code','em',
                      'i','li','ol','pre','strong','ul','h1','h2','h3','p']
        target.content_html = bleach.linkify(bleach.clean(
            markdown(value,output_form='html'),
            tags=allow_tags,strip=True
        ))


    def __repr__(self):
        return '<Article %r>' % (self.title)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    username = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime)
    article_id = db.Column(db.Integer, index = True)
    content = db.Column(db.Unicode(300))
    parentCmt_id = db.Column(db.Integer, db.ForeignKey('comment.id'))

    def __repr__(self):
        return '<Comment %d>' % (self.id)



class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(10), index = True)

    def __repr__(self):
        return '<Tag %u>' % (self.name)


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name


class Relationship(db.Model):
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), primary_key=True, index=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), primary_key=True, index = True)

    def __repr__(self):
        return '<article %d -- tag %d>' % (self.article_id, self.tag_id)


db.event.listen(Article.content_markdown, 'set', Article.on_change_body)




