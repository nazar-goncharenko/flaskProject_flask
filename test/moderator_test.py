from flask_testing import TestCase
from test.article_test import *
from test.user_test import *
from app import *
import unittest
import base64
import json


class TestModerator(TestCase):
    tester = app.test_client()
    user_tester = TestUser()
    article_tester = TestArticle()

    moderator_data = {
        "username": "admin",
        "password": "admin",
        "email": "admin@gmail.com",
        "role": "moderator"
    }

    s = '{}:{}'.format(moderator_data['email'], moderator_data['password'])
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

    def test_change_particle_by_id(self):
        self.user_tester.create_user(self.moderator_data)
        self.article_tester.put_article()
        response = self.tester.put("/moderator/particle/1",
                                   headers=self.headers,
                                   content_type='application/json')
        return self.assertEqual(200, response.status_code)

    def test_change_particle_by_id_not_found(self):
        self.user_tester.create_user(self.moderator_data)
        response = self.tester.put("/moderator/particle/1",
                                   headers=self.headers,
                                   content_type='application/json')
        return self.assertEqual(404, response.status_code)

    def test_change_particle_by_id_already_changed(self):
        self.user_tester.create_user(self.moderator_data)
        self.article_tester.put_article()
        self.tester.put("/moderator/particle/1",
                        headers=self.headers,
                        content_type='application/json')
        response = self.tester.put("/moderator/particle/1",
                                   headers=self.headers,
                                   content_type='application/json')
        return self.assertEqual(208, response.status_code)

    def test_change_particle_no_permission(self):
        self.user_tester.create_user()
        self.article_tester.put_article()
        response = self.tester.put("/moderator/particle/1",
                                   headers=self.user_tester.headers,
                                   content_type='application/json')
        return self.assertEqual(404, response.status_code)

    def test_delete_particle_by_id(self):
        self.user_tester.create_user(self.moderator_data)
        self.article_tester.put_article()
        response = self.tester.delete("/moderator/particle/1",
                                      headers=self.headers,
                                      content_type='application/json')
        return self.assertEqual(201, response.status_code)

    def test_get_pending_articles(self):
        self.user_tester.create_user(self.moderator_data)
        self.article_tester.put_article()
        response = self.tester.get("/moderator/particle",
                                   headers=self.headers,
                                   content_type='application/json')
        return self.assertEqual(200, response.status_code)

    def test_get_pending_articles_no_permission(self):
        self.user_tester.create_user()
        self.article_tester.put_article()
        response = self.tester.get("/moderator/particle",
                                   headers=self.user_tester.headers,
                                   content_type='application/json')
        return self.assertEqual(404, response.status_code)

    def test_get_pending_article_by_id(self):
        self.user_tester.create_user(self.moderator_data)
        self.article_tester.put_article()
        response = self.tester.get("/moderator/particle/1",
                                   headers=self.headers,
                                   content_type='application/json')
        return self.assertEqual(200, response.status_code)

    def test_get_pending_article_by_id_no_permission(self):
        self.user_tester.create_user()
        self.article_tester.put_article()
        response = self.tester.get("/moderator/particle/1",
                                   headers=self.user_tester.headers,
                                   content_type='application/json')

        return self.assertEqual(404, response.status_code)

    def test_get_pending_article_by_id_not_found(self):
        self.user_tester.create_user(self.moderator_data)
        response = self.tester.get("/moderator/particle/1",
                                   headers=self.headers,
                                   content_type='application/json')
        return self.assertEqual(404, response.status_code)


if __name__ == '__main__':
    unittest.main()
