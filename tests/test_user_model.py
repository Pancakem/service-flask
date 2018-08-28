import unittest
import datetime


from fiucha.main.import db
from fiucha.main.model.user import User
from fiucha.test.base import BaseTestCase

class TestUserModel(BaseTestCase):

    def test_encode_auth_token(self):
        user = User(
            first_name = "John",
            last_name = "Doe",
            password = "test", 
            registered_on = datetime.datetime.utcnow()
        )

        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))


    def test_decode_auth_token(self):
        user = User(
            first_name = "John",
            last_name = "Doe",
            password = "test", 
            registered_on = datetime.datetime.utcnow()
        )
        
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(User.decode_auth_token(auth_token.decode("utf-8")) == 1)


if __name__ == "__main__":
    unittest.main()