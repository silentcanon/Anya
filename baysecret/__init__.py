__author__ = 'Canon'
from flask import Blueprint

blog = Blueprint('baysecret',__name__)

from . import views