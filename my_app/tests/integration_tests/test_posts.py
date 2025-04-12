import unittest
from routes import create_app
from models import db, Post

app = create_app()

class PostDatabaseIntegrationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_post_in_db(self):
        response = self.client.post('/posts', json={"content": "This is a test post"})
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn('id', data)
        self.assertEqual(data['content'], 'This is a test post')

        with self.app.app_context():
            post = db.session.get(Post, data['id'])
            self.assertIsNotNone(post)
            self.assertEqual(post.content, 'This is a test post')

    def test_get_post_by_id_from_db(self):
        response = self.client.post('/posts', json={"content": "Test post for DB GET"})
        post_id = response.get_json()['id']

        response = self.client.get(f'/posts/{post_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['id'], post_id)
        self.assertEqual(data['content'], "Test post for DB GET")

        with self.app.app_context():
            post = db.session.get(Post, post_id)
            self.assertEqual(post.content, "Test post for DB GET")

    def test_update_post_in_db(self):
        response = self.client.post('/posts', json={"content": "Old content"})
        post_id = response.get_json()['id']

        response = self.client.put(f'/posts/{post_id}', json={"content": "Updated content"})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['content'], "Updated content")

        with self.app.app_context():
            post = db.session.get(Post, post_id)
            self.assertEqual(post.content, "Updated content")

    def test_delete_post_from_db(self):
        response = self.client.post('/posts', json={"content": "Test post for DELETE"})
        post_id = response.get_json()['id']

        response = self.client.delete(f'/posts/{post_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['message'], "Post deleted successfully")

        with self.app.app_context():
            post = db.session.get(Post, post_id)
            self.assertIsNone(post)

    def test_like_post_in_db(self):
        response = self.client.post('/posts', json={"content": "Test post for like"})
        post_id = response.get_json()['id']

        response = self.client.post(f'/posts/{post_id}/like')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['likes'], 1)

        with self.app.app_context():
            post = db.session.get(Post, post_id)
            self.assertEqual(post.likes, 1)

    def test_get_likes_from_db(self):
        response = self.client.post('/posts', json={"content": "Test post for get likes"})
        post_id = response.get_json()['id']

        self.client.post(f'/posts/{post_id}/like')

        response = self.client.get(f'/posts/{post_id}/likes')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['likes'], 1)

        with self.app.app_context():
            post = db.session.get(Post, post_id)
            self.assertEqual(post.likes, 1)

    def test_heart_post_in_db(self):
        response = self.client.post('/posts', json={"content": "Test post for heart"})
        post_id = response.get_json()['id']

        response = self.client.post(f'/posts/{post_id}/heart')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['hearts'], 1)

        with self.app.app_context():
            post = db.session.get(Post, post_id)
            self.assertEqual(post.hearts, 1)

    def test_get_hearts_from_db(self):
        response = self.client.post('/posts', json={"content": "Test post for get hearts"})
        post_id = response.get_json()['id']

        self.client.post(f'/posts/{post_id}/heart')

        response = self.client.get(f'/posts/{post_id}/hearts')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['hearts'], 1)

        with self.app.app_context():
            post = db.session.get(Post, post_id)
            self.assertEqual(post.hearts, 1)


if __name__ == '__main__':
    unittest.main()
