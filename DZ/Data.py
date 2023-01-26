# a = int(input('Введите число:'))
# a1, a = a % 10, a // 10
# a2, a = a % 10, a // 10
# a3, a = a % 10, a // 10
#
# print(a3)
# print(a2)
# print(a1)
# print(a1 + a2 + a3)

# a = int(input('Введите первую сторону треугольника: '))
# b = int(input('Введите вторую сторону треугольника: '))
# c = int(input('Введите третью сторону треугольника: '))
#
# if a == b and a == c:
#     print('Треугольник равносторонний')
# elif a == b or a == c or b == c:
#     print('Треугольник равнобедренный')
# else: print('Треугольник разносторонний')

# a = input('Введите число 1 ')
# b = input('Введите число 2 ')
#
# try:
#     c = int(a) + int(b)
# except ValueError:
#     print(f'Rresult: {a + b}')
# else:
#     print(f'Rresult: {c}')

# b = 1
# c = 1
# while True:
#     a = int(input('Введите число: '))
#     if a < 0:
#         b = b * a
#     if a > 0:
#         c = c * a
#     if a == 0:
#         print(f'Произведение положительных: {c}')
#         print(f'Произведение отрицательных: {b}')
#         break

a = int(input('Введите число: '))

i = 0
c = ''
while i < a:
    i += 1
    c += str(i)
    print(c)

i = 0
while i < 3:
    j = 0
    while j < 6:
        print('^', end='')
        j += 1
    print()
    i += 1

for i in range(3, 70, 5): #range (min, max, step)
    print(i)

names = [1, 2, 3, 4, 5, 6]
print(names)
print(names[2])
print(names[0:3])
print(names[2:3])
print(names[2:5])

a = list('123')
print(a)

for name in names:
    print(name)

def fun(a, b):
    for i in range(min(a, b), max(a, b)):
        if i % 2 != 0:
            print(i)

c = int(input('введите первое значение: '))
d = int(input('Введите второе значение: '))
fun(c, d)

def fun(a, b):
    for i in range(min(a, b), max(a, b)):
        if i % 2 != 0:
            print(i)

c = int(input('введите первое значение: '))
d = int(input('Введите второе значение: '))
fun(c, d)

def qar(n, a):
    if a == 0:
        print(1)
        return 1
    else:
        print(n * a)
        return qar(n, a - 1)

qar(2, 2)

a = ''
def function(n):
    global a
    if n > 0:
        a = a + '*'
        return function(n - 1)

function(10)

print(a)

def function(n):
    global a
    if n > 0:
        print('*', end='')
        return function(n - 1)

function(10)

# # Задание 1
# # Пользователь вводит с клавиатуры строку. Проверьте
# # является ли введенная строка палиндромом. Палин-
# # дром — слово или текст, которое читается одинаково
# # слева направо и справа налево. Например, кок; А роза
# # упала на лапу Азора; доход; А буду я у дуба.

stroka_in = input('Введите строку для проверки, является ли она полиндромом: ')
stroka = stroka_in.replace(' ', '') # удалим пробелы!
stroka = stroka.lower()
stroka_inv = stroka[::-1]

if stroka == stroka_inv:
    print(f'Введенная вами строка {stroka_in} является полиндромом')
else:
    print(f'Введенная вами строка {stroka_in} не является полиндромом')


# Задание 2
# Пользователь вводит с клавиатуры некоторый текст,
# после чего пользователь вводит список зарезервированных
# слов. Необходимо найти в тексте все зарезервированные
# слова и изменить их регистр на верхний. Вывести на
# экран измененный текст.

text_in = input('Введите текст для обработки: ')
mas_reserv = []

while True:
    a = input('Введите зарезервированное слово в тексте, для выхода введите "endend": ')
    if (a == 'endend'):
        break
    mas_reserv.append(a)

text_low = text_in.lower()

for i in mas_reserv:
    a = text_low.index(i.lower())
    b = len(i)
    c = i.upper()
    text_in = text_in[:a] + c + text_in[a+b:]

print(f'Результат равен: {text_in}')

# Задание 3
# Есть некоторый текст. Посчитайте в этом тексте ко-
# личество предложений и выведите на экран полученный
# результат.

text_in = input('Введите текст для обработки: ')
a = 1

a = text_in.count('.')

print(f'В веденном вами тексте: \n {text_in} \n\n колличество предложений равно: {a} ')

#сортировка
from random import randint
spisok = []

for i in range(0, 10):
    spisok.append(randint(0, 10))

print(spisok)
def func(sp):
    for i in range(len(sp)):
        key = sp[i]
        j = i
        while j >= 1 and sp[j - 1] > key:
            sp[j] = sp[j - 1]
            j -= 1
        sp[j] = key
    return sp

print(func(spisok))

import  random
a = [random.randint(0, 10000) for i in range(10000)]

def func(b, index_in):
    for i in range(len(b)):
        if b[i] == index_in:
            return i

print(a)
print(func(a, 2104))

# кортеж

list = ('яблоко', 'груша', 'киви', 'вишня', 'слива', 'яблоко')

a = input('Введите название: ')

print(list.count(a))

#==========================
#кортеж
mas = ('яблоко-груша', 'груша', 'киви-груша', 'вишня', 'слива-груша', 'яблоко')

a = input('Введите название: ')
count = 0
for i in mas:
    if a in i:
        count += 1

print(count)

# замена элементов кортежа
mas = ('рено', 'форд', 'киа', 'рено', 'рено', 'киа')

a = input('Введите название: ')
b = input('введите слово для замены')

for i in range(len(mas)):
    if a == mas[i]:
        mas = mas[:i] + (b,) + mas[i + 1:]

print(mas)

#множества
a = {'Абаза', 'Абакан', 'Азнакаево', 'Аксай', 'Алдан', 'Александров'}
b = {'Абаза', 'Абакан', 'Азнакаево', 'Алексеевка', 'Алзамай'}

s = a.intersection(b)

print(s)

#определить сколько одноразрядных двуразрядных и трехразрядных цифр


import  random
mas = tuple(random.randint(0, 1000) for i in range(10))
a = 0
b = 0
c = 0
print(mas)
for i in mas:
    if i // 10 <= 0:
        a += 1
    elif i // 100 <= 0:
        b += 1
    elif i // 1000 <= 0:
        c += 1

print(f'Одна цифра: {a}')
print(f'Две цифры: {b}')
print(f'Три цифры: {c}')

#Словари

sp = {} #создание словаря пустого
for i in range(1, 5):
    a = input('Введите назание продукта: ')
    sp[i] = a

print(sp)

sp.pop(int(input('Введите номер удаляемого элемента: ')))
# del sp[int(input('Введите номер удаляемого элемента: '))]

print(sp)

#работа с файлами
with open('one.txt', 'w') as one:
    for i in range(10):
        one.write('hello world\n')

with open('one.txt', 'r') as one:
    while one.readline() != '':
        a = one.readline()
        print(a)
        with open('two.txt', 'a') as two:
            two.write(a)
#00000000000000
with open(file='text.txt', mode='r') as f:
    words = f.readlines()
        words[-1] += '\n'
    with open(file='output.txt', mode='w') as out:
            out.writelines(words[::-1])

#открываем два файла переводим в списки ищем одинаковые слова формируем третий список без одинаковых сслов

dictionary = {
    'а': 'a',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'д': 'd',
    'е': 'e',
    'ё': 'e',
    'ж': 'zh',
    'з': 'z',
    'и': 'i',
    'й': 'i',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'u',
    'ф': 'f',
    'х': 'h',
    'ц': 'c',
    'ч': 'cz',
    'ш': 'sh',
    'щ': 'scz',
    'ъ': '',
    'ы': 'y',
    'ь': 'b',
    'э': 'e',
    'ю': 'u',
    'я': 'ja',
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'ZH',
    'З': 'Z',
    'И': 'I',
    'Й': 'I',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'H',
    'Ц': 'C',
    'Ч': 'CZ',
    'Ш': 'SH',
    'Щ': 'SCH',
    'Ъ': '',
    'Ы': 'y',
    'Ь': 'b',
    'Э': 'E',
    'Ю': 'U',
    'Я': 'YA',
    ',': ',',
    '?': '?',
    ' ': '_',
    '~': '~',
    '!': '!',
    '@': '@',
    '#': '#',
    '$': '$',
    '%': '%',
    '^': '^',
    '&': '&',
    '*': '*',
    '(': '(',
    ')': ')',
    '-': '-',
    '=': '=',
    '+': '+',
    ':': ':',
    ';': ';',
    '<': '<',
    '>': '>',
    '\'': '\'',
    '"': '"',
    '\\': '\\',
    '/': '/',
    '№': '#',
    '[': '[',
    ']': ']',
    '{': '{',
    '}': '}',
    'ґ': 'r',
    'ї': 'r',
    'є': 'e',
    'Ґ': 'g',
    'Ї': 'i',
    'Є': 'e',
    '—': '-',
    '.': '.',
    '«': '«',
    '»': '»'

}

with open(file='start.txt', mode='r', encoding='UTF-8') as x:
    a = x.read().split(' ')
print(a)
with open(file='ban_words.txt', mode='r', encoding='UTF-8') as y:
    b = y.read().split(' ')
print(b)
c = ''
for i in a:
    if i.lower() not in b:
        c += f'{i} '
c = c[:-1]
print(c)
with open(file='output.txt', mode='w', encoding='UTF-8') as out:
    out.write(c)

#=========================
c = ''
while True:
    a = input('Введите название файла с расширением, для выхода введите quit: ')
    if a == 'quit':
        break
    with open(file=a, mode='r', encoding='UTF-8') as x:
        f = x.read()
    c += f

with open(file='output.txt', mode='w', encoding='UTF-8') as out:
    out.write(c)