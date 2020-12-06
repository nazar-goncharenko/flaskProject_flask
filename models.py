from app import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column('id', db.INTEGER, primary_key=True)
    userName = db.Column('username', db.VARCHAR(20), nullable=False)
    email = db.Column('email', db.VARCHAR(30), nullable=False)
    password = db.Column('password', db.VARCHAR(255), nullable=False)
    userStatus = db.Column('userstatus', db.INTEGER, nullable=False)

    def __init__(self, userName, email, password, userStatus):
        self.userName = userName
        self.email = email
        self.password = generate_password_hash(password)
        self.userStatus = userStatus

class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column('id', db.INTEGER, primary_key=True)
    name = db.Column('name', db.VARCHAR(20), nullable=False)
    text = db.Column('text', db.TEXT(2000), nullable=False)


import enum

class StatusEnum(enum.Enum):
    pending = 'pending'
    done = 'done'


class PArticle(db.Model):
    __tablename__ = 'particle'

    id = db.Column('id', db.INTEGER, primary_key=True)
    article_id = db.Column('article_id', db.ForeignKey(Article.id))
    article = db.relationship(Article)
    name = db.Column('name', db.VARCHAR(20), nullable=False)
    text = db.Column('text', db.TEXT(2000), nullable=False)
    status = db.Column('status', db.Enum(StatusEnum), nullable=False)

