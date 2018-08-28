from flask import request
from flask_restplus import Resource

from ..service.bike_service import get_a_bike, get_all_bikes, inventory_bike_size, save_new_bike
from ..service.spare_service import new_spare, get_all_spares, get_a_spare, inventory_size
from main.util.dto import ProductDto

api = ProductDto.api

_product = ProductDto.product


@api.route('/')
class ProductList(Resource):
    @api.doc('List available products')
    @api.marshal_list_with(_product, envelope='data')
    def get(self):
        """List the inventory"""
        return get_all_bikes()

    @api.response(201, 'Inventory successfully added.')
    @api.doc('Add a new item')
    @api.expect(_product, validate=True)
    def post(self):
        """Adds a new item"""
        data = request.json
        if data['type'] == 'bike':
            return save_new_bike(data)
        else:
            return new_spare(data)


@api.route('/<barcode>')
@api.response(404, 'Product not found.')
class Product(Resource):
    @api.doc('Get a product by id')
    @api.marshal_with(_product)
    def get(self, barcode):
        if not get_a_bike(barcode):
            return get_a_spare(barcode)
        else:
            return get_a_bike(barcode)


@api.route('/size/<barcode>')
class Productsize(Resource):
    @api.doc('Get product type inventory size')
    def get(self, barcode):
        if not inventory_bike_size(barcode):
            return inventory_size(barcode)
        else:
            return inventory_bike_size(barcode)
