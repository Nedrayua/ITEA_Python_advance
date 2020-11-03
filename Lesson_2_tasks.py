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
total_market = dict()
class Fish:
    def __init__(self, kind_of_fish, price, quantity):
        self.kind_of_fish = kind_of_fish
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return f"Fish (ID goods {id(self)}, kind of fish: {self.kind_of_fish}, quantity: {self.quantity})"


class FishMarket:
    def __init__(self, name, initial_profit, *fishs):
        self.name = name
        self.initial_profit = initial_profit
        self.fishs = {id(fish): fish for fish in fishs}
        self.profit = initial_profit
        profit = {name: self.profit}
        total_market.update(profit)

    def __str__(self):
        return '\n'.join(str(fish) for fish in self.fishs.values()) + f"\n===\nОбщая выручка = {self.profit}\n {'=' * 35}"

    def sell(self, fish, sum):
        fish = self.fishs[id(fish)] #для упрощения дальнешего кода
        fish.quantity -= sum
        self.profit += (fish.price * sum)
        temp_profit = {self.name: self.profit}
        total_market.update(temp_profit)
        print(f"Зоомагазин {self.name} продал рыбку {fish.kind_of_fish} в колличестве {sum} штук.\n"
              f"Выручка от операции: {fish.price * sum} грн.\nОбщая выручка: {total_market[self.name]}")
        print('=' * 35)

#    def sales_profit:
#        pass
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