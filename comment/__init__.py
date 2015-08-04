__author__ = 'Canon'
from flask import Blueprint

blog = Blueprint('comment',__name__)

from . import views