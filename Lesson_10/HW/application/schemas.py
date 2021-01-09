from marshmallow import Schema, fields
from marshmallow.validate import Range, Length


class ProductSchema(Schema):
    id = fields.String()
    name = fields.String(validate=Length(min=2, max=128), required=True)
    is_available = fields.Boolean()
    num_available = fields.Integer()
    price = fields.Integer()
    category = fields.String()
    num_of_view = fields.Integer()


class CategorySchema(Schema):
    id = fields.String()
    name = fields.String(validate=Length(min=2, max=64), required=True)
    description = fields.String(validate=Length(min=2, max=1024))
    parent_category = fields.String()
    sub_category = fields.List(fields.String())
    products = fields.List(fields.String())


