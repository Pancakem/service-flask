from .. import db


class Bike(db.Model):
	""" Table for storing bike details """

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
