from marshmallow import Schema, fields
from marshmallow.validate import Range, Length


class PostSchema(Schema):
    id = fields.String()
    post_title = fields.String(validate=Length(min=2, max=128), required=True)
    post_body = fields.String(validate=Length(min=16, max=2024), required=True)
    date_of_publication = fields.String()
    author = fields.String()
    num_of_views = fields.Integer()
    tag = fields.List(fields.String())


class TagSchema(Schema):
    id = fields.String()
    tag_name = fields.String(validate=Length(min=2, max=32), required=True)
    post = fields.List(fields.String())


class AuthorSchema(Schema):
    id = fields.String()
    name = fields.String(validate=Length(min=2, max=256), required=True)
    surname = fields.String(validate=Length(min=2, max=256), required=True)
    publication = fields.List(fields.String())
    num_of_publication = fields.Integer()

