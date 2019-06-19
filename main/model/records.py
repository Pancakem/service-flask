from .. import db


class Record(db.Model):
    __tablename__ = "records"

    id = db.Column(db.Integer)
    first_part = db.Column(db.String(100))
    second_part = db.Column(db.String(100))