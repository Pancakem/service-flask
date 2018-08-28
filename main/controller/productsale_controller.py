
from flask import request
from flask_restplus import Resource


# from ..service.bike_service 
from main.util.dto import ProductSaleDto

api = ProductSaleDto.api

_product = ProductSaleDto.productsale


@api.route('/')
class ProductSale(Resource):
    @api.marshal_with(_product)
    def get(self, barcode):
        """ Buys specified """
        pass