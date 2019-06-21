from flask import request
from flask_restplus import Resource

from ..util.dto import RecordDto
from ..service.record_service import *
from ..service.auth_helper import Auth


api = RecordDto.api

_record = RecordDto.record

user_id_ = RecordDto.user_id


@api.route('/')
class RecordList(Resource):

    @api.doc('get all records belonging to a user')
    @api.marshal_list_with(_record, envelope='data')
    def get(self):
        
        user_id = get_token(request)

        return get_all_records(user_id)

    @api.doc('creates a record')
    @api.expect(_record, validate=True)
    def post(self):
        data = request.json
        user_id = get_token(request)

        return create_record(data, user_id)
    
    @api.doc('update a record')
    @api.expect(_record, validate=True)
    def update(self):
        data = request.json
        return update_record(data)

@api.route('/<title>')
class Record(Resource):

    @api.doc('get a user record')
    @api.marshal_with(_record)
    def get(self, title):
        return get_record(title)

    @api.doc('delete a user record')
    def delete(self, title):
        return delete_record(title)
    

def get_token(request):
    data, status = Auth.get_logged_in_user(request)
    token = ''
    if status == 200:
        token = data['data']['user_id']
    return token