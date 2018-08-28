import datetime

from main.models.customer import Customer


def get_all_customers():
    return Customer.query.all()


def save_new_customer(data):
	customer = Customer.query.filter_by(email=data['email']).first()

	if not customer:
		new_customer = Customer(
			public_id=str(uuid.uuid4()),
			email=data['email'],
            phone_number=data["phone_number"]
			first_name=data['first_name'],
			last_name=data['last_name'],
			item_key=data['item'],
			last_date_of_sale=datetime.datetime.utcnow()
			)

		save_changes(new_customer)
		return {
            "status": "success",
            "message": "Customer created."}, 200
        
	else:
		try:
			customer.items.loads().append(data["item"])
			return {
            "status": "success",
            "message": "Customer created."}, 200
			
		except Exception  as e:
			# if an error occurs send it to a bug email
			# then again in the application it should be handled b7y throwing an error screen
			return { "status": "Failure",
					"message": "Failed to update customer"}	, 409
		

def get_a_customer(public_id):
	return Customer.query.filter_by(public_id=public_id).first()


def get_all_customers():
	return Customer.query.all()


def save_changes(data):
	db.session.add(data)
	db.session.commit()