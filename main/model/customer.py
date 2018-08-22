from .. import db
from sqlalchemy.orm import validates

class Customer(db.Model):
	""" Table for customer records """

	__tablename__ = 'customer'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	first_name = db.Column(db.String(20), nullable=False)
	last_name = db.Column(db.String(20), nullable=False)
	phone_number = db.Column(db.String(10), nullable=False)
	email = db.Column(db.String(20), nullable=True)
	item_key = db.Column(db.Integer, nullable=False)

	@validates('email')
	def validate_email(self, key, address):
		assert '@' in address
		return address

	def __repr__(self):
		return '<Customer: {} {}'.format(self.first_name, self.last_name)

	