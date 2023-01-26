# Задание 1
# Пользователь вводит с клавиатуры два числа. Нужно
# посчитать отдельно сумму четных, нечетных и чисел,
# кратных 9 в указанном диапазоне, а также среднеариф-
# метическое каждой группы.

min = int(input('Введите нижнее значение диапазона: '))
max = int(input('Введите верхнее значение диапазона: '))

even_number = 0
count_even_number = 0
not_even_number = 0
count_not_even_number = 0
multiple_number = 0
count_multiple_number = 0

i = min
while i < max + 1:

    if i % 2 == 0:
        even_number += i
        count_even_number += 1
    else:
        not_even_number += i
        count_not_even_number += 1

    if i % 9 == 0:
        multiple_number += i
        count_multiple_number += 1

    i += 1

print(f'Сумма четных чисел равна: {even_number}, среднеарифмитическое равно: {even_number / count_even_number}')
print(f'Сумма не четных чисел равна: {not_even_number}, среднеарифмитическое равно: {not_even_number / count_not_even_number}')
print(f'Сумма чисел кратных 9 равна: {multiple_number}, среднеарифмитическое равно: {multiple_number / count_multiple_number}')

# Задание 2
# Пользователь вводит с клавиатуры длину линии и
# символ для заполнения линии. Нужно отобразить на
# экране вертикальную линию из введенного символа,
# указанной длины.
# Например, если было введено 5 и символ %, тогда
# вывод на экран будет такой:
# %
# %
# %
# %
# %

line = int(input('Введите длину линии: '))
symbol = input('Введите символ для построения линии: ')

i = 0
while i < line:
    print(symbol)
    i += 1

# Задание 3
# Пользователь вводит с клавиатуры числа. Если число
# больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero». Когда пользователь вводит
# число 7 программа прекращает свою работу и выводит
# на экран надпись «Good bye!»

while True:
    number = int(input('Введите число: '))
    if number == 7:
        print('«Good bye!»')
        break
    elif number > 0:
        print('«Number is positive»')
    elif number < 0:
        print('«Number is negative»')
    else:
        print('«Number is equal to zero»')

# Задание 4
# Пользователь вводит с клавиатуры числа. Програм-
# ма должна подсчитывать сумму, максимум и минимум,
# введенных чисел. Когда пользователь вводит число 7
# программа прекращает свою работу и выводит на экран
# надпись «Good bye!»

sum = 0
max = 0
min = 0
while True:
    number = int(input('Введите число: '))

    if number == 7:
        print('«Good bye!»\n')
        print(f'\nРезультаты ввода:\n\nСумма всех чисел равна: {sum}'
              f'\nМаксимальное введенное значение: {max}'
              f'\nМинимальное введенное значение: {min}')
        break
    elif number > max:
        max = number
    elif number < min:
        min = number

    sum = sum + number
