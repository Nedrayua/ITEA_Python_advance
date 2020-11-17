# Задача 1
# Создайте класс ПЕРСОНА с абстрактным методом, позволяющим вывести
# на экран информацию о персоне, а также реализовать обычный метод
# определения возраста (в текущем году). Создайте дочерние классы:
# АБИТУРИЕНТ (фамилия, дата рождения, факультет), СТУДЕНТ (фамилия,
# дата рождения, факультет, курс), ПРЕПОДАВАТЕЛЬ (фамилия, дата
# рождения, факультет, должность, стаж), со своими методами возврата
# информации. Создайте список из объектов персон, вывести информацию о
# каждом объекте, а также организуйте поиск персон, чей возраст попадает в
# заданный с клавиатуры диапазон.

from abc import ABC, abstractmethod
from datetime import date
today_date = date.today()
person_list = ['person' + str(i) for i in range(1, 12)]


class Person:

    def __init__(self, name, sur_name, date_of_birth):
        self.name = name
        self.sur_name = sur_name
        self.date_of_birth = date_of_birth

    @abstractmethod
    def person_info(self):
        return f'Имя: {self.name}, фамилия: {self.sur_name}, дата рождения: {self.date_of_birth}'

    def person_age(self):
        temp_date = self.date_of_birth.split('.')
        temp_date.reverse()
        temp_date_today = str(today_date).split('-')
        if int(temp_date[2]) <= int(temp_date_today[2]) and int(temp_date[1]) <= int(temp_date_today[1]):
            return int(temp_date_today[0]) - int(temp_date[0])
        else:
            return int(temp_date_today[0]) - int(temp_date[0]) - 1


class Enrollee(Person):

    def __init__(self, name, sur_name, date_of_birth, faculty):
        Person.__init__(self, name, sur_name, date_of_birth)
        self.faculty = faculty

    def person_info(self):
        return f'{"=" * 20}\n{Person.person_info(self)}\nфакультет: {self.faculty}'


class Student(Person):

    def __init__(self, name, sur_name, date_of_birth, faculty, course):
        Person.__init__(self, name, sur_name, date_of_birth)
        self.faculty = faculty
        self.course = course

    def person_info(self):
        return f'{"=" * 20}\n{Person.person_info(self)}\nфакультет: {self.faculty}, курс: {self.course}'


class Teacher(Person):

    def __init__(self, name, sur_name, date_of_birth, faculty, position, year_of_start_activity):
        Person.__init__(self, name, sur_name, date_of_birth)
        self.faculty = faculty
        self.position = position
        self.experience = int(str(today_date).split('-')[0]) - int(year_of_start_activity)

    def person_info(self):
        return f'{"=" * 20}\n{Person.person_info(self)}\nфакультет: {self.faculty}, должность: {self.position},' \
               f' трудовой стаж: {self.experience} лет'


person1 = Enrollee('Анатолий', 'Григорович', '10.05.2002', 'ФизТех')
person2 = Enrollee('Михаил', 'Хай', '15.10.2002', 'ФЭМ')
person3 = Enrollee('Павел', 'Мельничук', '14.11.1999', 'ФЭМ')
person4 = Student('Ольга', 'Олехнович', '17.12.1997', 'ФЭМ', '4')
person5 = Student('Николай', 'Полищук', '25.05.1996', 'ФЭМ', '3')
person6 = Student('Дмитрий', 'Кропивницкий', '17.05.1997', 'ФизТех', '3')
person7 = Student('Богдан', 'Стрельчук', '14.10.1995', 'медсестринства', '5')
person8 = Teacher('Владимир', 'Молчанов', '15.02.1971', 'ФЭМ', 'преподаватель', '1996')
person9 = Teacher('Николай', 'Ущаповский', '11.09.1969', 'ФизТех', 'ректор', '1991')
person10 = Teacher('Лилия', 'Ткачук', '02.05.1978', 'ФизТех', 'преподаватель', '1999')
person11 = Teacher('Татьяна', 'Кулич', '05.03.1985', 'ФЭМ', 'преподаватель', '2001')

person_list = [person1, person2, person3, person4, person5, person6, person7, person8, person9, person10, person11]


def display_of_person(list_):
    for i in list_:
        print(i.person_info())


display_of_person(person_list)


def age_search(list_):
    marck_person = 0
    print('Для поиска персон по возрасту, задайте диапозон поиска:')
    start = int(input("От:"))
    end = int(input("До"))
    for i in list_:
        if i.person_age() >= start and i.person_age() <= end:
            print(i.person_info())
            marck_person += 1
    if marck_person == 0:
        print(f'{"=" * 50}\nПо заданному диапазону людей не найдено.')
    else:
        print(f'{"=" * 50}\nПо заданному диапазону найдено {marck_person} людей.')


age_search(person_list)
