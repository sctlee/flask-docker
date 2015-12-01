from flask.ext.script import Manager
from models import db
from app import create_app

manager = Manager(create_app())


# manage db
@manager.command
def initdb():
    from models import User
    db.create_all(app=create_app())


@manager.command
def dropdb():
    from models import User
    db.drop_all(app=create_app())

if __name__ == '__main__':
    manager.run()
