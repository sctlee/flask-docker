from flask import Flask,g
from views.welcome import welcome_page
from views.auth import auth_page
from models import db
from auth.auth import login_manager, current_user
import socket
import os


def create_app():
    app = Flask(__name__)
    app.secret_key = 'super~~~~~~~~~~~~'

    # url
    app.register_blueprint(welcome_page)
    app.register_blueprint(auth_page)

    # db
    if socket.gethostname() == 'lihaichuangdeMac-mini.local':
        print(1)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sctlee:123456@192.168.99.100:3306/singledog'
    else:
        print(2)
        conn_string = 'mysql+pymysql://%s:%s@%s:%s/%s' % (os.getenv('MYSQL_USERNAME'), os.getenv('MYSQL_PASSWORD'),\
                      os.getenv('MYSQL_PORT_3306_TCP_ADDR'), os.getenv('MYSQL_PORT_3306_TCP_PORT'),\
                      os.getenv('MYSQL_INSTANCE_NAME'))
        print(conn_string)
        app.config['SQLALCHEMY_DATABASE_URI'] = conn_string

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
    app.run(debug=True)
