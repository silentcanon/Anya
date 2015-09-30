__author__ = 'Canon'
from flask import Blueprint

gallery = Blueprint('gallery',__name__)
client_id = "7d6f30edaf824f709b8606a8dc495c25"

from . import views

