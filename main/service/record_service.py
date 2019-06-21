import datetime
import uuid
from .. import db
from user_service import save_changes
from main.model.records import Record


def create_record(data):
    record = Record(
        id = str(uuid.uuid4()),
        first_part = data['first'],
        second_part = data['second'],
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

def get_record(data):
    return Record.query.filter_by(name=data['name']).first_or_404(description='No such data')
    
def delete_record(data):
    record = Record.query.filter_by(name=data['name'])
    
    if record:
        db.session.delete(record)
        db.session.commit()

def update_record(data):
    record = Record.query.filter_by(name=data['name'])
    record.first_part = data['first']
    record.second_part = data['second']
    record.date_created = datetime.datetime.utcnow()
    save_changes(record)
