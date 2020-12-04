# 1) Написать контекстный менеджер для работы с SQLite DB.
import sqlite3


class ManagerSQdb:

    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.connect = sqlite3.connect(self.db_name)
        return self.connect

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connect.close()


# with ManagerSQdb('cars.db') as connect:
#     cursor = connect.cursor()
#     cursor.execute('SELECT * FROM parking')
#     print(cursor.fetchall())


# 2) Создать базу данных студентов. У студента есть факультет,
# группа, оценки, номер студенческого билета. Написать программу,
# с двумя ролями: Администратор, Пользователь. Администратор
# может добавлять, изменять существующих студентов.
# Пользователь может получать список отличников, список всех
# студентов, искать студентов по по номеру студенческого, получать
# полную информацию о конкретном студенте (включая оценки,
# факультет)
def view_student(st_card):
    """Получить полную информацию о студенте"""
    with ManagerSQdb('university.db') as connect:
        cursor = connect.cursor()
        cursor.execute(f'SELECT students.name, students.surname, students.date_of_birth, groups.name_group,'
                        f' faculty.name_faulty'
                        f' FROM students'
                        f' LEFT JOIN groups'
                        f' ON students.group_id = groups.id'
                        f' LEFT JOIN faculty'
                        f' ON faculty.id = groups.faculty_id'
                        f' WHERE students.student_card = ?', (st_card,))
        result = cursor.fetchone()
        view = f'{"=" * 100}\n' \
               f'Студенческий билет: №{st_card}, Имя: {result[0]}, фамилия: {result[1]},' \
               f'дата рождения: {result[2]}, группа: {result[3]}, факультет: {result[4]}\n'

        cursor.execute(f'SELECT subjects.name_subject, grades.mark FROM subjects JOIN grades'
                       f' ON subjects.id = grades.id_subject'
                       f' JOIN students ON students.student_card = grades.id_student'
                       f' WHERE students.student_card = ?', (st_card,))
        view += f'Оценки:'
        while cursor:
            result = cursor.fetchone()
            if not result:
                break
            view2 = f'\n{result[0]}: {result[1]};'
            view += view2
        return view[:-1] + f'.'


def find_student(st_card):
    """ Поиск студента по студенческому"""
    with ManagerSQdb('university.db') as connect:
        cursor = connect.cursor()
        cursor.execute(f'SELECT students.name, students.surname, students.date_of_birth, groups.name_group'
                       f' FROM students'
                       f' LEFT JOIN groups'
                       f' ON students.group_id = groups.id'
                       f' WHERE students.student_card = ?', (st_card,))
        result = cursor.fetchone()
        view = f'{"=" * 70}\n' \
               f'Студенческий билет: №{st_card}, имя: {result[0]}, фамилия: {result[1]}, ' \
               f'дата рождения: {result[2]}, группа: {result[3]}\n' \
               f'{"=" * 70}'
        return view


def view_all_student():
    """Просмотр всех студентов"""
    with ManagerSQdb('university.db') as connect:
        cursor = connect.cursor()
        cursor.execute(f'SELECT students.student_card, students.name, students.surname, students.date_of_birth,'
                       f' groups.name_group FROM students'
                       f' LEFT JOIN groups'
                       f' ON students.group_id = groups.id')
        view = f'Перечень всех студентов:\n'
        while cursor:
            result = cursor.fetchone()
            if not result:
                break
            view_temp = f'Студенческий билет: №{result[0]}, имя: {result[1]}, фамилия: {result[2]}, ' \
                        f'дата рождения: {result[3]}, группа: {result[4]};\n'
            view += view_temp
        return view[:-1] + f'.'


def view_excellent():
    """Поиск всех отличников"""
    with ManagerSQdb('university.db') as connect:
        cursor = connect.cursor()
        cursor.execute(f' SELECT st.student_card, st.name, st.surname, groups.name_group, marks_table.averege_mark'
                       f' FROM students as st'
                       f' INNER JOIN (SELECT AVG(mark) as averege_mark, id_student FROM grades'
                       f' GROUP BY id_student) as marks_table'
                       f' ON st.student_card = marks_table.id_student '
                       f' INNER JOIN groups '
                       f' ON groups.id = st.group_id '
                       f' WHERE marks_table.averege_mark > 4')
        view = f'Список отличников:\n' \
               f'{"=" * 80}\n'
        while cursor:
            result = cursor.fetchone()
            if not result:
                break
            temp = f'Студенческий билет: №{result[0]}, Имя: {result[1]}, фамилия: {result[2]}, группа: {result[3]}\n' \
                   f'Средний балл: {result[4]}\n' \
                   f'{"=" * 80}\n'
            view += temp
        return view


print(view_excellent())


def change_student(st_card, param, new_param):
    """Изменение данных по студенту"""
    with ManagerSQdb('university.db') as connect:
        cursor = connect.cursor()
        cursor.execute(f' UPDATE students'
                       f' SET {param}="{new_param}"'
                       f' WHERE student_card = {st_card}')
        connect.commit()


#change_student(1, "surname", "Кирилюк")

def create_student(name, surname, date_of_birth, group_id):
    """Создание студента"""
    with ManagerSQdb('university.db') as connect:
        cursor = connect.cursor()
        cursor.execute(f' INSERT INTO students (name, surname, date_of_birth, group_id)'
                       f' VALUES ("{name}", "{surname}", "{date_of_birth}", {group_id})')
        connect.commit()


#create_student('Александр', 'Николаенко', '12.02.1999', 2)


def rate_student(mark, subj_id, st_card):
    with ManagerSQdb('university.db') as connect:
        cursor = connect.cursor()
        cursor.execute(f' INSERT INTO grades (mark, id_subject, id_student)'
                       f' VALUES ({mark}, {subj_id}, {st_card})')
        connect.commit()

def create_user(login, password, is_admin):
    user = {login: {'password': password, 'admin': is_admin}}
    return users.update(user)


def check_user(login, password):
    if login not in users.keys() or password != users[login]['password']:
        return False
    else:
        return True


users = {'qwerty': {'password': 'qwerty', 'admin': True}}

run = True
while run:
    answer = int(input("Если хотите зарегистрироваться введите 1, если войти введите - 2"))
    if answer == 1:
        run3 = True
        while run3:
            login = input("Введите логин")
            if login in users.keys():
                print("Логин уже зарезервирован")
                run3 = True
            else:
                run3 = False
        password = input("Введите пароль")
        run2 = True
        while run2:
            is_admin = int(input("Если Вы админ, введите 1, если нет - 0"))
            if is_admin == 1 or is_admin == 0:
                run2 = False
            else:
                run2 = True
        create_user(login, password, bool(is_admin))
        run = True
    if answer == 2:
        login = input("Введите логин")
        password = input("Введите пароль")
        if check_user(login, password) == True:
            admin = users[login]['admin']
            print(f'Вы вошли как {"админ" if admin == True else "пользователь"}')
            run4 = True
            while run4:
                print('Вы в меню')
                answer2 = int(input(f'Для того, что бы добавить студента - введите 1 (права админа);'
                                    f'Для изменения существующего студента - введите 2 (права админа);'
                                    f'Получить список отличников - введите 3'
                                    f'Для получения списка всех студентов - введите 4'
                                    f'Для поиска студента по номеру студенческого - введите 5'
                                    f'Полная информация о конкретном студенте - введите 6'
                                    f'Если хотите выйти - введите 0'))
                if answer2 == 1:
                    if admin:
                        st_name = input('Введите имя студента')
                        st_surname = input('введите фамилию')
                        st_date_birth = input('Дату рождения')
                        group_id = input('Введите id группы')
                        try:
                            create_student(st_name, st_surname, st_date_birth, group_id)
                        except Exception:
                            print('Неправеильный ввод')
                            run4 = True
                    else:
                        print('Вы не админ')
                elif answer2 == 2:
                    if admin:
                        st_card = input("Введите номер студенческого")
                        st_param = input("Введите название параметра для изменения")
                        st_new_param = input("Введите новый параметр")
                        try:
                            change_student(st_card, st_param, st_new_param)
                        except Exception:
                            print('Неправеильный ввод')
                            run4 = True
                    else:
                        print("Вы не админ")
                elif answer2 == 3:
                    view_excellent()
                elif answer2 == 4:
                    view_all_student()
                elif answer2 == 5:
                    st_card = input("Введите № студенческого")
                    try:
                        find_student(st_card)
                    except Exception:
                        print("Введены неверные данные")
                elif answer2 == 6:
                    st_card = input("Введите № студенческого")
                    try:
                        view_student(st_card)
                    except Exception:
                        print("Введены неверные данные")

                elif answer2 == 0:
                    run4 = False
                else:
                    print("Введены не верные данные")
        else:
            print('You are out')
            run = True
    else:
        run = False

print("Goodbye")
