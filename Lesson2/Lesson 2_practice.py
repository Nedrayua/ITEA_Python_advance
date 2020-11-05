#Поехали!
#Task 1
#  Создать класс автомобиля. Создать классы легкового автомобиля
# и грузового. Описать в основном классе базовые атрибуты и методы
# для автомобилей. Будет плюсом если в классах наследниках
# переопределите методы базового класса!
class BaceAvto:
    def __init__(self, model, fuel_volum, fuel_consumption, type_of_fuel, average_speed):
        self.model = model
        self.fuel_volum = fuel_volum
        self.fuel_consumption = fuel_consumption
        self.type_of_fuel = type_of_fuel
        self.average_speed = average_speed

    def refueling(self, distance):
        print(f"Для покрытия маршрута в {distance} километров, {self.model} необходимо заправить\n"
              f"{(distance / 100) * self.fuel_consumption} литров {self.type_of_fuel}\n"
              f"Расчетное время поездки не меньше {distance/self.average_speed} часов")
    def forward(self):
        print(f"Транспортное средство {self.model} движется вперед")
    def left(self):
        print(f"Транспортное средство {self.model} движется влево")
    def right(self):
        print(f"Транспортное средство {self.model} движется вправо")
    def back(self):
        print(f"Транспортное средство {self.model} движется назад")
    def brake_(self):
        print(f"Транспортное средство {self.model} останавливается")

class Bus(BaceAvto):
    def brake_(self):
        print(f"Автобус {self.model} останавливается")
    def bus_stop(self):
        self.brake_()
        print(f"Открываются двери для входа и выхода пассажиров\n"
              f"Двери закрываются")
class Truk(BaceAvto):
    def brake_(self):
        print(f"Грузовик {self.model} останавливается")
    def stop_maneuvers(self):
        print(f"Транспортное средство выполняет маневры для парковки")
    def loading_(self):
        self.stop_maneuvers()
        self.brake_()
        print(f"Выполняется загрузка")
    def unloading_(self):
        self.stop_maneuvers()
        self.brake_()
        print(f"Выполняется разгрузка")
avto1 = BaceAvto('Volvo XC 70', 50, 8, "дизельное топливо", 120)
avto2 = Bus('Neoplan, N1216', 300, 15, 'дизельное топливо', 110)
avto3 = Truk('Man, TGX-18510', 370, 20, 'дизельное топливо', 110)
avto1.refueling(500)
print("-" * 50)
avto1.forward()
print("-" * 50)
avto1.left()
print("-" * 50)
avto1.brake_()
print("-" * 50)
avto2.right()
print("-" * 50)
avto2.brake_()
print("-" * 50)
avto2.bus_stop()
print("-" * 50)
avto3.loading_()
print('=' * 50)

#Task 2
# Создать класс магазина. Конструктор должен инициализировать
# значения: «Название магазина» и «Количество проданных
# товаров». Реализовать методы объекта, которые будут увеличивать
# кол-во проданных товаров, и реализовать вывод значения
# переменной класса, которая будет хранить общее количество
# товаров проданных всеми магазинами.
#total_market = dict()
class Fish:
    def __init__(self, kind_of_fish, price, quantity):
        self.kind_of_fish = kind_of_fish
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return f"Fish (ID goods {id(self)}, kind of fish: {self.kind_of_fish}, quantity: {self.quantity})"


class FishMarket:
    total = 0
    def __init__(self, name, initial_profit, *fishs):
        self.name = name
        self.initial_profit = initial_profit
        self.fishs = {id(fish): fish for fish in fishs}
        self.profit = initial_profit
        FishMarket.total += initial_profit


    def __str__(self):
        return '\n'.join(str(fish) for fish in self.fishs.values()) + f"\n===\nОбщая выручка = {self.profit}\n" \
                f" {'=' * 35}\nОбщая выручка всех магазинов сети: {FishMarket.total}\n{'=' * 35}"

    def sell(self, fish, sum):
        fish = self.fishs[id(fish)] #для упрощения дальнешего кода
        fish.quantity -= sum
        self.profit += (fish.price * sum)
        FishMarket.total += (fish.price * sum)
        print(f"Зоомагазин {self.name} продал рыбку {fish.kind_of_fish} в колличестве {sum} штук.\n"
              f"Выручка от операции: {fish.price * sum} грн.\nОбщая выручка магазина: {self.profit}\n"
              f"Общая выручка всех магазинов сети: {FishMarket.total}")
        print('=' * 35)

fish1 = Fish('Macrognatus', 50, 25)
fish2 = Fish('Taractum', 45, 11)
fish3 = Fish('Poecilia', 9, 60)
fish4 = Fish('Siamese algae eater', 15, 25)

zoomag1 = FishMarket('Aqua', 1500, fish1, fish2, fish3, fish4)
print(zoomag1)
zoomag2 = FishMarket('Silence', 900, fish2, fish3, fish4)
print(zoomag2)
zoomag2.sell(fish4, 15)
print(zoomag2)

# Создать класс точки, реализовать конструктор который
# инициализирует 3 координаты (Class): Определенный программистом тип данных.x, y, z).
# Реалзиовать методы дляполучения и изменения каждой из координат.
# Перегрузить для этого класса методы сложения, вычитания, деления умножения.
# Перегрузить один любой унарный метод.
# Ожидаемый результат: умножаю точку с координатами 1,2,3 на
# другую точку с такими же координатами, получаю результат 1, 4, 9.

class Point:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
    def __str__(self):
        return f"Точка х = {self.x}, точка у = {self.y}, точка z = {self.z}"

    def get_coor(self, coor):
        if coor == 'x':
            return f"{self.x}"
        elif coor == 'y':
            return f"{self.y}"
        elif coor == "z":
            return f"{self.z}"
        else:
            return f"Неверные данные"
    def change_coor(self, coor):
        change = int(input(f"Введите новое значение точки {coor}"))
        if coor == 'x':
            self.x = change
        elif coor == 'y':
            self.y = change
        elif coor == "z":
            self.z = change
        else:
            return f"Неверные данные"

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        return Point(new_x, new_y, new_z)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z
        return Point(new_x, new_y, new_z)

    def __mul__(self, other):
        new_x = self.x * other.x
        new_y = self.y * other.y
        new_z = self.z * other.z
        return Point(new_x, new_y, new_z)

    def __truediv__(self, other):
        new_x = self.x / other.x
        new_y = self.y / other.y
        new_z = self.z / other.z
        return Point(new_x, new_y, new_z)

    def __pos__(self):
        new_x = self.x + self.x
        new_y = self.y + self.y
        new_z = self.z + self.z
        return Point(new_x, new_y, new_z)

point1 = Point(5, 8, 10)
point2 = Point(8, 5, 7)
print(point1)
print(point1.get_coor('y'))
point1.change_coor("x")
print(point1)
point3 = point1 + point2
print(point3)
point4 = point1 - point2
print(point4)
point5 = point1 * point2
print(point5)
point6 = point1 / point2
print(point6)
point1 += point1
print(point1)