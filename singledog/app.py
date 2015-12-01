from flask import Flask,g
from views.welcome import welcome_page
from views.auth import auth_page
from models import db
from auth.auth import login_manager, current_user


def create_app():
    app = Flask(__name__)
    app.secret_key = 'super~~~~~~~~~~~~'

    # url
    app.register_blueprint(welcome_page)
    app.register_blueprint(auth_page)

    # db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sctlee:123456@192.168.99.100:3306/singledog'
    db.init_app(app)

    from models import User
    db.create_all(app=app)

    # login manager
    login_manager.init_app(app)

    @app.before_request
    def before_request():
        g.user = current_user

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
