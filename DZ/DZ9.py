# Задание 1
# Необходимо отсортировать первые две трети списка
# в порядке возрастания, если среднее арифметическое
# всех элементов больше нуля; иначе — лишь первую треть.
# Остальную часть списка не сортировать, а расположить
# в обратном порядке.

from  random import randint

spisok = [randint(0, 100) for i in range(30)]

print(spisok)
result = 0

for i in spisok:
    result = result + i

if result / len(spisok) > 0:
    sp_len = int((len(spisok) / 3) * 2)
else:
    sp_len = int(len(spisok) / 3)

spisok_out = []

for i in range(1, sp_len):
    key = spisok[i]
    j = i

    while j >= 1 and spisok[j-1] > key:
        spisok[j] = spisok[j-1]
        j -= 1

    spisok[j] = key

spisok_out = spisok[0:sp_len]

for i in spisok[:sp_len - 1:-1]:
    spisok_out.append(i)
print(spisok_out)

# Задание 2
# Написать программу «успеваемость». Пользователь
# вводит 10 оценок студента. Оценки от 1 до 12. Реализовать
# меню для пользователя:
#  ■ Вывод оценок (вывод содержимого списка);
#  ■ Пересдача экзамена (пользователь вводит номер эле-
# мента списка и новую оценку);
#  ■ Выходит ли стипендия (стипендия выходит, если
# средний бал не ниже 10.7);
#  ■ Вывод отсортированного списка оценок: по возрас-
# танию или убыванию.

list_of_ratings = []
for i in range(0, 10):
    list_of_ratings.append(int(input(f'Предмет № {i} введите оценку ученика: ')))

while True:
    print()
    main = int(input(f'Укажите цифрой номер меню\n 1. Вывод всех оценок\n 2. Пересдача экзамена\n 3. Проверить выходит ли стипендия\n 4. Вывод отсортированного списка оценок\n 0. выход\n '))
    if main == 1:
        print()
        print(list_of_ratings)
    elif main == 2:
        print(list_of_ratings)
        print()
        a = int(input('Введите номер элемента в списке которому соответствует предмет для пересдачи: '))
        b = int(input('Введите полученную оценку: '))
        list_of_ratings[a] = b
        print()
        print(list_of_ratings)
    elif main == 3:
        res = 0
        for i in list_of_ratings:
            res =  res + i
        res = res / len(list_of_ratings)
        print()
        if res >= 10.7:
            print('Студент сдал на степендию')
        else:
            print('Студент не сдал на стипендию')
    elif main == 4:
        list_of_ratings.sort()
        print()
        print(list_of_ratings)
    elif main == 0:
        print()
        print('Вы вышли из меню')
        break

# Задание 3
# Написать программу, реализующую сортировку списка
# методом усовершенствованной сортировки пузырьковым
# методом. Усовершенствование состоит в том, чтобы ана-
# лизировать количество перестановок на каждом шагу, если
# это количество равно нулю, то продолжать сортировку
# нет смысла — список отсортирован.

from random import randint
spisok_A = [randint(1, 20) for i in range(30)]
print(spisok_A)

spisok_A.sort()
print(spisok_A)

for i in range(len(spisok_A)):
    status = False
    for j in range(len(spisok_A) - 1):
        if spisok_A[j] > spisok_A[j + 1]:
            a = spisok_A[j]
            spisok_A[j] = spisok_A[j + 1]
            spisok_A[j + 1] = a
            status = True

    if status == False:
        print(f'Проходов: {i + 1}')
        print('Список отсортирован')
        break

print(spisok_A)

# Задание 1
# Написать программу «справочник». Создать два списка
# целых. Один список хранит идентификационные коды,
# второй — телефонные номера. Реализовать меню для
# пользователя:
#  ■ Отсортировать по идентификационным кодам;
#  ■ Отсортировать по номерам телефона;
#  ■ Вывести список пользователей с кодами и телефонами;
#  ■ Выход.

from random import randint
prefix = [randint(100, 999) for i in range(10)]
telephone = [randint(100000, 999999) for i in range(len(prefix))]

def sortingF(sp1, sp2):
    for i in range(1, len(sp1)):
        key1 = sp1[i]
        key2 = sp2[i]
        j = i

        while j >= 1 and sp1[j-1] > key1:
            sp1[j] = sp1[j-1]
            sp2[j] = sp2[j-1]
            j -= 1

        sp1[j] = key1
        sp2[j] = key2

    return (sp1, sp2)

def printF(sp1, sp2):
    print('Список номеров:')
    for i in range(len(sp1)):
        print(f'( {sp1[i]} ) - {sp2[i]}')
    print()

while True:
    main = int(input(f'Укажите цифрой номер меню\n 1. Отсортировать по идентификационным кодам\n 2. Отсортировать по номерам телефона\n 3. Вывод списка с кодами и телефонами\n 0. выход\n '))
    if main == 0:
        print('Вы вышли из меню')
        break
    elif main == 1:
        prefix, telephone = sortingF(prefix, telephone)
    elif main == 2:
        telephone, prefix = sortingF(telephone, prefix)
    elif main == 3:
        printF(prefix, telephone)

# Задание 2
# Написать программу «книги». Создать два списка
# с данными. Один список хранит названия книг, второй —
# годы выпуска. Реализовать меню для пользователя:
#  ■ Отсортировать по названию книг;
#  ■ Отсортировать по годам выпуска;
#  ■ Вывести список книг с названиями и годами выпуска;
#  ■ Выход;

book_titles = ['Возвращение', 'Долина ужаса', 'Яд бессмертия', 'Триумфальная арка', 'Иллюзия греха', 'Три товарища', 'Преступление и наказание', 'Ревизор', 'Гарри Поттер и узник Азкабана', 'Человек в футляре']
year_of_release = [1931, 1915, 1996, 1945, 1996, 1936, 1866, 1836, 1999, 1898]

def sortingBook(sp1, sp2):
    for i in range(1, len(sp1)):
        key1 = sp1[i]
        key2 = sp2[i]
        j = i

        while j >= 1 and sp1[j-1] > key1:
            sp1[j] = sp1[j-1]
            sp2[j] = sp2[j-1]
            j -= 1

        sp1[j] = key1
        sp2[j] = key2

    return (sp1, sp2)

def printBook(sp1, sp2):
    print('Список книг:')
    for i in range(len(sp1)):
        print(f'Книга: "{sp1[i]}", год выпуска: {sp2[i]}')
    print()

while True:
    main = int(input(f'Укажите цифрой номер меню\n 1. Отсортировать по названию книг\n 2. Отсортировать по годам выпуска\n 3. Вывести список книг с названиями и годами выпуска\n 0. выход\n '))
    if main == 0:
        print('Вы вышли из меню')
        break
    elif main == 1:
        book_titles, year_of_release = sortingBook(book_titles, year_of_release)
    elif main == 2:
        year_of_release, book_titles = sortingBook(year_of_release, book_titles)
    elif main == 3:
        printBook(book_titles, year_of_release)