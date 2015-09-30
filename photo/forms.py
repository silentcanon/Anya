__author__ = 'Canon'

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired

class photoForm(Form):
    title = StringField('Title', validators=[DataRequired])
    description = StringField('Description', validators=[DataRequired])
    image = FileField('Image', validators=[DataRequired])

