__author__ = 'Canon'
from flask import render_template, redirect, url_for, flash
from flask.ext.login import login_user, logout_user, current_user
from .forms import LoginForm
from . import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user is not None and current_user.is_authenticated():
        return redirect(url_for('main.index'))
    form = LoginForm()
    if not form.validate_on_submit():
        return render_template('login.html', title='Login', form=form)
    user = form.user
    login_user(user, remember=form.remember_me.data)
    flash("Login successfully")
    return redirect(url_for("main.index"))

@auth.route('/logout')
def logout():
    flash("%s, you have been logged out" % current_user.username)
    logout_user()
    return redirect(url_for('main.index'))