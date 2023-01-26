# Задание 1:
# Пользователь вводит с клавиатуры арифметическое
# выражение. Например, 23+12.
# Необходимо вывести на экран результат выражения.
# В нашем примере это 35. Арифметическое выражение
# может состоять только из трёх частей: число, операция,
# число. Возможные операции: +, -,*,/

while True:
   flag = 0;
   print('Введите ниже арифметическое выражение используя знаки (+, -, *, /), пример (23+12), если пожелаете выйти нажмите E')
   stroka = input('Ваше арифмитическое выражение без пробелов: ')

   if stroka == 'E' or stroka == 'e':
      print('Вы вышли из программы')
      break

   for i in range(0, len(stroka)):
      if stroka[i] == '+':
         num_1 = float(stroka[0:i])
         num_2 = float(stroka[i+1:len(stroka)])
         print(f'{num_1} + {num_2} = {num_1 + num_2}')
         flag = 1
      elif stroka[i] == '-':
         num_1 = float(stroka[0:i])
         num_2 = float(stroka[i+1:len(stroka)])
         print(f'{num_1} - {num_2} = {num_1 - num_2}')
         flag = 1
      elif stroka[i] == '*':
         num_1 = float(stroka[0:i])
         num_2 = float(stroka[i+1:len(stroka)])
         print(f'{num_1} * {num_2} = {num_1 * num_2}')
         flag = 1
      elif stroka[i] == '/':
         num_1 = float(stroka[0:i])
         num_2 = float(stroka[i+1:len(stroka)])
         print(f'{num_1} / {num_2} = {num_1 / num_2}')
         flag = 1

   if flag == 0:
      print('Вы ввели недопустимое выражение')

# Задание 2:
# В списке целых, заполненном случайными числами,
# определить минимальный и максимальный элементы,
# посчитать количество отрицательных элементов, посчи-
# тать количество положительных элементов, посчитать
# количество нулей. Результаты вывести на экран.

from random import randint

number_min = 0
number_max = 0
number_null = 0
number_negative = 0
number_positive = 0
numbers = []

for i in range(50):
    a = randint(-1000, 1000)
    numbers.append(a)

    if a > number_max:
       number_max = a

    if a < number_min:
       number_min = a

    if a < 0:
       number_negative += 1

    if a > 0:
       number_positive += 1

    if a == 0:
       number_null += 1

print("Список: ", numbers)
print('Максимальное значение числа в списке: ', number_max)
print('Минимальное значение числа в списке: ', number_min)
print('Количество отрицательных чисел в списке: ', number_negative)
print('Количество положительных чисел в списке: ', number_positive)
print('Количество чисел равных нулю в списке: ', number_null)

# ===================================================================
a = int(input('Введите колличество элементов списка: '))

spisok = []

for i in range(a):
    b = int(input('Введите элемент списка: '))
    spisok.append(b)

spisok.sort(reverse=True)
print(spisok)

while True:
    a = input('Введите число которое надо удалить из списка, для выхода нажмите e: ')

    if a == 'e':
        spisok.sort(reverse=True)
        print(spisok)
        break

    spisok.pop(spisok.index(int(a)))

# ===================================================================================
a = input('Введите строку символов и цифр: ')

count_digit = 0
count_isalpha = 0
for i in range(len(a)):

    if a[i].isdigit() == True:
        count_digit += 1

    if a[i].isalpha() == True:
        count_isalpha += 1

print(f'Количество цифр: {count_digit}, количество букв: {count_isalpha}')

# ================================================================================

a = input('Введите строку символов и цифр: ')

count_digit = 0
count_isalpha = 0
for i in a:

    if i.isdigit() == True:
        count_digit += 1

    if i.isalpha() == True:
        count_isalpha += 1

print(f'Количество цифр: {count_digit}, количество букв: {count_isalpha}')