import base64
from flask_testing import TestCase
from app import *
import unittest
import json


class TestUser(TestCase):
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

    def test_index(self):
        response = self.tester.get("/")
        self.assertEqual(200, response.status_code)

    def create_user(self, data=None):
        if data is None:
            data = self.data
        username = data.get('username', None)
        password = data.get('password', None)
        email = data.get('email', None)
        role = data.get('role', None)
        if username and password and email and role and User.query.filter_by(email=email).first() is None:
            if role != 'user' and role != 'moderator':
                response = self.tester.post("/users", data=json.dumps(data), content_type='application/json')
                return self.assertEqual(404, response.status_code)
            response = self.tester.post("/users", data=json.dumps(data), content_type='application/json')
            return self.assertEqual(200, response.status_code)
        if User.query.filter_by(email=email).first() is not None:
            response = self.tester.post("/users", data=json.dumps(data), content_type='application/json')
            return self.assertEqual(400, response.status_code)
        else:
            response = self.tester.post("/users", data=json.dumps(data), content_type='application/json')
            return self.assertEqual(204, response.status_code)

    def test_post_user(self):
        self.create_user()

    def test_post_user_already_email(self):
        self.create_user()
        self.create_user()

    def test_post_user_bad_role(self):
        data = self.data.copy()
        data['role'] = 'bad role'
        self.create_user(data=data)

    def test_post_user_bad_data(self):
        data = {
            "input": "Bad data"
        }
        self.create_user(data=data)

    def test_get_user_id(self):
        self.create_user()
        response = self.tester.get('/users', headers=self.headers)
        return self.assertEqual(200, response.status_code)

    def test_unauthorized(self):
        response = self.tester.get('/users')
        statuscode = response.status_code
        self.assertEqual(401, statuscode)

    def test_logout(self):
        logout_user()

    def test_put_user(self):
        self.create_user()
        response = self.tester.put('/users', data=json.dumps(self.data), headers=self.headers)
        return self.assertEqual(202, response.status_code)

    def test_put_user_bad_role(self):
        self.create_user()
        data = self.data.copy()
        data['role'] = 'bad role'
        response = self.tester.put('/users', data=json.dumps(data), headers=self.headers)
        return self.assertEqual(404, response.status_code)

    def test_put_user_bad_email(self):
        self.create_user()
        data = self.data.copy()
        data['email'] = 'email1@gmail.com'
        self.create_user(data=data)
        response = self.tester.put('/users', data=json.dumps(data), headers=self.headers)
        return self.assertEqual(400, response.status_code)

    def test_put_user_bad_data(self):
        self.create_user()
        data = {
            "username": "username",
            "email": "email@gmail.com",
            "role": "user"
        }
        response = self.tester.put('/users', data=json.dumps(data), headers=self.headers)
        return self.assertEqual(204, response.status_code)

    def test_delete_user(self):
        self.create_user()
        response = self.tester.delete('/users', headers=self.headers)
        return self.assertEqual(201, response.status_code)


if __name__ == '__main__':
    unittest.main()
