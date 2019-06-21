from flask_restplus import Namespace, fields


class UserDto:
	api = Namespace('user', description='user related operations')
	user = api.model(
		'user', {
		'email': fields.String(required=True, description='user email address'),
		'first_name': fields.String(required=True, description='user first name'),
		'last_name': fields.String(required=True, description='user last name'),
		'password': fields.String(required=True, description='user password')
		})
	outuser = api.model(
	'outuser', {
		'email': fields.String(required=True, description='user email address'),
		'first_name': fields.String(required=True, description='user first name'),
		'last_name': fields.String(required=True, description='user last name'),
		'is_admin': fields.Integer(required=True, description='user priviledge')
		})


class AuthDto:
	api = Namespace('auth', description='authentication related operations')
	user_auth = api.model('auth_details',{
		'email': fields.String(required=True, description='The email address'),
		'password': fields.String(required=True, description='The user password'),
	}
	)

class RecordDto:
	api = Namespace('record', description='record related operations')
	record = api.model(
		'record', {
			'title': fields.String(required=True, description='The record name'),
			'body': fields.String(required=True, description='Record body')
		}
	)