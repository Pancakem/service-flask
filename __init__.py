# fiucha/__init__.py

from flask_restplus import Api
from flask import Blueprint


from main.controller.user_controller import api as user_ns
from main.controller.auth_controller import api as auth_ns
from main.controller.product_controller import api as product_ns
from main.controller.productsale_controller import api as productsale_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
	title='Fiucha inventory management testing',
	version='1.0',
	description='a boilerplate for fiucha web service'
	)

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(product_ns)
api.add_namespace(productsale_ns)