from flask_testing import TestCase
from app import *
import unittest
import base64
import json


class ArticleUser(TestCase):
    data = {
        "username": "username",
        "password": "password",
        "email": "email@gmail.com",
        "role": "user"
    }

    tester = app.test_client()

    s = '{}:{}'.format(data['email'], data['password'])
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Basic ' + base64.b64encode(s.encode()).decode()}

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.session.commit()
        db.create_all()

    def tearDown(self):
        db.session.commit()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
