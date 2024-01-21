import os
from unittest import TestCase

from models import db, User, Message, Follows
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"

from app import app

db.create_all()

class MessageModelTestCase(TestCase):

   def setUp(self):
      """Create test client, add sample data."""

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

      self.message1 = Message(text="test message 1", user_id=self.user1.id)
      self.message2 = Message(text="test message 2", user_id=self.user2.id)

      db.session.add(self.message1)
      db.session.add(self.message2)
      db.session.commit()

   def tearDown(self):
      """Clean up."""

      db.session.rollback()

   def test_make_message(self):
      """Test that a message can be created."""

      message = Message(text="test message", user_id=self.user1.id)

      db.session.add(message)
      db.session.commit()

      self.assertEqual(len(self.user1.messages), 2)
      self.assertEqual(len(self.user2.messages), 1)

   def test_delete_message(self):
      """Test that a message can be deleted."""

      db.session.delete(self.message1)
      db.session.commit()

      self.assertEqual(len(self.user1.messages), 0)
      self.assertEqual(len(self.user2.messages), 1)

   def test_message_likes(self):
      """Test that a message can be liked."""

      self.user1.likes.append(self.message2)
      db.session.commit()

      self.assertEqual(len(self.user1.likes), 1)


   def test_message_unlikes(self):
      """Test that a message can be unliked."""

      self.user1.likes.append(self.message2)
      db.session.commit()

      self.user1.likes.remove(self.message2)
      db.session.commit()

      self.assertEqual(len(self.user1.likes), 0)

      

      