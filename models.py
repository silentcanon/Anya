__author__ = 'Canon'
from app import db, lm
from flask.ext.login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from markdown import markdown
import bleach

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.Integer, db.ForeignKey('role.id'))

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, pwd):
        self.password_hash = generate_password_hash(pwd)

    def verify_password(self, pwd):
        return check_password_hash(self.password_hash, pwd)


    def can(self, permissions):
        if self.role is None:
            return False
        myRole = Role.query.get(self.role)
        return myRole is not None and (myRole.permissions & permissions) == permissions

    def is_admin(self):
        return self.can(Permission.ROOT)

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

class AnonymousUser(AnonymousUserMixin):
    def is_active(self):
        return False

    def is_authenticated(self):
        return False

    def is_anonymous(self):
        return True

    def can(self, permission):
        return False

    def is_admin(self):
        return False




class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_title = db.Column(db.String(300), primary_key=True)
    title = db.Column(db.Unicode(300))
    content_html = db.Column(db.UnicodeText)
    brief_content = db.Column(db.UnicodeText)
    create_time = db.Column(db.DateTime, index=True)
    modified_time = db.Column(db.DateTime)
    allow_comment = db.Column(db.Boolean, default=True)
    public = db.Column(db.Boolean, default=True)
    removed = db.Column(db.Boolean, default=False)
    is_brief = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    @staticmethod
    def on_change_body(target, value, oldvalue, initiator):
        allow_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em',
                      'i', 'li', 'ol', 'pre', 'strong', 'ul', 'h1', 'h2', 'h3', 'p', 'embed', 'script']
        target.content_html = bleach.linkify(bleach.clean(
            markdown(value, output_form='html'),
            tags=allow_tags, strip=True
        ))

    def __repr__(self):
        return '<Article %r>' % (self.title)


class Comment(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    username = db.Column(db.Unicode(64))
    timestamp = db.Column(db.DateTime)
    article_url_title = db.Column(db.String(300), db.ForeignKey('article.url_title'))
    content = db.Column(db.Unicode(300))
    parentCmt_id = db.Column(db.String(20), db.ForeignKey('comment.id'))

    def toDict(self):
        d = {
            'id': self.id,
            'user_id': self.user_id,
            'username': self.username,
            'timestamp': self.timestamp.isoformat(),
            'article_url_title': self.article_url_title,
            'content': self.content,
            'parentCmt_id': self.parentCmt_id
        }
        return d

    def __repr__(self):
        return '<comment %d>' % (self.id)





class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False)
    permissions = db.Column(db.Integer)

    @staticmethod
    def insertRoles():
        roles = {
            'User': (Permission.COMMENT, True),
            'Friend': (Permission.COMMENT | Permission.SHOW_HIDDEN, False),
            'ROOT': (0xff, False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()


    def __repr__(self):
        return '<Role %r>' % self.name

class Permission:
    COMMENT = 0x01
    SHOW_HIDDEN = 0x02
    WRITE = 0x04
    ROOT = 0x80



class Tag(db.Model):
    __tablename__ = 'tag'
    # id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(10), primary_key=True)

    @staticmethod
    def getAllTags():
        tagList = Tag.query.all()
        result = [t.name for t in tagList]
        return result

    @staticmethod
    def addTags(tags):
        oriTagList = Tag.getAllTags()
        for t in tags:
            if t not in oriTagList:
                newTag = Tag(name=t)
                db.session.add(newTag)
        db.session.commit()

    def __repr__(self):
        return '<Tag %u>' % self.name

class Relationship(db.Model):
    __tablename__ = 'relationship'
    article_url_title = db.Column(db.String(300), db.ForeignKey('article.url_title'), primary_key=True, index=True)
    tag_name = db.Column(db.Unicode(10), db.ForeignKey('tag.name'), primary_key=True, index=True)

    def __repr__(self):
        return '<article %d -- tag %d>' % (self.article_id, self.tag_name)



class BlogStat(db.Model):
    __tablename__ = 'blogstat'
    id = db.Column(db.String(32), primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('article.id'), index=True)
    ip = db.Column(db.String(20))
    visit_time = db.Column(db.DateTime)


class PhotoInfo(db.Model):
    __tablename__ = "photoinfo"
    photo_id = db.Column(db.String(64), primary_key=True)
    title = db.Column(db.Unicode(64))
    upload_time = db.Column(db.DateTime)
    ## todo




@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

lm.anonymous_user = AnonymousUser




