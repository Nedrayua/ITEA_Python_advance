from flask import Flask
from flask_restful import Api
from resources import ProductResource, CategoryResource, TotalPriceResource

app = Flask(__name__)
api = Api(app)

api.add_resource(ProductResource, '/product', '/product/<string:id>')
api.add_resource(CategoryResource, '/category', '/category/<string:id>')
api.add_resource(TotalPriceResource, '/totalprice')

app.run(debug=True)