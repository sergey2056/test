# Задание 1
# Напишите функцию, которая отображает на экран
# форматированный текст, указанный ниже:
# “Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself.”
# Bill Gates

def text_formatting():
    print('''“Don't compare yourself with anyone in this world…
if you do so, you are insulting yourself.”
                                        Bill Gates''')

text_formatting()

# Задание 2
# Напишите функцию, которая принимает два числа
# в качестве параметра и отображает все четные числа
# между ними.

def even_numbers(x, y):
    if x > y:
        step_r = -1
    else:
        step_r = 1
    for i in range(x, y, step_r):
        if i % 2 == 0:
            print(i, end=',\t')

even_numbers(30, 3)

# Напишите функцию, которая отображает пустой или
# заполненный квадрат из некоторого символа. Функция
# принимает в качестве параметров: длину стороны ква-
# драта, символ и переменную логического типа:
#  ■ если она равна True, квадрат заполненный;
#  ■ если False, квадрат пустой.

def square(a, symbol, logic):
    for i in range(a):
        for j in range(a):
            if i == 0 or i == a - 1:
                print(symbol, end='\t')
            else:
                if logic == True:
                    print(symbol, end='\t')
                elif j == 0 or j == a-1:
                    print(symbol, end='\t')
                else:
                    print(' ', end='\t')
        print()

square(10, '#', 0)

def min_number(a, b, c, d, e):
    return min(a, b, c, d, e)

print(min_number(5, 8, 6, 4, 10))

# Задание 5
# Напишите функцию, которая возвращает произве-
# дение чисел в указанном диапазоне. Границы диапазона
# передаются в качестве параметров. Если границы диапа-
# зона перепутаны (например, 5 — верхняя граница, 25 —
# нижняя граница), их нужно поменять местами.

def composition(x, y):

    result = 1

    for i in range(min(x,y), max(x, y)):
        result *= i

    return result

print(composition(10, 3))

# Задание 6
# Напишите функцию, которая считает количество
# цифр в числе. Число передаётся в качестве параметра. Из
# функции нужно вернуть полученное количество цифр.
# Например, если передали 3456, количество цифр будет 4.

def number_of_digits(a):
    string_out = str(a)
    return len(string_out)

print(number_of_digits(12345698))

# Задание 7
# Напишите функцию, которая проверяет является ли
# число палиндромом. Число передаётся в качестве пара-
# метра. Если число палиндром нужно вернуть из функции
# true, иначе false.
# «Палиндром» — это число, у которого первая часть
# цифр равна второй перевернутой части цифр. Например,
# 123321 — палиндром (первая часть 123, вторая 321, которая
# после переворота становится 123), 546645 — палиндром,
# а 421987 — не палиндром.

def palindrome(a):
    string_out = str(a)
    result = ''

    for i in range(len(string_out)):
        result += string_out[(len(string_out)-1) - i]

    if int(result) == a:
        return True
    else:
        return False

print(palindrome(123443221))

#Вторая часть *************************
# Задание 1
# Напишите функцию, вычисляющую произведение
# элементов списка целых. Список передаётся в качестве па-
# раметра. Полученный результат возвращается из функции.

def composition_integer(sp):
    result = 1
    for i in sp:
        result *= i

    return result

from random import randint
spisok = []
spisok_b = []

for i in range(0, 20):
    spisok.append(randint(0, 10))
    spisok_b.append(randint(0, 10))

print(spisok)
print(spisok_b)

print(composition_integer(spisok))

# Задание 2
# Напишите функцию для нахождения минимума в
# списке целых. Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.

def min_integer(sp):
    result = min(sp)
    return result

print(min_integer(spisok))

# Задание 3
# Напишите функцию, определяющую количество про-
# стых чисел в списке целых. Список передаётся в качестве
# параметра. Полученный результат возвращается из функции.

def prime_number(sp):
    numbers = 0

    for i in sp:
        if i > 1:
            status = 0
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                numbers += 1

    return numbers

print(prime_number(spisok))

# Задание 4
# Напишите функцию, удаляющую из списка целых
# некоторое заданное число. Из функции нужно вернуть
# количество удаленных элементов.

def delete_f(sp, a):
    numbers = 0
    for i in range(len(sp)-1, -1, -1):
        if sp[i] == a:
            sp.pop(i)
            numbers += 1

    return numbers

print(delete_f(spisok, 5))

# Задание 5
# Напишите функцию, которая получает два списка в
# качестве параметра и возвращает список, содержащий
# элементы обоих списков.

def spicok_sum(sp1, sp2):
    return sp1 + sp2

print(spicok_sum(spisok, spisok_b))

# Задание 6
# Напишите функцию, высчитывающую степень каждого
# элемента списка целых. Значение для степени передаётся
# в качестве параметра, список тоже передаётся в качестве
# параметра. Функция возвращает новый список, содержа-
# щий полученные результаты.

def spisok_degree(sp, a):
    for i in range(len(sp)-1, -1, -1):
        sp[i] = sp[i] ** a

    return sp

print(spisok_degree(spisok, 2))


