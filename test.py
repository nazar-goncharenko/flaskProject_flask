from models import *

user1 = User(userName="testname", password="123", email="test@gmail.com", firstName="saf", lastName="sdaf", phone="fasd", userStatus=23)
article1 = Article(name="Some Article 1",photourl="url")
particale1 = PArticle(name="partical1", status="pending", photourl="url")
# article2 = Article(name="Some Article 2")
# article3 = Article(name="Some Article 3")
#
# user1 = User(userName="testname", password="123", email="test@gmail.com", firstName="saf", lastName="sdaf", phone="fasd", userStatus=23)
# user2 = User(userName="2", password="2", email="2", firstName="2", lastName="2", phone="2", userStatus=23)
# user3 = User(userName="3", password="3", email="3", firstName="3", lastName="3", phone="3", userStatus=23)

# db.create_all()

user2 = User(userName="testname2", password="2", email="2", firstName="2", lastName="2", phone="2", userStatus=23)
particale2 = PArticle(name="partical2", status="pending", photourl="url2")

db.session.add(user1)
db.session.add(article1)
db.session.add(particale1)

db.session.add(user2)
db.session.add(particale2)

db.session.commit()
