from auth.form import LoginForm, RegistrationForm
from auth import auth

from flask import url_for, render_template, request, flash, redirect, Blueprint, g


auth_page = Blueprint('auth_page', __name__)


@auth_page.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class

        if auth.login(form):
            flash('Logged in successfully.')
            arg_next = request.args.get('next')
            # # next_is_valid should check if the user has valid
            # # permission to access the `next` url
            # if not next_is_valid(next):
            #     return flask.abort(400)
            return redirect(arg_next or url_for('welcome_page.index'))

    return render_template('auth/login.html', form=form)


@auth_page.route('/logout')
def logout():
    auth.logout()
    return redirect(url_for('welcome_page.index'))


@auth_page.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        if auth.signup(form):
            flash('Signuped in successfully.')
            arg_next = request.args.get('next')
            # # next_is_valid should check if the user has valid
            # # permission to access the `next` url
            # if not next_is_valid(next):
            #     return flask.abort(400)
            return redirect(arg_next or url_for('welcome_page.index'))

    return render_template('auth/signup.html', form=form)
