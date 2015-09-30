__author__ = 'Canon'
from . import instagram, inst_client
from flask import Flask, redirect, url_for, session, request, jsonify, flash

@instagram.route("/", methods=['GET'])
def index():
    return ""


@instagram.route("/oauthorized",methods=['GET'])
def oauthorized():
    resp = inst_client.authorized_response()
    if resp is None:
        flash('You denied the request to sign in.')
    else:
        session['insta_oauth'] = resp
        print resp
    return redirect(url_for('instagram.index'))

@instagram.route('/login')
def login():
    callback_url = url_for('instagram.oauthorized', next=request.args.get('next'))
    return inst_client.authorize(callback='http://silentcanon.me' or request.referrer or None)