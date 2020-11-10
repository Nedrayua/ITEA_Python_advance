# Создать декоратор, который принимает на вход аргумент «количество
# повторений». Который будет вызывать функцию, определенное кол-во
# раз. Декорируемая функция должна возвращать:
# 1) Количество времени затраченное на каждый вызов;
# 2) Количество времени затраченное в общей сложности на все
# вызовы;
# 3) Имя декорируемой функции;
# 4) Значение последнего результата выполнения.
# декоратор должен уметь  использовать непределенное колличество позиционных аргументов


def decorator(iters):

    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            time_mark = 0
            num_iter = 1
            for i in range(iters):
                print(f"{num_iter}-я итерация:")
                begin_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                time_mark = time_mark + (end_time - begin_time)
                num_iter += 1
            print(f"Время затраченное на вызов составило: {end_time - begin_time}, \n"
                  f"Общее колличество времени затраченное на все вызовы: {time_mark}\n"
                  f"Имя декорируемой функции: '{func.__name__}'")
            return result

        return wrapper

    return actual_decorator


@decorator(100)
def square(weight, length):
    print(weight * length)
    return weight * length


@decorator(10)
def overxertion(num, degree):
    for i in range(num):
        print(f"{i} в степени {degree} = {i ** degree}")

a = dict()

@decorator(1)
def up_dict(key, value, dict_):
    temp = {key: value}
    dict_.update(temp)


z = square(10, 20)
z1 = overxertion(7, 100000)
up_dict(5, 20, a)
print(a)