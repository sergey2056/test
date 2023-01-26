# Задание 1
# Есть четыре списка целых. Необходимо их объединить
# в пятом списке. Полученный результат в зависимости от
# выбора пользователя отсортировать по убыванию или
# возрастанию. Найти значение, введенное пользователем,
# с использованием линейного поиска.

import  random
sp1 = [random.randint(0, 100) for i in range(3)]
sp2 = [random.randint(0, 100) for i in range(3)]
sp3 = [random.randint(0, 100) for i in range(3)]
sp4 = [random.randint(0, 100) for i in range(3)]

# print(f'Список_1: {sp1}')
# print(f'Список_2: {sp2}')
# print(f'Список_3: {sp3}')
# print(f'Список_4: {sp4}')


sp5 = sp1 + sp2 + sp3 + sp4

print(f'Список_5: {sp5}')
print()

def linear_Search(spf, key):
    for i in range(0, len(spf)):
        if (spf[i] == key):
            return i
    return -1

while True:
    main = int(input(f'Укажите цифрой номер меню\n 1. Отсортировать по возрастанию\n 2. Отсортировать по убыванию\n 3. Поиск значения введенного пользователеь\n 0. выход\n '))
    if main == 0:
        print('Вы вышли из меню')
        break
    elif main == 1:
        sp5 = sorted(sp5, reverse = False)
        print(sp5)
        print()
    elif main == 2:
        sp5 = sorted(sp5, reverse = True)
        print(sp5)
        print()
    elif main == 3:
        a = int(input('Введите число для поиска: '))
        result = linear_Search(sp5, a)
        if result == -1:
            print(f'Введенный вами элемент не найден')
        else:
            print(f'Индекс введенного вами элемента: {result}')
            print()

# Задание 2
# Есть четыре списка целых. Необходимо объединить
# в пятом списке только те элементы, которые уникальны
# для каждого списка. Полученный результат в зависимости
# от выбора пользователя отсортировать по убыванию или
# возрастанию. Найти значение, введенное пользователем,
# с использованием бинарного поиска.

sp5 = []


sp5 = (set(sp1) ^ set(sp2) ^ set(sp3) ^ set(sp4))

print(sp5)
print()

def bin_search(mas, index, l, h):
    x = (l + h) // 2
    if mas[x] == index:
        return x
    elif mas[x] > index and l != h:
        h = x - 1
        return bin_search(mas, index, l, h)
    elif l != h:
        l = x + 1
        return bin_search(mas, index, l, h)
    else:
        return -1

sort_status = 0

while True:
    main = int(input(f'Укажите цифрой номер меню\n 1. Отсортировать по возрастанию\n 2. Отсортировать по убыванию\n 3. Поиск значения введенного пользователеь\n 0. выход\n '))
    if main == 0:
        print('Вы вышли из меню')
        break
    elif main == 1:
        sp5 = sorted(sp5, reverse = False)
        sort_status = 1
        print(sp5)
        print()
    elif main == 2:
        sp5 = sorted(sp5, reverse = True)
        sort_status = -1
        print(sp5)
        print()
    elif main == 3:
        a = int(input('Введите число для поиска: '))
        if sort_status == 0:
            sp5 = sorted(sp5)
            sort_status = 1
        if sort_status == 1:
            result = bin_search(sp5, a, 0, len(sp5) - 1)
        if sort_status == -1:
            result = bin_search(sp5, a, len(sp5) - 1, 0)
        if result == -1:
            print(f'Введенный вами элемент не найден')
        else:
            print(f'Индекс введенного вами элемента: {result}')
            print()

# Задание 1
# Есть три кортежа целых чисел необходимо найти
# элементы, которые есть во всех кортежах.

import  random
mas_1 = tuple(random.randint(0, 10) for i in range(10))
mas_2 = tuple(random.randint(0, 10) for i in range(10))
mas_3 = tuple(random.randint(0, 10) for i in range(10))

print(mas_1)
print(mas_2)
print(mas_3)

print()

mas_out = tuple(set(mas_1) & set(mas_2) & set(mas_3))

print(f'Элементы которые есть во всех кортежах: {mas_out}')

# Задание 2
# Есть три кортежа целых чисел необходимо найти
# элементы, которые уникальны для каждого списка.

def get_uniq(tuple_1, tuple_2, tuple_3):
    s_1 = set()
    s_2 = set()
    s_3 = set()
    for number in tuple_1:
        if (number not in tuple_2) and (number not in tuple_3):
            s_1.add(number)
    for number in tuple_2:
        if (number not in tuple_1) and (number not in tuple_3):
            s_2.add(number)
    for number in tuple_3:
        if (number not in tuple_2) and (number not in tuple_1):
            s_3.add(number)

    return s_1, s_2, s_3

out_1, out_2, out_3 = get_uniq(mas_1, mas_2, mas_3)

if len(out_1) > 0:
    print(f'Уникальные элементы первого кортежа: {out_1}')
if len(out_2) > 0:
    print(f'Уникальные элементы второго кортежа: {out_2}')
if len(out_3) > 0:
    print(f'Уникальные элементы третьего кортежа: {out_3}')

# Задание 3
# Есть три кортежа целых чисел необходимо найти эле-
# менты, которые есть в каждом из кортежей и находятся
# в каждом из кортежей на той же позиции.

import  random
mas_11 = tuple(random.randint(0, 3) for i in range(30))
mas_21 = tuple(random.randint(0, 3) for i in range(30))
mas_31 = tuple(random.randint(0, 3) for i in range(30))

print(mas_11)
print(mas_21)
print(mas_31)

for i, j, g in zip(mas_11, mas_21, mas_31):   # zip() функция которая создает итератор, который объединяет элементы из нескольких источников данных.
    if i == j == g:
        print(i, end=', ')

