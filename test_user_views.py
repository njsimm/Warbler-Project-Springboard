import os
from unittest import TestCase

from models import db, connect_db, Message, User

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"

from app import app, CURR_USER_KEY

db.create_all()

app.config['WTF_CSRF_ENABLED'] = False

class UserViewTestCase(TestCase):
    """Test user views"""

    def setUp(self):
        """Create test client and sample data"""
        User.query.delete()
        Message.query.delete()

        self.client = app.test_client()

        self.testuser = User.signup(username="testuser", email="test@test.com", password="testuser", image_url=None)

        db.session.commit()

    def test_user_listings(self):
        """Test the listings of the users"""
        with self.client as c:
            resp = c.get("/users")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("@testuser", html)

    def test_user_profile(self):
        """Test viewing a user profile"""
        with self.client as c:
            resp = c.get(f"/users/{self.testuser.id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(self.testuser.username, html)

    def test_show_following(self):
        """Test showing the following page"""
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id

            resp = c.get(f"/users/{self.testuser.id}/following")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Following", html)

    def test_add_follower(self):
        """Test adding a follower"""

        follower = User.signup("follower", "follow@test.com", "password", None)
        db.session.add(follower)
        db.session.commit()

        with self.client as c:
            with c.session_transaction() as sess:
                testuser = User.query.get(self.testuser.id)
                sess[CURR_USER_KEY] = testuser.id
                follower = User.query.get(follower.id)

            resp = c.post(f"/users/follow/{self.testuser.id}", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Unfollow", html)
       