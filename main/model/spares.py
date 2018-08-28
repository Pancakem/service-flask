from .. import db
import datetime


class Spare(db.Model):
	"""Table for storing spares inventory """

	__tablename__ = 'spares'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	retail_price = db.Column(db.Integer, nullable=False)
	part_name = db.Column(db.String(20), nullable=False)
	part_type = db.Column(db.String(20), nullable=False)
	barcode = db.Column(db.String(50), nullable=False)
	number_of = db.Column(db.Integer)
	

	def __repr__(self):
		return "<Part name {}>".format(self.model)


	def sold(self):
		self.number_of -= 1
