# Создать классы структур данных:
# 1) Стек
# 2) Очередь.
# 3) Создать класс комплексного числа и реализовать для него
# арифметические операции (не использовать стандартный тип
# complex).

# 1) Стек


class Stack:

    def __init__(self):
        self.total_items = []

    def stack_in(self, item):
        self.total_items.insert(0, item)
        print(f"{item} => in, Stack: {self.total_items}")

    def stack_out(self):
        print(f"{self.total_items.pop(0)} => out, Stack: {self.total_items}")

    def show_stack(self):
        return self.total_items


list1 = Stack()
list1.stack_in(1)
list1.stack_in(3)
list1.stack_in(8)
list1.stack_in(2)
list1.stack_in(15)
list1.stack_out()
list1.stack_out()

# 2) Очередь.


class Queue:

    def __init__(self):
        self.total_items = []

    def queue_in(self, item):
        self.total_items.insert(0, item)
        print(f"{item} => in, Queue: {self.total_items}")

    def queue_out(self):
        print(f"{self.total_items.pop(-1)} => out, Queue: {self.total_items}")

    def show_queue(self):
        return self.total_items


list2 = Queue()
list2.queue_in(1)
list2.queue_in(3)
list2.queue_in(8)
list2.queue_in(2)
list2.queue_in(15)
list2.queue_out()
list2.queue_out()

# 3) Создать класс комплексного числа и реализовать для него
# арифметические операции (не использовать стандартный тип
# complex).


class ComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b > 0:
            return f"{self.a} + {self.b}i"
        else:
            return f"{self.a} - {abs(self.b)}i"

    def __add__(self, other):
        return ComplexNumber((self.a + other.a), (self.b + other.b))

    def __sub__(self, other):
        return ComplexNumber((self.a - other.a), (self.b - other.b))

    def __mul__(self, other):
        return ComplexNumber((self.a * other.a - self.b * other.b), (self.b * other.a + self.a * other.b))

    def __truediv__(self, other):
        return ComplexNumber(((self.a * other.a + self.b * other.b) / (other.a ** 2 + other.b ** 2)),
                    ((self.b * other.a - self.a * other.b) / (other.a ** 2 + other.b ** 2)))


z1 = ComplexNumber(-2, 3)
z2 = ComplexNumber(-3, -4)
z3 = -2 + 3j  # проверка
z4 = -3 - 4j  # проверка
print(z1 + z2)
print(z3 + z4)  # проверка
z1 = ComplexNumber(-2, 3)
z2 = ComplexNumber(-3, -4)
z3 = -2 + 3j  # проверка
z4 = -3 - 4j  # проверка
print(z1 - z2)
print(z3 - z4)  # проверка
z1 = ComplexNumber(-2, 3)
z2 = ComplexNumber(-3, -4)
z3 = -2 + 3j  # проверка
z4 = -3 - 4j  # проверка
print(z1 * z2)
print(z3 * z4)  # проверка
z1 = ComplexNumber(-2, 3)
z2 = ComplexNumber(-3, -4)
z3 = -2 + 3j  # проверка
z4 = -3 - 4j  # проверка
print(z1 / z2)
print(z3 / z4)  # проверка
