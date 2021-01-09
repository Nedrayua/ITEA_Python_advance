import mongoengine as me
from datetime import datetime
import json

me.connect('LESSON_10_PRACTICE')


class Post(me.Document):
    post_title = me.StringField(required=True, min_length=2, max_length=128)
    post_body = me.StringField(required=True, min_length=16, max_length=2024)
    date_of_publication = me.StringField()
    author = me.ReferenceField('Author')
    num_of_views = me.IntField(default=0)
    tag = me.ListField(me.ReferenceField('Tag'))

    def save(self, *args, **kwargs):
        self.date_of_publication = str(datetime.today().strftime('%d.%m.%Y %H:%M:%S'))
        super().save(*args, **kwargs)

    def add_view(self):
        self.num_of_views += 1
        self.save()

    def add_tag(self, tag):
        self.tag.append(tag)
        self.save()
        tag.post.append(self)
        tag.save()

    def add_author(self, author):
        self.author = author
        self.save()
        author.publication.append(self)
        author.num_of_publication += 1


class Tag(me.Document):
    tag_name = me.StringField(required=True, min_length=2, max_length=32)
    post = me.ListField(me.ReferenceField('Post'))

    def get_posts_of_tag(self):
        queryset = []
        for post in self.post:
            queryset.append(json.loads(post.to_json()))
        return queryset


class Author(me.Document):
    name = me.StringField(required=True, min_length=2, max_length=256)
    surname = me.StringField(required=True, min_length=2, max_length=256)
    publication = me.ListField(me.ReferenceField('Post'))
    num_of_publication = me.IntField(default=0)

    def get_posts_of_author(self):
        queryset = []
        for post in self.publication:
            queryset.append(json.loads(post.to_json()))
        return queryset
