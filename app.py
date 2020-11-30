from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/pp_6'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

manager = Manager(app)
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

SessionFactory = sessionmaker(bind=engine)

BaseModel = declarative_base()

db.create_all()

# if __name__ == "__main__":
#     app.run(debug=True)

