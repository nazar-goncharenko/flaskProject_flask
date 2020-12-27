from models import *


def create_objects():
    user1 = User(userName="testname", password="123", email="test@gmail.com", userStatus=23, role="user")
    article1 = Article(name="Some Article 1", text="Some Text")
    particale1 = PArticle(name="partical1", status="pending", text='some text', article=article1)
    user2 = User(userName="testname2", password="2", email="2", userStatus=23, role="admin")
    particale2 = PArticle(name="partical2", status="pending", text="url2", article=article1)

    db.session.add(user1)
    db.session.add(article1)
    db.session.add(particale1)
    db.session.add(user2)
    db.session.add(particale2)
    db.session.commit()


if __name__ == '__main__':
    db.create_all()
    # create_objects()
