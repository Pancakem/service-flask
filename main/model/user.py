from .. import db, bcrypt
from sqlalchemy.orm import validates
import datetime
import jwt
from .blacklist import BlacklistToken
from ..config import key


class User(db.Model):
    """ User Model for storing user related information"""
    __tablename__ = 'user'

    email = db.Column(db.String(20), unique=True)
    public_id = db.Column(db.String(50), unique=True, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    password_hash = db.Column(db.String(100))
    date_registered = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Integer, default=0)
    records = db.relationship('Record', backref='user', lazy=True)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'

    @validates('email')
    def validate_email(self, key, address):
        assert '@' in address
        return address

    def encode_auth_token(self):
        """
        Generates the Auth Token
        : return: string
        """
        try:
            payload = {
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                "iat": datetime.datetime.utcnow(),
                "sub": self.public_id
            }
            return jwt.encode(
                payload,
                key,
                algorithm="HS256"
            ).decode('utf-8')
        except Exception as e:
            print(e)
            return 

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer string
        """
        try:
            payload = jwt.decode(auth_token, key)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return "Token blacklisted. Please log in again."
            else:
                return payload["sub"]
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please log in again."
        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again."
