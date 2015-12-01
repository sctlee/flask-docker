from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from models import User

welcome_page = Blueprint('welcome_page', __name__)


@welcome_page.route('/')
@welcome_page.route('/index')
def index():
    return render_template('index.html')


