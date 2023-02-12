a = int(input('Введите число:'))
a1, a = a % 10, a // 10
a2, a = a % 10, a // 10
a3, a = a % 10, a // 10

print(a3)
print(a2)
print(a1)
print(a1 + a2 + a3)

a = int(input('Введите первую сторону треугольника: '))
b = int(input('Введите вторую сторону треугольника: '))
c = int(input('Введите третью сторону треугольника: '))

if a == b and a == c:
    print('Треугольник равносторонний')
elif a == b or a == c or b == c:
    print('Треугольник равнобедренный')
else: print('Треугольник разносторонний')

a = input('Введите число 1 ')
b = input('Введите число 2 ')

try:
    c = int(a) + int(b)
except ValueError:
    print(f'Rresult: {a + b}')
else:
    print(f'Rresult: {c}')

b = 1
c = 1
while True:
    a = int(input('Введите число: '))
    if a < 0:
        b = b * a
    if a > 0:
        c = c * a
    if a == 0:
        print(f'Произведение положительных: {c}')
        print(f'Произведение отрицательных: {b}')
        break

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

#=============================================
from random import randint
mas = [randint(0, 30) for i in range(10)]
print(mas)

def nums(mas_f):
    count = 0
    for i in range(len(mas_f)):
        for j in range(i + 1, len(mas_f)):
            if mas_f[i] == mas_f[j] and i < j:
                count += 1
    return count

print(nums(mas))

#============================

from random import randint
mas = [randint(0, 30) for i in range(10)]
print(mas)

def nums(mas_f):
    sp = []
    for i in range(len(mas_f)):
        count = 0
        for j in range(len(mas_f)):
            if mas_f[i] > mas_f[j]:
                count += 1
        sp.append(count)
    return sp

print(nums(mas))

#===========================================

from random import randint

matrix = []
m, n = 3, 3

for i in range(m):
    matrix.append([])
    for j in range(n):
        matrix[i].append(randint(1, 10))

print(matrix)
def nums(mas_f):
    sp = []
    str = len(mas_f[0])
    stb = len(mas_f)
    for i in range(str) :
        a = min(mas_f[i])
        b = 0
        for j in range(stb):
            if b < mas_f[j][i]:
                b = mas_f[j][i]
        if b == a:
            sp.append(b)
    return sp

print(nums(matrix))

#=====================================================
mas = ['cjajcaj5', 'ada', '3', '7', '000', 'kjdjs']
print(mas)
def mas_f(mas_fun):
    result = 0
    for i in mas_fun:
        if i.isdigit():
           if result < int(i):
               result = int(i)
        elif result < len(i):
            result = len(i)
    return result

print(mas_f(mas))

#=========================================================
class Fraction:
    def __init__(self, numerator: int = 0, denominator: int = 1):
        self.numerator = numerator
        self.denominator = denominator

    def reset(self):
        self.numerator = int(input('Введите новый числитель: '))
        self.denominator = int(input('Введите новый знаменатель: '))

    def sum(self, another: 'Fraction'):
        shared_denom = self.denominator * another.denominator
        shared_num = self.numerator * another.denominator + \
                     another.numerator * self.denominator
        i = 1
        while i < min(shared_num, shared_denom):
            if shared_num % i == 0 and shared_denom % i == 0:
                shared_num //= i
                shared_denom //= i
                i = 1
            i += 1
        return Fraction(shared_num, shared_denom)

a = Fraction(3, 4)
b = Fraction(7, 8)
print(b)
c = a.sum(b)
print(c.numerator, c.denominator)

class Human:
    __counter = 0
    def __init__(self, full_name: str, age: int, number: int, city: str, country: str, adress: str):
        self.full_name = full_name
        self.age = age
        self.number = number
        self.city = city
        self.country = country
        self.adress = adress
        Human.__counter += 1
    def show_info(self):
            print(f'\nФИО: {self.full_name},\n'
                  f'Возраст: {self.age},\n'
                  f'Телефон: {self.number},\n'
                  f'Город: {self.city},\n'
                  f'Страна: {self.country},\n'
                  f'Адрес: {self.adress}\n')
    def change_info(self):
            self.full_name = input('Введите ваше ФИО: ')
            self.age = int(input('Введите ваш возраст: '))
            self.number = int(input('Введите ваш номер телефона: '))
            self.city = input('Введите ваш город: ')
            self.country = input('В какой стране вы проживаете: ')
            self.adress = input('Назовите ваш адрес: ')

    @staticmethod
    def get_counter():
        return Human.__counter

p = Human('Фио', 35, +77777777777,'Москва','Россия','Street')
p.show_info()
print(Human.get_counter())

class square:
    __count = 0
    @staticmethod
    def get_square_area(a):
        b = a * a
        square.__count += 1
        return b
    @staticmethod
    def get_square_rectangle(a, b):
        c = a * b
        square.__count += 1
        return c
    @staticmethod
    def get_count():
        return square.__count
    @staticmethod
    def get_square_rhomb(a, h):
        s = a * h
        return s

print(square.get_square_area(5))
print(square.get_square_rectangle(5, 2))
print(square.get_square_rhomb(5, 10))
print(square.get_count())

class number:
    __count = 0
    @staticmethod
    def get_max(a, b, c, d):
        s = max(a, b, c, d)
        return s
    @staticmethod
    def get_min(a, b, c, d):
        s = min(a, b, c, d)
        return s
    @staticmethod
    def get_arithmetic_mean(a, b, c, d):
        s = (a + b + c + d) / 4
        return s
    @staticmethod
    def get_factorial(a, b, c, d):
        s = a * b * c * d
        return s


print(number.get_max(1, 2, 3, 4))
print(number.get_min(1, 2, 3, 4))
print(number.get_arithmetic_mean(1, 2, 3, 4))
print(number.get_factorial(1, 2, 3, 4))