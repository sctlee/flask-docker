import flask.ext.login as flask_login
from flask_login import login_user, logout_user
from models import User

login_manager = flask_login.LoginManager()
current_user = flask_login.current_user


@login_manager.user_loader
def user_loader(user_id):
    user = User.query.get(user_id)
    return user


def login(form):
    registered_user = User.query.filter_by(email=form.email.data, password=form.password.data).first()
    if registered_user is None:
        return False
    print(registered_user.username, registered_user.password)
    login_user(registered_user, True)
    return True


def logout():
    logout_user()


def signup(form):
    user = User(form.username.data, form.email.data, form.password.data)

    try:
        user.insert()
    except Exception as e:
        print(e)
        return False
    login_user(user)

    return True

# @login_manager.request_loader
# def request_loader(request):
#     email = request.form.get('email')
#     users = User.query.all()
#     if email not in users:
#         return
#
#     user = User()
#     user.id = email
#
#     # DO NOT ever store passwords in plaintext and always compare password
#     # hashes using constant-time comparison!
#     user.is_authenticated = request.form['pw'] == users[email]['pw']
#
#     return user
