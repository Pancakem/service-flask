# fiucha/__init__.py

from flask_restplus import Api
from flask import Blueprint


from main.controller.user_controller import api as user_ns
from main.controller.auth_controller import api as auth_ns
from main.controller.record_controller import api as record_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
	title='SoftSearch interview',
	version='1.0',
	description='a boilerplate for an example web service'
	)

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(record_ns)