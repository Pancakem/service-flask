from flask import request
from flask_restplus import Resource

from ..util.dto import RecordDto
from ..service.record_service import *


api = RecordDto.api

_record = RecordDto.record


@api.route('/')
class RecordList(Resource):

    @api.doc('get all records belonging to a user')
    @api.marshal_list_with(_record, envelope='data')
    def get(self):

        data = request.json
        return get_all_records(data['user_id'])

    @api.doc('creates a record')
    def post(self):
        data = request.json

        return create_record(data)
    
    @api.doc('update a record')
    def update(self):
        data = request.json
        return update_record(data)

@api.route('/<name>')
class Record(Resource):

    @api.doc('get a user record')  
    def get(self, name):
        return get_record(name)

    @api.doc('delete a user record')
    def delete(self, name):
        return delete_record(name)
    
    