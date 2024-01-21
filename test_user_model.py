"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


import os
from unittest import TestCase

from models import db, User, Message, Follows
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()


class UserModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test clients as well as add sample data."""

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

        self.client = app.test_client()

        self.user1 = User(email="test@test.com", username="testuser", password="password1")
        
        self.user2 = User(email="test2@test.com", username="testuser2", password="password2")
        
        self.user1.password = bcrypt.generate_password_hash(self.user1.password).decode('UTF-8')
        self.user2.password = bcrypt.generate_password_hash(self.user2.password).decode('UTF-8')
        
        db.session.add(self.user1)
        db.session.add(self.user2)
        db.session.commit()

    def test_user_model(self):
        """Does basic model work?"""

        self.assertEqual(len(self.user1.messages), 0)
        self.assertEqual(len(self.user1.followers), 0)

        self.assertEqual(len(self.user2.messages), 0)
        self.assertEqual(len(self.user2.followers), 0)

    def test_repr(self):
        """Does repr work?"""

        self.assertEqual(repr(self.user1), f"<User #{self.user1.id}: {self.user1.username}, {self.user1.email}>")
        self.assertEqual(repr(self.user2), f"<User #{self.user2.id}: {self.user2.username}, {self.user2.email}>")

    def test_following(self):
        """Does following work?"""
        
        self.user1.following.append(self.user2)
        db.session.commit()

        self.assertEqual(self.user1.is_following(self.user2), True)
        self.assertEqual(self.user2.is_following(self.user1), False)

    def test_followed(self):
        """Does followed by work?"""

        self.user1.following.append(self.user2)
        db.session.commit()

        self.assertEqual(self.user1.is_followed_by(self.user2), False)
        self.assertEqual(self.user2.is_followed_by(self.user1), True)

    def test_signup(self):
        """Does signup work?"""

        user3 = User.signup(email="test3@test.com", username="testuser3", password="password3", image_url="http://randomurl.jpg")
        db.session.commit()

        self.assertEqual(user3.username, "testuser3")
        self.assertEqual(user3.email, "test3@test.com")

    def test_signup_fail(self):
        """Does signup fail with invalid inputs?"""

        with self.assertRaises(ValueError):
            user3 = User.signup(email="", username="", password="", image_url="")

    def test_authenticate(self):
        """Does authenticate work?"""

        user1 = User.authenticate(self.user1.username, "password1")

        self.assertEqual(user1, self.user1)

    def test_authenticate_fail(self):
        """Does authenticate fail with invalid inputs?"""

        user1 = User.authenticate(self.user1.username, "incorrect")

        self.assertEqual(user1, False)
