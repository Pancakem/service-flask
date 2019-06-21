from .. import db


class Record(db.Model):
    __tablename__ = "records"

    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, unique=True)
    body = db.Column(db.String(1000))
    date_created = db.Column(db.DateTime)
    user_id = db.Column(db.String(100), db.ForeignKey('user.public_id'), nullable=False)

    def __repr__(self):
        return f'<record : {self.title}>'