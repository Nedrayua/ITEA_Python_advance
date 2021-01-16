import json
from marshmallow.exceptions import ValidationError
from flask_restful import Resource
from flask import request

from models import Product, Category
from schemas import ProductSchemaRead, ProductSchemaWrite, CategorySchemaRead, CategorySchemaWrite
from utils import total_price_all_product_in_shop


class ProductResource(Resource):
    def get(self, id=None):
        if id:
            product = Product.objects.get(id=id)
            product.add_view()
            product.reload()
            return ProductSchemaRead().dump(product)
        else:
            products = Product.objects()
            return ProductSchemaRead().dump(products, many=True)

    def post(self):
        try:
            ProductSchemaWrite().load(request.json)
        except ValidationError as e:
            return str(e)
        product = Product(**request.json)
        product.save()
        return ProductSchemaRead().dump(product)

    def put(self, id):
        try:
            ProductSchemaWrite().load(request.json)
        except ValidationError as e:
            return str(e)
        if request.json['category']:
            request.json['category'] = Category.objects.get(id=request.json['category'])
        product = Product.objects.get(id=id)
        product.update(**request.json)
        product.reload()
        return ProductSchemaRead().dump(product)

    def delete(self, id):
        Product.objects.get(id=id).delete()
        return str({"status": "deleted"})


class CategoryResource(Resource):
    def get(self, id=None):
        if id:
            return CategorySchemaRead().dump(Category.objects.get(id=id))
        else:
            categories = Category.objects()
            return CategorySchemaRead().dump(categories, many=True)

    def post(self):
        try:
            CategorySchemaWrite().load(request.json)
        except ValidationError as e:
            return str(e)
        category = Category(**request.json)
        category.save()
        return CategorySchemaRead().dump(category)

    def put(self, id):
        try:
            CategorySchemaWrite().load(request.json)
        except ValidationError as e:
            return str(e)
        if request.json['parent_category']:
            request.json['parent_category'] = Category.objects.get(id=request.json['parent_category'])

        if request.json['sub_category']:
            for i in range(len(request.json['sub_category'])):
                request.json['sub_category'][i] = Category.objects.get(id=request.json['sub_category'][i])

        if request.json['products']:
            for i in range(len(request.json['products'])):
                request.json['products'][i] = Product.objects.get(id=request.json['products'][i])

        category = Category.objects.get(id=id)
        category.update(**request.json)
        category.reload()
        return CategorySchemaRead().dump(category)

    def delete(self, id):
        Category.objects.get(id=id).delete()
        return str({"status": "deleted"})


class TotalPriceResource(Resource):
    def get(self):
        return str({"Total price": total_price_all_product_in_shop()})
