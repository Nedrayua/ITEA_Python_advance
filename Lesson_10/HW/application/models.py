import mongoengine as me


me.connect('Lesson10_HW')


class Product(me.Document):
    name = me.StringField(required=True, min_length=2, max_length=128)
    is_available = me.BooleanField(default=True)
    num_available = me.IntField(default=0)
    price = me.IntField(default=0)
    category = me.ReferenceField('Category')
    num_of_view = me.IntField(default=0)

    def sum_total_price(self):
        return self.price * self.num_available

    def add_view(self):
        self.num_of_view += 1
        self.save()


class Category(me.Document):
    name = me.StringField(required=True, min_length=2, max_length=64)
    description = me.StringField(required=True, min_length=2, max_length=1024)
    parent_category = me.ReferenceField('Category')
    sub_category = me.ListField(me.ReferenceField('Category'))
    products = me.ListField(me.ReferenceField('Product'))

    def add_sub_category(self, category):
        self.sub_category.append(category)
        category.parent_category = self
        self.save()
        category.save()

    def add_product(self, product):
        self.products.append(product)
        product.category = self
        self.save()
        product.save()



