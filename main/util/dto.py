from flask_restplus import Namespace, fields


class UserDto:
	api = Namespace('user', description='user related operations')
	user = api.model(
		'user', {
		'email': fields.String(required=True, description='user email address'),
		'first_name': fields.String(required=True, description='user first name'),
		'last_name': fields.String(required=True, description='user last name'),
		'password': fields.String(required=True, description='user password'),
		'public_id': fields.String(description='user Identifier')
		})