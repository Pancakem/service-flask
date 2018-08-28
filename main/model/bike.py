from .. import db
import datetime


class Bike(db.Model):
	""" Table for storing bike details """

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	model = db.Column(db.String(20))
	engine_type = db.Column(db.String(20))
	barcode = db.Column(db.String(50))
	retail_price = db.Column(db.Integer, nullable=False)
	bike_plate = db.column(db.String(20))
	since = db.Column(db.DateTime, default=datetime.datetime.utcnow())
	
	def __repr__(self):
		return "<Model {}".format(self.model)

