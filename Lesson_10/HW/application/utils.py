import random
import json
from models import Product, Category

parent_category = {
    'Бытованя техника': ['Телефоны', 'Стиральные машины', 'Телевизоры'],
    'Продукты питания': ['Молочные продукты', 'Фрукты, ягоды', 'Кондитерские изделия'],
    'Сантехника': ['Трубы', 'Фитинги', 'Строительные нструменты']
}
sub_categories = {
    'Молочные продукты': ['Молоко', 'Кефир', 'Творог'],
    'Фрукты, ягоды': ['Яблоки', 'Черника', 'Бананы'],
    'Кондитерские изделия': ['Торт Капучино', 'Печенье', 'Конфеты Ромашка'],
    'Трубы': ['Труба полипропиленовая c стекловолокном Valtec', 'Труба полипропиленовая Underprice',
              'Труба полипропиленовая UP! (Underprice) PN16 20x2,8'],
    'Фитинги': ['Муфта полипропиленовая Koer с наружной резьбой 32x1', 'Муфта обжимна APE наружня різьба 20 Н 1/2',
                'Сгон американка 1/2" прямой KOER KR.341'],
    'Строительные нструменты': ['Шлифмашина угловая Dnipro-M GL-125S', 'Лазерный уровень Dnipro-M ML-230',
                                'Миксер строительный EM14-140'],
    'Телефоны': ['Мобільний телефон Samsung Galaxy A31 4/128GB Prism Crush Blue',
                 'Мобільний телефон Nokia 105 TA-1203 Single Sim 2019 Black',
                 'Мобільний телефон Nokia 3.4 3/64 GB Charcoal'],
    'Стиральные машины': ['Стиральная машина Bosch WAJ20170UA', 'Стиральная машинаSAMSUNG WF60F1R2E2WDUA',
                          'Стиральная машина  ELECTROLUX EW6S4R27BX'],
    'Телевизоры': ['Телевизор Samsung UE55RU7300UXUA', 'Телевизор Kivi 32H510KD', 'Телевизор LG 43UN71006LB']
}

products = {
    'Молоко': 20,
    'Кефир': 24,
    'Творог': 70,
    'Яблоки': 23,
    'Черника': 80,
    'Бананы': 30,
    'Торт Капучино': 250,
    'Печенье Арлекино': 60,
    'Конфеты Ромашка': 54,
    'Труба полипропиленовая c стекловолокном Valtec': 35,
    'Труба полипропиленовая Underprice': 40,
    'Труба полипропиленовая UP! (Underprice) PN16 20x2,8': 25,
    'Муфта полипропиленовая Koer с наружной резьбой 32x1' : 45,
    'Муфта обжимна APE наружня різьба 20 Н 1/2': 70,
    'Сгон американка 1/2" прямой KOER KR.341': 65,
    'Шлифмашина угловая Dnipro-M GL-125S': 1250,
    'Лазерный уровень Dnipro-M ML-230': 2500,
    'Миксер строительный EM14-140': 1430,
    'Мобильний телефон Samsung Galaxy A31 4/128GB Prism Crush Blue': 5400,
    'Мобильний телефон Nokia 105 TA-1203 Single Sim 2019 Black': 980,
    'Мобильний телефон Nokia 3.4 3/64 GB Charcoal': 4900,
    'Стиральная машина Bosch WAJ20170UA': 4800,
    'Стиральная машинаSAMSUNG WF60F1R2E2WDUA': 6700,
    'Стиральная машина  ELECTROLUX EW6S4R27BX': 8000,
    'Телевизор Samsung UE55RU7300UXUA': 14000,
    'Телевизор Kivi 32H510KD': 11000,
    'Телевизор LG 43UN71006LB': 13000

}

parent_category_describes = {
    'Бытованя техника': 'Электроческие и механические приборы, которые выполняют некоторые бытовые функции',
    'Продукты питания': 'Продукты для повседневного питания',
    'Сантехника': 'Системы непрерывного водоснабжения потребителей, предназначенная для проведения воды для питья'
                  ' и технических целей из одного места (обыкновенно водозаборных сооружений) в другое',
}

sub_category_describes = {
    'Молочные продукты': 'пищевые продукты, вырабатываемые из молока. Переработка молока в пищевые продукты'
                         ' производится для придания особых вкусовых качеств и повышения устойчивости к хранению',
    'Фрукты, ягоды': 'Фрукт (лат. fructus — плод) — сочный съедобный плод растения. Фрукты являются важной'
                     ' составляющей пищи человека и многих животных',
    'Кондитерские изделия': 'Это сладкие продукты, отличающиеся приятными вкусом и ароматом, красивым внешним видом,'
                            ' высокой пищевой ценностью, а также хорошей усвояемостью. ',
    'Трубы': 'Цилиндрическое изделие, полое внутри, имеющее длину, значительно превосходящую диаметр. Предназначены'
             'для транспортировки воды',
    'Фитинги': 'Соединительная часть трубопровода, устанавливаемого для разветвления, поворотов, переходов на другой'
               ' диаметр, а также при необходимости частой сборки и разборки труб.',
    'Строительные нструменты': 'инструменты, используемые преимущественно при производстве строительных, монтажных'
                               ' и ремонтно-строительных работ.',
    'Телефоны': 'Телекоммуникацинные приборы разных разновидностей, основным назначением которых является связь '
                'поддержка коммуникационной связи',
    'Стиральные машины': 'Установка для стирки текстильных изделий (одежды, нижнего и постельного белья, сумок и'
                         ' других вещей)',
    'Телевизоры': 'Приёмник телевизионных сигналов изображения и звукового сопровождения, отображающий их на экране'
                  ' и с помощью динамиков. '

}


def create_category(collection_names, collection_describes):
    for cat in collection_names.keys():
        try:
            Category.objects().get(name=cat)
        except:
            Category(name=cat, description=collection_describes[cat]).save()


def create_product(dict_products: dict):
    for product in dict_products.keys():
        try:
            Product.objects().get(name=product)
        except:
            Product(name=product, num_available=random.randint(1, 20), price=dict_products[product]).save()


    # name = me.StringField(required=True, min_length=2, max_length=128)
    # is_available = me.BooleanField(default=True)
    # num_available = me.IntField(default=0)
    # price = me.IntField(default=0)
    # category = me.ReferenceField('Category')
    # num_of_view = me.IntField(default=0)


def link_sub_object(collection_names, category=True):
    if category:
        objects = Category.objects()
    else:
        objects = Product.objects()
    for sub_object in objects:
        for key in collection_names.keys():
            if sub_object.name in collection_names[key]:
                cat = Category.objects().get(name=key)
                if category:
                    cat.add_sub_category(sub_object)
                else:
                    cat.add_product(sub_object)


def total_price_all_product_in_shop():
    products = Product.objects()
    total_price = 0
    for product in products:
        total_price += product.sum_total_price()
    return total_price


create_category(parent_category, parent_category_describes)
create_category(sub_categories, sub_category_describes)
link_sub_object(parent_category)
create_product(products)
link_sub_object(sub_categories, False)
