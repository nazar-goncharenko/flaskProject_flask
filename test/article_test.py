from flask_testing import TestCase
from test.user_test import *
from app import *
import unittest
import base64
import json


class ArticleUser(TestCase):
    data = {
        "name": "Article",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    }

    tester = app.test_client()
    user = TestUser()

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.session.commit()
        db.create_all()

    def tearDown(self):
        db.session.commit()
        db.drop_all()

    def create_article(self, data=None):
        if data is None:
            data = self.data
        self.user.create_user()
        name = data.get('name', None)
        text = data.get('text', None)
        if name and text:
            response = self.tester.post("/articles", data=json.dumps(data),
                                        headers=self.user.headers,
                                        content_type='application/json')
            return self.assertEqual(201, response.status_code)
        else:
            response = self.tester.post("/articles", data=json.dumps(data),
                                        headers=self.user.headers,
                                        content_type='application/json')
            return self.assertEqual(400, response.status_code)

    def test_post_article(self):
        self.create_article()

    def test_post_article_bad_data(self):
        data = {
            "title": "Article",
            "article": "Lorem ipsum"
        }
        return self.create_article(data=data)

    def test_get_article(self):
        self.create_article()
        response = self.tester.get("/articles/1",
                                   headers=self.user.headers,
                                   content_type='application/json')
        return self.assertEqual(200, response.status_code)

    def test_get_article_not_found(self):
        self.user.create_user()
        response = self.tester.get("/articles/1",
                                   headers=self.user.headers,
                                   content_type='application/json')
        return self.assertEqual(404, response.status_code)

    def test_get_article_no_user(self):
        response = self.tester.get("/articles/1",
                                   headers=self.user.headers,
                                   content_type='application/json')
        return self.assertEqual(401, response.status_code)

    def test_get_articles(self):
        self.create_article()
        response = self.tester.get("/articles",
                                   headers=self.user.headers,
                                   content_type='application/json')
        return self.assertEqual(200, response.status_code)

    def test_delete_article(self):
        self.create_article()
        self.put_article()
        response = self.tester.delete("/articles/1", data=json.dumps(self.data),
                                      headers=self.user.headers,
                                      content_type='application/json')
        return self.assertEqual(201, response.status_code)

    def test_delete_article_not_found(self):
        self.user.create_user()
        response = self.tester.delete("/articles/1", data=json.dumps(self.data),
                                      headers=self.user.headers,
                                      content_type='application/json')
        return self.assertEqual(404, response.status_code)

    def put_article(self):
        self.create_article()
        response = self.tester.put("/articles/1", data=json.dumps(self.data),
                                   headers=self.user.headers,
                                   content_type='application/json')
        return self.assertEqual(202, response.status_code)

    def test_put_article(self):
        return self.put_article()

    def test_put_article_bad_data(self):
        self.create_article()
        data = {
            "title": "Article",
            "text": "Lorem ipsum"
        }
        response = self.tester.put("/articles/1", data=json.dumps(data),
                                      headers=self.user.headers,
                                      content_type='application/json')
        return self.assertEqual(204, response.status_code)

    def test_put_article_not_found(self):
        self.user.create_user()
        response = self.tester.put("/articles/1", data=json.dumps(self.data),
                                      headers=self.user.headers,
                                      content_type='application/json')
        return self.assertEqual(404, response.status_code)


if __name__ == '__main__':
    unittest.main()
