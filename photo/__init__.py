__author__ = 'Canon'
from flask import Blueprint


photo = Blueprint('photo',__name__)


from . import views