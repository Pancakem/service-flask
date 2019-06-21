import datetime
import uuid
from .. import db
from main.model.records import Record


def create_record(data):
    record = Record(
        id = str(uuid.uuid4()),
        title = data['title'],
        body = data['body'],
        date_created = datetime.datetime.utcnow(),
        user_id = data['user_id']
    )
    save_changes(record)
    return {
        'status': 'success',
        'message': 'New record successfuly created.'
    }, 201


def get_all_records(user_id):
    records = Record.query.filter_by(user_id=data['user_id'])

    if not records:
        return {
            'status': 'fail',
            'message': 'could not get records'
        }, 409
    
    return records

def get_record(title):
    return Record.query.filter_by(title=title).first_or_404(description='No such data')
    
def delete_record(title):
    record = Record.query.filter_by(title=title)
    
    if record:
        db.session.delete(record)
        db.session.commit()

def update_record(data):
    record = Record.query.filter_by(title=data['title'])
    record.body = data['body']
    record.date_created = datetime.datetime.utcnow()
    save_changes(record)


def save_changes(data):
    db.session.add(data)
    db.session.commit()