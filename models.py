from app import db

Base = db.Model


# class Category(db.Model):
#     __tablename__ = 'categories'
#     id = db.Column('id', db.Integer, primary_key=True)
#     name = db.Column('name', db.VARCHAR(length=40))
#
#
# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column('id', db.Integer, primary_key=True)
#     username = db.Column('username', db.VARCHAR(length=40), nullable=False)
#     password = db.Column('password', db.VARCHAR(length=40), nullable=False)
#
#
# class Ticket(db.Model):
#     __tablename__ = 'tickets'
#     id = db.Column('id', db.Integer, primary_key=True, unique=True)
#     category_id = db.Column(db.Integer, db.ForeignKey(Category.id))
#     category = db.relationship('Category')
#     name = db.Column('name', db.VARCHAR(length=40), nullable=False)
#     description = db.Column('description', db.VARCHAR(length=400))
#     price = db.Column('price', db.Integer)
#     endTimeReservation = db.Column('endTimeReservation', db.TIMESTAMP)
#     reservationPrice = db.Column('reservationPrice', db.Integer)
#     status = db.Enum('available', 'pending', 'sold', 'reserved')
#
#
# class Order(db.Model):
#     __tablename__ = 'orders'
#     id = db.Column('id', db.Integer, primary_key=True, unique=True)
#     ticket_id = db.Column('ticket_id', db.Integer, db.ForeignKey(Ticket.id), unique=True)
#     ticket = db.relationship("Ticket")
#     status = db.Enum('placed', 'payed')
#     complete = db.Column('complete', db.Boolean)
#
#
# class Reservation(db.Model):
#     __tablename__ = 'reservations'
#     id = db.Column('id', db.Integer, primary_key=True, unique=True)
#     ticket_id = db.Column('ticket_id', db.Integer, db.ForeignKey(Ticket.id), unique=True)
#     ticket = db.relationship("Ticket")
#     status = db.Enum('waiting', 'payed')
#     complete = db.Column('complete', db.Boolean)
#
#
# class ApiResponse(db.Model):
#     __tablename__ = 'apiresponse'
#     id = db.Column('id', db.Integer, primary_key=True)
#     type = db.Column('type', db.VARCHAR(length=40))
#     message = db.Column('message', db.VARCHAR(length=40))


# class Order(Base):
#     __tablename__ = 'order'
#     id = db.Column(db.Integer, primary_key=True)
#     customer = db.Column(db.String(127))
#     items = db.relationship("OrderItem")
#
#
# class Food(Base):
#     __tablename__ = 'food'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(127))
#
#
# class OrderItem(Base):
#     __tablename__ = 'order_item'
#     id = db.Column(db.Integer, primary_key=True)
#     order_id = db.Column(db.Integer, db.ForeignKey(Order.id))
#     order = db.relationship(Order)
#     food_id = db.Column(db.Integer, db.ForeignKey(Food.id))
#     food = db.relationship(Food)
#     comment = db.Column(db.String(127))










class User(db.Model):
    __tablename__ = 'user'

    id = db.Column('id', db.INTEGER, primary_key=True)
    userName = db.Column('username', db.VARCHAR(20), nullable=False)
    firstName = db.Column('firstname', db.VARCHAR(20), nullable=False)
    lastName = db.Column('lastname', db.VARCHAR(20), nullable=False)
    email = db.Column('email', db.VARCHAR(30), nullable=False)
    password = db.Column('password', db.VARCHAR(20), nullable=False)
    phone = db.Column('phone', db.VARCHAR(13), nullable=False)
    userStatus = db.Column('userstatus', db.INTEGER, nullable=False)


class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column('id', db.INTEGER, primary_key=True)
    name = db.Column('name', db.VARCHAR(20), nullable=False)
    photourl = db.Column('photourl', db.VARCHAR(40))


import enum

class StatusEnum(enum.Enum):
    pending = 'pending'
    done = 'done'


class PArticle(db.Model):
    __tablename__ = 'particle'

    id = db.Column('id', db.INTEGER, primary_key=True)
    name = db.Column('name', db.VARCHAR(20), nullable=False)
    photourl = db.Column('photourl', db.VARCHAR(40))
    status = db.Column('status', db.Enum(StatusEnum), nullable=False)

# class User(db.Model):
#     __tablename__ = 'user'
#
#     id = db.Column('id', db.INTEGER, primary_key=True)
#     userName = db.Column('username', db.VARCHAR(20), nullable=False)
#     firstName = db.Column('firstName', db.VARCHAR(20))
#     lastName = db.Column('lastName', db.VARCHAR(20))
#     email = db.Column('email', db.VARCHAR(30), nullable=False)
#     password = db.Column('password', db.VARCHAR(20), nullable=False)
#     phone = db.Column('phone', db.VARCHAR(13))
#     userStatus = db.Column('userStatus', db.INTEGER)
#
#
# class Photo(db.Model):
#     __tablename__ = 'photo'
#
#     id = db.Column('id', db.INTEGER, primary_key=True)
#     photo = db.Column('photo', db.VARCHAR(100))
#
#
#
# class Article(db.Model):
#     __tablename__ = 'article'
#
#     id = db.Column('id', db.INTEGER, primary_key=True)
#     name = db.Column('name', db.VARCHAR(20), nullable=False)
#
# class Photos(db.Model):
#     __tablename__ = 'photos'
#
#     id = db.Column('id', db.INTEGER, primary_key=True)
#     article_id = db.Column(db.INTEGER, db.ForeignKey(Article.id))
#     article = db.relationship(Article)
#     photo_id = db.Column(db.INTEGER, db.ForeignKey(Photo.id))
#     photo = db.relationship(Photo)
