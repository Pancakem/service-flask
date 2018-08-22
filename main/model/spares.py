from .. import db


class Spare(db.Model):
	"""Table for storing spares inventory """

	__tablename__ = 'spares'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
