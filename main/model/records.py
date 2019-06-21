from .. import db


class Record(db.Model):
    __tablename__ = "records"

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, unique=True)
    first_part = db.Column(db.String(100))
    second_part = db.Column(db.String(100))
    date_created = db.Column(db.DateTime)
    user_id = db.Column(db.String(100), db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<record : {self.name}>'