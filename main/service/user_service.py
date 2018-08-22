import uuid
import datetime 

from fiucha.main.model.user import User

# this function should only be accessed by a logged in user
def save_new_user(data):
	user = User.query.filter_by(email=data['email']).first()

	if not user:
		new_user = User(
			public_id=str(uuid.uuid4()),
			email=data['email']
			first_name=data['first_name'],
			last_name=data['last_name'],
			password=data['password'],
			date_registered=datetime.datetime.utcnow()
			)

		save_changes(new_user)
		response_object = {
			'status': 'success',
			'message': 'Succesfully registered'
		}

		return response_object, 201
	else:

		response_object = {
			'status': 'fail',
			'message': 'User already exists. Please Log in.'
		}

		return response_object, 409

def get_a_user(public_id):
	return User.query.filter_by(public_id=public_id).first()


def get_all_users():
	return User.query.all()


def save_changes(data):
	db.session.add(data)
	db.session.commit()