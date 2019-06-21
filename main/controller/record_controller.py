from flask import request
from flask_restplus import Resource



class RecordList(Resource):


    def get():
        return