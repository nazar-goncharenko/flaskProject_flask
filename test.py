from models import *

# user1 = User(userName="testname", password="123", email="test@gmail.com", firstName="saf", lastName="sdaf", phone="fasd", userStatus=23)
# photo1 = Photo(photoUrl="someUrl")
# article1 = Article(name="Some Article")
# photos1 = Photos(article=article1, photo=photo1)

user1 = User(userName="testname", password="123", email="test@gmail.com", firstName="saf", lastName="sdaf", phone="fasd", userStatus=23)
user2 = User(userName="2", password="2", email="2", firstName="2", lastName="2", phone="2", userStatus=23)
user3 = User(userName="3", password="3", email="3", firstName="3", lastName="3", phone="3", userStatus=23)

db.create_all()

db.session.add(user1)
db.session.add(user3)
db.session.add(user2)
# db.session.add(photo1)
# db.session.add(article1)
# db.session.add(photos1)

db.session.commit()
