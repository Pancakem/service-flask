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


class AuthDto:
	api = Namespace("auth", description="authentication related operations")
	user_auth = api.model("auth_details",{
		"email": fields.String(required=True, description="The email address"),
		"password": fields.String(required=True, description="The user password"),
	}
	)

class CustomerDto:
	api = Namespace('customer', description='customer related operations')
	customer = api.model('customer', {
		'phone_number': fields.String(required=True, description='customer mobile number'),
		'email': fields.String(description='customer email address'),
		'first_name': fields.String(required=True, description='customer first name'),
		'last_name': fields.String(required=True, description='customer last name'),
		'password': fields.String(required=True, description='customer password'),
		'public_id': fields.String(description='customer Identifier')
	})


class BikeDto:
	api = Namespace('bike', description='Bike related operations')
	bike = api.model('bike', {
		'price': fields.Integer(required=True, description='Bike price'),
		'model': fields.String(required=True, description='Bike model'),
		'engine': fields.String(required=True, description='Bike engine'),
		'plate': fields.String(required=True, description='Bike license plate'),
		'barcode': fields.String(description='Bike barcode')
	})

class SpareDto:
	api = Namespace('spare', description='spare related operations')
	spare = api.model('spare', {
		'name': fields.String(required=True, description='spare name'),
		'type': fields.String(description='spare type'),
		'barcode': fields.String(required=True, description='spare barcode'),
		'number_of_parts': fields.String(required=True, description='How many'),
		'price': fields.String(required=True, description='price'),
	})

class SpareSaleDto:
	api = Namespace('sparesale', description='spare sale related operations')
	sparesale = api.model('sparesale', {
		"barcode":fields.String(required=True, description='The product barcode.'),
		"number_of": fields.Integer(required=True, description='How many')
	})


class BikeSaleDto:
	api = Namespace('bikesale', description='Bike sale related operations')
	sparesale = api.model('bikesale',{
		"barcode": fields.String(required=True, description='The product barcode.'),
		
	})

class ProductDto:
	api = Namespace('product', description='Product related operations')
	product = api.model('product', {
		'barcode': fields.String(required=True, description='The product barcode'),
		'type': fields.String(required=True, description='The product type'),
		'type_id': fields.String(required=True, description='The product unique id'),
		'name': fields.String(required=True, description='The product name'),
		'cost': fields.String(required=True, description='The product cost'),
		'selling_price': fields.String(required=True, description='The product retail price'),
		'description': fields.String(description='The product description'),
		'image': fields.String(description='Item image')
	})


class ProductSaleDto:
	api = Namespace('productsale', description='Product sale related operations')
	productsale = api.model(
		'productsale',{
			'barcode': fields.String(required=True)
		}
	)