__author__ = 'Canon'
from flask import Blueprint
from .. import oauth
from flask_oauthlib.client import OAuth, OAuthException

client_id = "7d6f30edaf824f709b8606a8dc495c25"
client_secret = "a4618523170b42c2b14b8fc0dc81bdd5"

instagram = Blueprint('instagram',__name__)

inst_client = oauth.remote_app(
    'instagram',
    consumer_key=client_id,
    consumer_secret=client_secret,
    base_url='https://api.instagram.com/v1/',
    request_token_url=None,
    access_token_url='https://api.instagram.com/oauth/access_token',
    access_token_method='POST',
    authorize_url='https://api.instagram.com/oauth/authorize'
)

from . import views