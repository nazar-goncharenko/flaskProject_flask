from app import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column('id', db.INTEGER, primary_key=True)
    userName = db.Column('username', db.VARCHAR(20), nullable=False)
    firstName = db.Column('firstName', db.VARCHAR(20), nullable=False)
    lastName = db.Column('lastName', db.VARCHAR(20), nullable=False)
    email = db.Column('email', db.VARCHAR(30), nullable=False)
    password = db.Column('password', db.VARCHAR(20), nullable=False)
    phone = db.Column('phone', db.VARCHAR(13), nullable=False)
    userStatus = db.Column('userStatus', db.INTEGER, nullable=False)


class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column('id', db.INTEGER, primary_key=True)
    name = db.Column('name', db.VARCHAR(20), nullable=False)
    photos = db.relationship('Photo', secondary='photos', backref=db.backref('articles'))


class Photo(db.Model):
    __tablename__ = 'photo'

    id = db.Column('id', db.INTEGER, primary_key=True)
    photo = db.Column('photo', db.VARCHAR(100))


class Photos(db.Model):
    __tablename__ = 'photos'

    id = db.Column('id', db.INTEGER, primary_key=True)
    article_id = db.Column('article_id', db.INTEGER, db.ForeignKey(Article.id))
    photo_id = db.Column('photo_id', db.INTEGER, db.ForeignKey(Photo.id))
