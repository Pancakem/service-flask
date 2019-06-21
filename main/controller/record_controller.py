from flask import request
from flask_restplus import Resource

from ..util.dto import RecordDto
from ..service.record_service import *


api = RecordDto.api

_record = RecordDto.record


@api.route('/record')
class RecordList(Resource):

    @api.doc('get all records belonging to a user')
    def get(self):

        data = request.json
        
        return