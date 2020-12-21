from models import *
from app import app
from setuptools import setup, find_packages

# db.create_all()

from controllers.article_controller import *
from controllers.user_controller import *
from controllers.moderator_controller import *

@app.route('/')
def index():
    return 'Hello world'


db.create_all()
app.run()
