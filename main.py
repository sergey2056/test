# Задание 1
# Создайте программу, хранящую информацию о вели-
# ких баскетболистах. Нужно хранить ФИО баскетболиста и
# его рост. Требуется реализовать возможность добавления,
# удаления, поиска, замены данных. Используйте словарь
# для хранения информации.

sp = {'Келвин Мерфи': '175', 'Слэйтер Мартин': '178', 'Эвери Джонсон': '178', 'Дэйна Баррос': '178', 'Майкл Адамс': '178'}

while True:
    print()
    main = int(input(f'Укажите цифрой номер меню\n 1. Добавить\n 2. Удалить\n 3. Поиск\n 4. Редактировать\n 5. Вывести список\n 0. выход\n '))
    print()
    if main == 0:
        print('Вы вышли из меню')
        break
    elif main == 1:
        a = input('Введите фамилию баскетболиста которого хотите добавить: ')
        b = input('Введите его рост: ')
        sp.update({a: b})
    elif main == 2:
        a = input('Введите фамилию баскетболиста которого хотите удалить: ')
        del sp[a]
    elif main == 3:
        a = input('Введите фамилию баскетболиста которого хотите найти: ')
        b = sp.get(a)
        if b != None:
            print(f'{a}, его рост: {b} см')
            print()
    elif main == 4:
            a = input('Введите фамилию баскетболиста которого хотите отредактировать: ')
            b = input('Введите его рост: ')
            sp[a] = b
    elif main == 5:
        for key, value in sp.items():
            print(f'{key}, его рост: {value} см')

# Задание 2
# Создайте программу «Англо-французский словарь».
# Нужно хранить слово на английском языке и его перевод
# на французский. Требуется реализовать возможность до-
# бавления, удаления, поиска, замены данных. Используйте
# словарь для хранения информации.

sp = {'морковь': 'carotte', 'капуста': 'chou', 'картофель': 'pommes de terre', 'помидор': 'tomate', 'огурец': 'concombre'}

while True:
    print()
    main = int(input(f'Укажите цифрой номер меню\n 1. Добавить\n 2. Удалить\n 3. Поиск\n 4. Редактировать\n 5. Вывести список\n 0. выход\n '))
    print()
    if main == 0:
        print('Вы вышли из меню')
        break
    elif main == 1:
        a = input('Введите слово: ')
        b = input('Введите его перевод на французский: ')
        sp.update({a: b})
    elif main == 2:
        a = input('Введите слово которое хотите удалить: ')
        del sp[a]
    elif main == 3:
        a = input('Введите слово для поиска: ')
        b = sp.get(a)
        if b != None:
            print(f'{a}, перевод на французский: {b}')
            print()
    elif main == 4:
            a = input('Введите слово для редактирования: ')
            b = input('Введите перевод на французский: ')
            sp[a] = b
    elif main == 5:
        for key, value in sp.items():
            print(f'{key}, перевод на французский: {value}')

# Задание 3
# Создайте программу «Фирма». Нужно хранить ин-
# формацию о человеке: ФИО, телефон, рабочий email,
# название должности, номер кабинета, skype. Требуется
# реализовать возможность добавления, удаления, поис-
# ка, замены данных. Используйте словарь для хранения
# информации.

def adding_new_employee(num: str = '0') -> None:
    department[num] = {}
    for key in pattern:
        department[num][key] = input(f'Введите {key}: ')

def print_data(mas):
    for key1, value1 in mas.items():
        print(f'{key1}:')
        print()
        for key2, value2 in value1.items():
            print(f'    {key2}:')
            for key3, value3 in value2.items():
                print(f'         {key3}:', end='')
                len_new = 20 - len(key3)
                for i in range(len_new):
                    print(' ', end='')
                print(f'{value3}')
            print()

def deleting_an_employee(firma_f, key):
    for key1, value1 in firma_f.items():
        for key2 in set(value1.keys()):
            if key2 in key:
                if value1.pop(key2, None) == None:
                    print('Вы ввели не верные данные либо такого работника не существует')
                else:
                    print('Данные удалены')

def employee_search(firma_f, key):
    for key1, value1 in firma_f.items():
        for key2, value2 in value1.items():
            if key2 in key:
                print_persone(value2, key2)
                return
    print('Вы ввели не верные данные либо такого работника не существует')
    return 0

def print_persone(mas, key):
    print()
    print(f'    {key}:')
    for key1, value1 in mas.items():
        print(f'         {key1}:', end='')
        len_new = 20 - len(key1)
        for i in range(len_new):
            print(' ', end='')
        print(f'{value1}')
    print()

def editing_data(firma_f, key1, key2):
    for key1f, value1f in firma_f.items():
        for key2f, value2f in value1f.items():
            if key2f in key1:
                for key3f in set(value2f.keys()):
                    if key3f in key2:
                        с = input('Введите новое значение: ')
                        value2f[key3f] = с
                        print('Данные изменены')
                        return
    print('Вы ввели не верные данные')

def save_dict_to_file(dic):
    f = open(file='firma.txt', mode='w', encoding='UTF-8')
    f.write(str(dic))
    f.close()

def load_dict_from_file():
    f = open(file='firma.txt', mode='r', encoding='UTF-8')
    data=f.read()
    f.close()
    return eval(data)

firma = {}
department = {}
pattern = {'Телефон': '', 'email': '', 'Должность': '', 'Номер кабинета': '', 'skype': ''}
count = 0

if len(load_dict_from_file()) > 0:
    firma = load_dict_from_file()

while True:
    print()
    main = int(input(f'Укажите цифрой номер меню\n 1. Добавить работника\n 2. Удалить работника\n 3. Поиск работника\n 4. Редактировать личные данные\n 5. Вывести список работников и подразделений\n 0. выход\n '))
    print()

    if main == 0:
        print('Вы вышли из меню')
        save_dict_to_file(firma)
        break

    elif main == 1:
        a = input('Введите название отдела "0" отказ от ввода: ')
        if a != '0':
            b = input('Введите ФИО работника "0" отказ от ввода: ')
            if b != '0':
                adding_new_employee(count)
                if a not in firma:
                   firma.update({a: {b: department[count]}})
                   count += 1
                else:
                   firma[a][b] = department[count]

    elif main == 2:
        a = input('Введите ФИО работника которого хотите удалить "0" отказ от ввода: ')
        if a != '0':
            deleting_an_employee(firma, a)

    elif main == 3:
        a = input('Введите ФИО работника которого хотите найти "0" отказ от ввода: ')
        if a != '0':
            employee_search(firma, a)

    elif main == 4:
        a = input('Введите ФИО работника данные которого хотите отредактировать "0" отказ от ввода: ')
        if a != '0':
            if employee_search(firma, a) != 0:
                b = input('Введите название ячейки которую хотите отредактировать "0" отказ от ввода: ')
                if b != '0':
                    editing_data(firma, a, b)

    elif main == 5:
        print_data(firma)

# Задание 4
# Создайте программу «Книжная коллекция». Нужно
# хранить информацию о книгах: автор, название книги,
# жанр, год выпуска, количество страниц, издательство.
# Требуется реализовать возможность добавления, удале-
# ния, поиска, замены данных. Используйте словарь для
# хранения информации.

#          Прошу прощения делать не стал так как не успеваю из за работы. Если принципиально скажите я сделаю мне это не сложно.
#          Задача реализуется по такому же принципу как и фирма.

