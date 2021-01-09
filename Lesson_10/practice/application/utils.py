import random
import json

from models import Post, Tag, Author

titles = ['Инфорация о погоде', 'Погода бушует', 'Погодная катострофа']


posts = ['На полуострове Малайзия обострились наводнения, и в настоящее время около 25 тысяч человек покинули свои'
         ' дома в 7 штатах.', 'Филиппинское информационное агентство (PNA) сообщило о наводнении в центральных районах'
         ' страны с 1 января 2021 года из-за сильного дождя, принесенного циклоном', 'Поисково-спасательные группы в'
         ' Норвегии в понедельник продолжают поиск трех пропавших без вести людей в результате огромного оползня,'
         ' в результате которого погибли семь человек.']

tags = ['Погода', 'Катастрофы']

NAME = ['Николай', 'Дмитрий', 'Богдан', 'Руслан', 'Владимир', 'Андрей', 'Сергей', 'Лев', 'Михаил', 'Александр']
SURNAME = ['Иванов', 'Петров', 'Сидоров', 'Николаев', 'Сергеев', 'Алексеев', 'Непоседов', 'Кругомбегов',
           'Спатьнехотелов', 'Меблепортель']


def random_author_post():
    posts = Post.objects()
    author = Author.objects()
    for post in posts:
        post.add_author(random.choice(author))


def random_teg_post():
    posts = Post.objects()
    tags = Tag.objects()
    for post in posts:
        post.add_tag(random.choice(tags))


def get_post_of_tag(tag_id):
    tag = Tag.objects.get(id=tag_id)
    queryset = []
    for post in tag.post:
        queryset.append(json.loads(post.to_json()))
    return queryset


 # if __name__ == '__main__':

    # for i in range(5):
    #     post = Post(post_title=random.choice(titles), post_body=random.choice(posts))
    #     post.save()

    # for i in range(2):
    #     Author(name=random.choice(NAME), surname=random.choice(SURNAME)).save()

    # for i in tags:
    #     Tag(tag_name=i).save()
    # random_author_post()
    #random_teg_post()

