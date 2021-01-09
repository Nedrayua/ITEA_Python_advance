import json
from marshmallow.exceptions import ValidationError
from flask_restful import Resource
from flask import request

from models import Post, Tag, Author
from schemas import PostSchema, TagSchema, AuthorSchema


class PostResource(Resource):
    def get(self, id=None):
        if id:
            post = Post.objects.get(id=id)
            post.add_view()
            post.reload()
            return PostSchema().dump(post)  #
        else:
            posts = Post.objects()
            return PostSchema().dump(posts, many=True)

    def post(self):
        try:
            PostSchema().load(request.json)
        except ValidationError as e:
            return str(e)
        post = Post(**request.json)
        post.save()
        return PostSchema().dump(post)

    def put(self, id):
        try:
            PostSchema().load(request.json)
        except ValidationError as e:
            return str(e)
        post = Post.objects.get(id=id)
        post.update(**request.json)
        post.reload()
        return PostSchema().dump(post)

    def delete(self, id):
        Post.objects.get(id=id).delete()
        return str({"status": "deleted"})


class AuthorResource(Resource):
    def get(self, id=None):
        if id:
            author = Author.objects.get(id=id)
            return author.get_posts_of_author()
        else:
            authors = Author.objects()
            return AuthorSchema().dump(authors, many=True)

    def post(self):
        try:
            AuthorSchema().load(request.json)
        except ValidationError as e:
            return str(e)
        author = Author(**request.json)
        author.save()
        return PostSchema().dump(author)

    def put(self, id):
        try:
            AuthorSchema().load(request.json)
        except ValidationError as e:
            return str(e)
        author = Author.objects.get(id=id)
        author.update(**request.json)
        author.reload()
        return AuthorSchema().damp(author)

    def delete(self, id):
        Author.objects.get(id=id).delete()
        return str({"status": "deleted"})


class TagResource(Resource):
    def get(self, id=None):
        if id:
            tag = Tag.objects.get(id=id)
            return tag.get_posts_of_tag()
        else:
            tags = Tag.objects()
            return TagSchema().dump(tags, many=True)

    def post(self):
        try:
            TagSchema().load(request.json)
        except ValidationError as e:
            return str(e)
        tag = Tag(**request.json)
        tag.save()
        return TagSchema().dump(tag)

    def put(self, id):
        try:
            TagSchema().load(request.json)
        except ValidationError as e:
            return str(e)
        tag = Tag.objects.get(id=id)
        tag.update(**request.json)
        tag.reload()
        return TagSchema().dump(tag)

    def delete(self, id):
        Tag.objects.get(id=id).delete()
        return str({"status": "deleted"})