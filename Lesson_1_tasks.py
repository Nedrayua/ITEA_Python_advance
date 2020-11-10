
#Задача 1
list_of_numbers = [x for x in range(1, 20, 1)]
for i in list_of_numbers:
    if i % 2 == 0:
        print(i)
#Задача 2
dict_of_countries = {
    'Австралия': 'Сидней',
    'Белоруссия': 'Минск',
    'Бразилия': 'Бразилиа',
    'Канада': 'Отава',
    'Китай': 'Пекин',
    'США': 'Нью-Йорк',
    'Турция': 'Анкара',
    'Украина': 'Киев',
    'Япония': 'Токио'
}
list_of_countries = ['Австралия', 'Канада', 'Китай', 'Украина', 'Япония']
for i in list_of_countries:
    if i in dict_of_countries.keys():
        print(f'город {dict_of_countries[i]} - столица страны {i}')

#задача 3
list_of_numbers = [x for x in range(1, 100)]
for i in list_of_numbers:
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)
#Задача 4
def bank(sum_of_dep, years, percent):
    total_sum = sum_of_dep
    for i in range(years):
        total_sum = total_sum + (total_sum * percent)
    return total_sum
print(bank(1500, 3, 0.15))