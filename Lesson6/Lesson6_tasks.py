# 1) Создать свою структуру данных Список, которая поддерживает
# индексацию. Методы pop+, append+, insert+, remove+, clear+. Перегрузить
# операцию сложения для списков (__add__), которая возвращает новый расширенный
# объект.
# 2) Создать свою структуру данных Словарь, которая поддерживает методы,
# get, items, keys, values. Так же перегрузить операцию сложения для
# словарей, которая возвращает новый расширенный объект.
# Указанные методы описываем самостоятельно, без использования
# стандартных.


class CustomList:
    def __init__(self, size=0, sequence=0):
        self._list = [0] * size
        if sequence != 0:
            self._list = [0] * len(sequence)
            for i in range(len(sequence)):
                self._list[i] = sequence[i]

    def __str__(self):
        if len(self._list) > 0:
            x = f"["
            for i in self._list:
                x += f'{i}, '
            return x[:-2] + f']'
        else:
            return f'[]'

    def __getitem__(self, item):
        return self._list[item]

    def __setitem__(self, key, value):
        self._list[key] = value

    def c_pop(self, index=-1):
        new_list = [0] * (len(self._list)-1)
        temp = self._list[index]
        for i in range(0, len(self._list)-1):
            new_list[i] = self._list[i]
        self._list = new_list
        return temp

    def c_append(self, num):
        result = self._list + [num]
        self._list = result
        return self._list

    def c_insert(self, index, num):
        self._list += [0]
        for i in range(len(self._list)-1, index, -1):
            self._list[i] = self._list[i-1]
        self._list[index] = num
        return self._list

    def c_remove(self, num):
        if num in self._list:
            count = 0
            for i in self._list:
                if num == i:
                    break
                else:
                    count += 1
            for i in range(count, len(self._list)-1):
                self._list[i] = self._list[i+1]
            return self._list.pop()
        else:
            raise ValueError

    def c_clear(self):
        self._list = []
        return self._list

    def __add__(self, other):
        new_list = self._list + other._list
        self._list = new_list
        return CustomList(0, self._list)


l = CustomList(5)
h = CustomList()
l[0] = 5
l[1] = 15
l[2] = 1222

print(l)
l.c_pop()
print(l)
l.c_append(10)
print(l)
l.c_insert(2, [3, 5])
h.c_append(5)
h.c_append(0)
h.c_append(4)
h.c_append(10)
print(l)
l.c_remove(1222)
print(l)
print(h)
d = l + h
print(f'd = {d}, {type(d)}')
l.c_clear()
print(l)

# 2) Создать свою структуру данных Словарь, которая поддерживает методы,
# # get+, items, keys, values. Так же перегрузить операцию сложения для
# # словарей, которая возвращает новый расширенный объект.
# # Указанные методы описываем самостоятельно, без использования
# # стандартных.

class CustomDict:

    def __init__(self, dict_data):
        self._dict = dict()
        for k, v in dict_data.items():
            self._dict[k] = v

    def __str__(self):
        x = f'{{'
        for k, v in self._dict.items():
            x += f'{repr(k)}: {repr(v)}, '
        return x[:-2] + f'}}'

    def __add__(self, other):
        for k in other._dict:
            self._dict[k] = other._dict[k]
            return CustomDict(self._dict)

    def __getitem__(self, item):
        return self._dict[item]

    def __setitem__(self, key, value):
        self._dict[key] = value

    def c_get(self, key, default=None):
        if key in self._dict.keys():
            return self._dict[key]
        else:
            return default

    def c_items(self):
        dict_items = []
        for k in self._dict:
            v = self._dict[k]
            dict_items.append((k, v))
        return dict_items

    def c_keys(self):
        dict_keys = []
        for k in self._dict:
            dict_keys.append(k)
        return dict_keys

    def c_values(self):
        dict_values = []
        for k in self._dict:
            dict_values.append(self._dict[k])
        return dict_values


c = {'key': 'value'}
b = {'a1': 1, 'a2': 2}
d = CustomDict(c)
dd = CustomDict(b)
print(d, type(d), dd, type(dd))
ddd = d + dd
print(f'ddd {ddd}, {type(ddd)}')
print(type(ddd))
print(d.c_get('key', 'Default default'))
print(ddd.c_items())
