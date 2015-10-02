__author__ = 'Canon'

from flask.ext.wtf import Form
from wtforms import StringField, FileField, IntegerField
from wtforms.validators import DataRequired

class photoForm(Form):
    title = StringField('title')
    x1 = IntegerField('x1', validators=[DataRequired()])
    x2 = IntegerField('x2', validators=[DataRequired()] )
    y1 = IntegerField('y1', validators=[DataRequired()])
    y2 = IntegerField('y2', validators=[DataRequired()])
    w = IntegerField('w', validators=[DataRequired()])
    h = IntegerField('h', validators=[DataRequired()])
    description = StringField('description')
    image_upload = FileField('image_upload', validators=[DataRequired()])

