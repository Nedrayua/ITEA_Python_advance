from marshmallow import Schema, fields
from marshmallow.validate import Range, Length


class ProductSchemaRead(Schema):
    id = fields.String()
    name = fields.String(validate=Length(min=2, max=128), required=True)
    is_available = fields.Boolean()
    num_available = fields.Integer()
    price = fields.Integer()
    category = fields.Nested('CategorySchema', only=('id',))
    num_of_view = fields.Integer()


class ProductSchemaWrite(ProductSchemaRead):
    category = fields.String()


class CategorySchemaRead(Schema):
    id = fields.String()
    name = fields.String(validate=Length(min=2, max=64), required=True)
    description = fields.String(validate=Length(min=2, max=1024))
    parent_category = fields.Nested('CategorySchemaRead', only=("id", "name",))
    sub_category = fields.List(fields.Nested('CategorySchemaRead', only=("id", "name",)))
    products = fields.List(fields.Nested('ProductSchemaRead', only=("id", "name",)))


class CategorySchemaWrite(CategorySchemaRead):
    parent_category = fields.String()
    sub_category = fields.List(fields.String())
    products = fields.List(fields.String())
