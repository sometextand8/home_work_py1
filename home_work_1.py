# 1. Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки
# и сохраните в переменные, затем выведите на экран.

# some_num = 8
# some_text = 'Hello'
#
# print(some_num, some_text, sep='\n')
# print()
# input_from_user_text = input('Enter some text: ')
# input_from_user_number = int(input('Enter some number: '))
# print()
# print(f'your text - {input_from_user_text}\nyour number - {input_from_user_number}')


# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды
# и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


# input_sec = int(input('Enter time in seconds: '))
#
# hours = input_sec // 3600
# minuts = (input_sec - hours * 3600) // 60
# seconds = (input_sec - hours * 3600) % 60
#
#
#
# print('{} - seconds equals\n{}hh:{}mm:{}ss.'.format(input_sec, hours, minuts, seconds))


# template = 'Дорогой {}! Поздравляю Вас с праздником {}!'
# name = 'Dima'
# party = '9 May'
#
# print(template.format(name,party))
# print()
#
# age = 5
#
# print(f'{age:03d}')
#
# price = 67.823414323
# print(round(price, 2))
#
# print(int(price))
#
# print(round(price))
#
# print(f'{price:.1f}')


# 3. Узнайте у пользователя число n. Найдите сумму чисел
# n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

# input_user = input('enter number n: ')
#
# first = int(input_user)
# second = int(input_user * 2)
# third = int(input_user * 3)
# print(first + second + third)
#


# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте
# цикл while и арифметические операции.

# input_num = int(input('enter number: '))
# look = 0
# while input_num > 0:
#
#     max_number = input_num % 10
#     input_num = input_num // 10
#     if max_number > look:
#         look = max_number
#
# print(look)


# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
# финансовым результатом работает фирма. Например, прибыль — выручка больше издержек,
# или убыток — издержки больше выручки. Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение
# прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль
# фирмы в расчёте на одного сотрудника.

#
# revenue = int(input('Введите прибыль фирмы: '))
# costs = int(input('Введите убыток фирмы: '))
#
# if revenue > costs:
#     rentab = revenue / costs
#     if rentab > 0:
#         number_of_costumer = int(input('enter number of coustomer: '))
#         result = revenue / number_of_costumer
#         print(f'Прибыль на сотпудника - {result}')
#     print('Прибыль у фирмы')
# else:
#     print('Убытки у фирмы')


# num_a = int(input('enter num a: '))
# num_b = int(input('enter num b: '))
# count_day = 1
# while num_a < num_b:
#     num_a *= 1.1
#     count_day += 1
# print(f'на {count_day} спортсмен достин результата не менее - {num_b}км. ')
