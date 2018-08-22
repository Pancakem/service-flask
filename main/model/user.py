from .. import db, bcrypt
from sqlalchemy.orm import validates


class User(db.Model):
	""" User Model for storing user related information"""
	__tablename__ = 'user'

	id = db.Column(db.Integer,  primary_key=True, autoincrement=True)
	email = db.Column(db.String(20), nullable=True)
	# public_id
	first_name = db.Column(db.String(20), nullable=False)
	last_name = db.Column(db.String(20), nullable=False)


	@property
	def password(self):
	    raise AttriuteError('password: write-only field')

	@password.setter
	def password(self, password):
		self.password_hash = bcrypt.generate_passwrd_hash(password).decode('utf-8')


	def check_password(self, password):
		return bcrypt.check_password_hash(self.password_hash, password)

	def __repr__(self):
		return '<User "{} {}" >'.format(self.first_name, self.last_name)

	@validates('email')
	def validate_email(self, key, address):
		assert '@' in address
		return address