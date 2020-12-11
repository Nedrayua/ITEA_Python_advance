import mongoengine as me

me.connect('LESSON_11_PRACTICE')


class GuestProfile(me.Document):
    from_user_id = me.IntField()
    fio = me.StringField(min_length=2, max_length=256)
    num_phone = me.StringField(min_length=12, max_length=12)
    post = me.StringField()
    address = me.StringField()
    wishes = me.StringField(max_length=256)

    def __str__(self):
        return f"id: {self.from_user_id}"

