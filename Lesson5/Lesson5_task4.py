# Задача 2. Создать подобие социальной сети.
# 1) Создать класс авторизации, в котором описать методы регистрации, аутентификации, добавить
# методы проверки на валидность пароля (содержание символов и цифр), проверка на уникальность
# логина пользователя. В классовых переменных хранить всех пользователей сети. (Отдельно
# объекты этого класса создаваться не будут, такие классы называются миксинами)
# 2) Создать класс пользователя, наследующий класс авторизации. который будет разделять роли
# админа и простого пользователя (этот вопрос можно решить с помощью флага is_admin, либо
# создав 2 разных класса для админа и обычного пользователя и наследовать их). Класс
# пользователя должен наследовать класс авторизации. На момент создания каждого объекта этого
# класса, в переменную объекта сохранять время и дату его создания.
# 3) Создать класс поста, который имеет дату публикации и её содержимое.
# Что должно быть в клиентском коде:
# Человек заходит, и имеет возможность зарегистрироваться (ввод логин, пароль, подтверждение
# пароля), далее входит в свою учетную запись. Добавить возможность выхода из учетной записи, и
# вход в новый аккаунт.
# При входе под обычным пользователем мы можем создать новый пост, с определённым
# содержимым. Под учётной записью администратора мы можем увидеть всех пользователей нашей
# системы, дату их регистрации, и их посты.
from datetime import datetime
import shelve

FILE = 'USERS_DICT'
def upd_users(t_dict):
    with shelve.open(FILE) as db:
        db.update(t_dict)

def check_keys(key):
    with shelve.open(FILE) as db:
        if key in db.keys():
            return True
        else:
            return False

def check_user_pass(us_log, us_pass):
    with shelve.open(FILE) as db:
        if db[us_log]['password'] == us_pass:
            return True
        else:
            return False
def open_for_chec_admin(us_log):
    with shelve.open(FILE) as db:
        if db[us_log]['users'].chec_admin() == 1:
            return 1
        else:
            return 0


def print_admin():
    with shelve.open(FILE) as db:
        for i in db:
            print(db[i]['users'].view())
            for j in db[i]['posts']:
                print(j.view_post())


def append_post(us_log, post):
    with shelve.open(FILE) as db:
        db[us_log]['posts'].append(post)


class NetworkAuthorize:

    logins_net = dict()

    def registration(self):
        """
        метод регистрации
        """
        flag_log = 1
        while flag_log == 1:
            login = input("Введите логин, по которому Вас будут идентифицировать в сети")
            if check_keys(login):
                print(f"Пользователь с лгином {login} уже существует")
                flag_log = 1
            else:
                flag_log = 0
        flag_pass = 1
        while flag_pass == 1:
            password_net = input("Введите пароль, с обязательной комбинацией букв в верхнем и нижнем регистре"
                                 "и наличием цифр")
            p_test = [0, 0, 0] # p_test[0] - upper, p_test[1] - lower, p_test[2] - digit
            for i in password_net:
                if i.isupper():
                    p_test[0] += 1
                if i.islower():
                    p_test[1] += 1
                if i.isdigit():
                    p_test[2] += 1
            if 0 in p_test:
                print('Вы ввели пароль, без соблюдения условий ввода')
                flag_pass = 1
            else:
                password_conf = input('Введите подтверждение пароля')
                if password_conf == password_net:
                    flag_pass = 0
                else:
                    print('Пароли не совпадают')
        temp_dict = {login: {'password': password_net}}
        upd_users(temp_dict)
        return login, password_net


    def authontification(self):
        """
        метод аутификации
        """
        login = input('Введите логин')
        if check_keys(login):
            password = input('Введите пароль')
            if check_user_pass(login, password):
                return login, 1
            else:
                print('Не верный пароль')
                return 0, 0
        else:
            print('Неверный логин')
            return 0, 0

    def create_user_network(self, login, passwod):
        create_name = input('Введите Ваше имя')
        create_sur_name = input('Введите Вашу фамилию')
        is_you_admin = self.is_admin()
        create_time = str(datetime.now())[:-7]
        temp_dict = {login: {'password': passwod,
                             'users': UserNetwork(create_name, create_sur_name, is_you_admin, create_time), 'posts': []}}
        upd_users(temp_dict)

    def create_user_post(self, login):
        create_title = input("Введите заголовок поста")
        create_body = input("Напишите свой пост")
        create_time = str(datetime.now())[:-7]
        post = Post(create_title, create_body, create_time)
        append_post(login, post)


class UserNetwork(NetworkAuthorize):

    def __init__(self, name=0, sur_name=0, is_you_admin=0, time_of_create=str(datetime.now())[:-7]):
        self.name = name
        self.sur_name = sur_name
        self.is_you_admin = is_you_admin
        self.time_of_create = time_of_create

    def is_admin(self):
        flag = 0
        while flag == 0:
            admin = input('Вы админ? Введите 1 если да и 0 если нет')
            if admin == str(1):
                return 1
                flag = 1
            elif admin == str(0):
                return 0
                flag = 1
            else:
                flag = 0

    def chec_admin(self):
        if self.is_you_admin == 1:
            return 1
        else:
            return 0

    def view(self):
        return f'Имя: {self.name}, фамилия: {self.sur_name}\n' \
               f'Статус админа: {"Да" if self.is_you_admin == 1 else "Нет"}\n' \
               f'Дата создания: {self.time_of_create}'\


class Post(NetworkAuthorize):

    def __init__(self, title='0', body='0', time_of_create=str(datetime.now())[:-7]):
        self.title = title
        self.body = body
        self.time_of_create = time_of_create

    def view_post(self):
        return f'Дата публикации: {self.time_of_create}\n' \
               f'{self.title}\n' \
               f'{self.body}'

CONFIRM_ANSWERS = 'Yy/Дд'
DECLINE_ANSWERS = 'Nn/Нн'

print('Приветствуем Вас в недоделланной социальной сети')
u = UserNetwork()
flag = 1
while flag == 1:
    login = 0
    answer1 = input("Если хотите зарегистрироваться введите 1, если хотите войти - введите 2, если хотите выйти, "
                    "нажмите - 'Yy/Дд'")
    if answer1 == '1':
        u.create_user_network(*u.registration())
    elif answer1 == '2':
        login, temp = u.authontification()
        if temp == 1:
            flag2 = 1
            while flag2 == 1:
                print('Вы вошли в меню. К сожалению фикционал не шик, но вы можете создать публикацию'
                                'или (при наличии прав админа) просмотреть все публикации всех пользователей')
                answer2 = input('Для добавления публикации - введите 1, для просмотра публикаций'
                                ' пользователей - введите 2, для выхода из меню - введите Yy/Дд')
                if answer2 == '1':
                    u.create_user_post(login)
                elif answer2 == '2':
                    if open_for_chec_admin(login) == 1:
                        print('proof')
                        print_admin()
                    else:
                        print('Ну-ну, Вы не админ')
                elif answer2 in CONFIRM_ANSWERS:
                    flag2 = 0

    elif answer1 in CONFIRM_ANSWERS:
        flag = 0
    else:
        print('Введите предложенные комбинации')

print("Хорошего дня!")