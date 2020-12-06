import sqlite3


class ManagerSQdb:

    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.connect = sqlite3.connect(self.db_name)
        return self.connect

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connect.close()


def get_all_goods_db():
    with ManagerSQdb('goods.db') as connect:
        cursor = connect.cursor()
        cursor.execute(f' SELECT category.cat_of_goods, g.id, g.name_of_goods '
                       f' FROM goods as g'
                       f' JOIN category'
                       f' ON category.id = g.category_id'
                       f' WHERE g.in_stock = "available"')
        goods_dictionary = dict()
        while cursor:
            result = cursor.fetchone()
            if not result:
                break
            if goods_dictionary.get(result[0]):
                temp1 = {result[1]: {'name_of_good': result[2]}}
                goods_dictionary[result[0]].update(temp1)
            else:
                temp2 = {result[0]: {result[1]: {'name_of_good': result[2]}}}
                goods_dictionary.update(temp2)
        return goods_dictionary


def get_goods_detail_db():
    with ManagerSQdb('goods.db') as connect:
        cursor = connect.cursor()
        cursor.execute(f' SELECT g.id, g.name_of_goods, g.description, g.quantity, g.price'
                       f' FROM goods as g'
                       f' JOIN category'
                       f' ON category.id = g.category_id'
                       f' WHERE g.in_stock = "available" ')
        goods_dictionary = dict()
        while cursor:
            result = cursor.fetchone()
            if not result:
                break
            temp = {result[0]: {'name_of_good': result[1], 'description': result[2], 'quantity': result[3],
                                     'price': result[4]}}

            goods_dictionary.update(temp)
        return goods_dictionary


def get_category_db():
    with ManagerSQdb('goods.db') as connect:
        cursor = connect.cursor()
        cursor.execute(f' SELECT category.cat_of_goods FROM category')
        res_list = []
        while cursor:
            result = cursor.fetchone()
            if not result:
                break
            res_list.append(result[0])
        return res_list


def add_category_db(cat_of_goods):
    """Создание категории"""
    with ManagerSQdb('goods.db') as connect:
        cursor = connect.cursor()
        cursor.execute(f' INSERT INTO category (cat_of_goods)'
                       f' VALUES ("{cat_of_goods}")')
        connect.commit()


def add_goods_db(name_of_goods, description, price, quantity, in_stock, category_id):
    """Создание товара"""
    with ManagerSQdb('goods.db') as connect:
        cursor = connect.cursor()
        cursor.execute(f' INSERT INTO goods (name_of_goods, description, price, quantity, in_stock, category_id)'
                       f' VALUES ("{name_of_goods}", "{description}", {price},'
                       f' {quantity}, "{in_stock}", {category_id})')
        connect.commit()


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def greeting():
    return render_template('index.html')


@app.route('/categories')
def goods_cat():
    categories = get_category_db()
    return render_template('categories.html', categories=categories)


@app.route('/categories/<string:goods_name>')
def get_goods(goods_name):
    goods = get_all_goods_db()
    return render_template('list_of_goods.html', goods=goods[goods_name])


@app.route('/<int:goods_id>/')
def get_detail_goods(goods_id):
    goods = get_goods_detail_db()
    return render_template('goods_detail.html', goods=goods[goods_id])


@app.route('/add_goods', methods=["GET", "POST"])
def add_goods():
    temp = []
    if request.form:
        temp.append(request.form)
        add_goods_db(temp[0]["name_of_goods"], temp[0]["description"], temp[0]["price"],
                     temp[0]["quantity"], temp[0]["in_stock"], temp[0]["category_id"])
    return render_template('add_goods.html')


@app.route('/add_category', methods=["GET", "POST"])
def add_category():
    temp = []
    if request.form:
        temp.append(request.form)
        add_category_db(temp[0]["category"])
    return render_template('add_category.html')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

# 1) Создать базу данных товаров, у товара есть: Категория (связанная
# таблица), название, есть ли товар в продаже или на складе, цена, кол-во
# единиц.Создать html страницу. На первой странице выводить ссылки на все
# категории, при переходе на категорию получать список всех товаров в
# наличии ссылками, при клике на товар выводить его цену, полное описание и
# кол-во единиц в наличии.
# 2) Создать страницу для администратора, через которую он может добавлять
# новые товары и категории.