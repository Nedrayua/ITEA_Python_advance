import json
from marshmallow.exceptions import ValidationError
from flask_restful import Resource
from flask import request

from models import Product, Category
from schemas import ProductSchema, CategorySchema
from utils import total_price_all_product_in_shop


class ProductResource(Resource):
    def get(self, id=None):
        if id:
            product = Product.objects.get(id=id)
            product.add_view()
            product.reload()
            return ProductSchema().dump(product)
        else:
            products = Product.objects()
            return ProductSchema().dump(products, many=True)

    def post(self):
        try:
            ProductSchema().load(request.json)
        except ValidationError as e:
            return str(e)
        product = Product(**request.json)
        product.save()
        return ProductSchema().dump(product)

    def put(self, id):
        try:
            ProductSchema().load(request.json)
        except ValidationError as e:
            return str(e)
        product = Product.objects.get(id=id)
        product.update(**request.json)
        product.reload()
        return ProductSchema().dump(product)

    def delete(self, id):
        Product.objects.get(id=id).delete()
        return str({"status": "deleted"})


class CategoryResource(Resource):
    def get(self, id=None):
        if id:
            category = Category.objects.get(id=id)
            return CategorySchema().dump(category)
        else:
            categories = Category.objects()
            return CategorySchema().dump(categories, many=True)

    def post(self):
        try:
            CategorySchema().load(request.json)
        except ValidationError as e:
            return str(e)
        category = Category(**request.json)
        category.save()
        return CategorySchema().dump(category)

    def put(self, id):
        try:
            CategorySchema().load(request.json)
        except ValidationError as e:
            return str(e)
        category = Category.objects.get(id=id)
        category.update(**request.json)
        category.reload()
        return CategorySchema().damp(category)

    def delete(self, id):
        Category.objects.get(id=id).delete()
        return str({"status": "deleted"})


class TotalPriceResource(Resource):
    def get(self):
        return str({"Total price": total_price_all_product_in_shop()})
