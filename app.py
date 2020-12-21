from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
auth = HTTPBasicAuth()
app.debug = True
app.config['SECRET_KEY'] = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{user}:{password}@{server}/{database}'.format(
    user='root', password='root', server='localhost', database='pp_db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
engine = db.engine

from controllers.article_controller import *
from controllers.user_controller import *
from controllers.moderator_controller import *

if __name__ == '__main__':
    db.create_all()
    app.run()
