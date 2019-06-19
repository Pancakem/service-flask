import uuid
import datetime 
from .. import db
from main.model.user import User

def generate_token(user):

	try:
		# generate the auth token
		auth_token = user.encode_auth_token(user.id)

		response_object = {
			"status": "succes",
			"message": "Successfully registered.",
			"Authorization": user.decode_auth_token(auth_token)
		}

		return response_object, 201
	
	except Exception as e:
		response_object = {
			"status": "fail",
			"message": "Some error occurred. Please try again."
		}

		return response_object, 401

# this function should only be accessed by a logged in user
def save_new_user(data):
	user = User.query.filter_by(email=data['email']).first()

	if not user:
		new_user = User(
			public_id=str(uuid.uuid4()),
			email=data['email'],
			first_name=data['first_name'],
			last_name=data['last_name'],
			password=data['password'],
			date_registered=datetime.datetime.utcnow(),
			is_admin = data['is_admin']
			)

		save_changes(new_user)
		return generate_token(new_user)
	else:

		response_object = {
			'status': 'fail',
			'message': 'User already exists. Please Log in.'
		}

		return response_object, 409

def get_a_user(public_id):
	return User.query.filter_by(public_id=public_id).first()

# only an admin or super admin can view all users
def get_all_users(admin_token):
	return User.query.all()


def save_changes(data):
	db.session.add(data)
	db.session.commit()


