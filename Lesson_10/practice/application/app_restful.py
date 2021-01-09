from flask import Flask
from flask_restful import Api
from resources import PostResource, AuthorResource, TagResource

app = Flask(__name__)
api = Api(app)

api.add_resource(PostResource, '/post', '/post/<string:id>')
api.add_resource(AuthorResource, '/author', '/author/<string:id>')
api.add_resource(TagResource, '/tag', '/tag/<string:id>')

app.run(debug=True)