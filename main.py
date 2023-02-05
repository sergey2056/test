# Задание 1
# Напишите информационную систему «Сотрудники».
# Программа должна обеспечивать ввод данных, редакти-
# рование данных сотрудника, удаление сотрудника, поиск
# сотрудника по фамилии, вывод информации обо всех
# сотрудниках, указанного возраста, или фамилия которых
# начинается на указанную букву. Организуйте возможность
# сохранения найденной информации в файл. Также весь
# список сотрудников сохраняется в файл (при выходе из
# программы — автоматически, в процессе исполнения
# программы — по команде пользователя). При старте
# программы происходит загрузка списка сотрудников из
# указанного пользователем файла.

def save_dict_to_file(dic, file_name):
    f = open(file=file_name, mode='w', encoding='UTF-8')
    f.write(str(dic))
    f.close()

def load_dict_from_file(f_f):
    f = open(f_f, 'r', encoding = 'utf-8')
    data=f.read()
    f.close()
    return eval(data)


# Добавление сотрудника
def adding_new_employee(num):
    department[num] = {}
    for key in pattern:
        department[num][key] = input(f'Введите {key}: ')

# Удаление сотрудника
def deleting_an_employee(firma_f, key):
    for value1 in firma_f.values():
        for key2 in set(value1.keys()):
            if key2.lower() in key.lower():
                if value1.pop(key2, None) == None:
                    print('Вы ввели не верные данные либо такого работника не существует')
                else:
                    print('Данные удалены')

# Поиск сотрудника
def employee_search(firma_f, key):
    status = 0
    firma_out = {}
    for key1, value1 in firma_f.items():
        for key2 , value2 in value1.items():
            if key1 not in firma_out:
                firma_out[key1] = {}
            if key.isdigit():
                for value3 in value2.values():
                    if key == value3:
                        print_persone(value2, key2)
                        status = 1
                        firma_out[key1][key2] = value2
            else:
                if key.lower() == key2.lower():
                    print_persone(value2, key2)
                    status = 1
                    firma_out[key1][key2] = value2
                else:
                    if len(key) == 1:
                        if key[0].lower() == key2[0].lower():
                            print_persone(value2, key2)
                            status = 1
                            firma_out[key1][key2] = value2
                    else:
                        sp = key2.split()
                        for i in sp:
                            if key.lower() == i.lower():
                                print_persone(value2, key2)
                                status = 1
                                firma_out[key1][key2] = value2


    spp = []
    for i in firma_out.keys():
        spp.append(i)
    for i in spp:
        if  firma_out[i] == {}:
            firma_out.pop(i)

    if status:
        return firma_out
    else:
        print('Вы ввели не верные данные либо такого работника не существует')
        return 0

# Вывод информации
def print_persone(mas, key):
    print(f'\n    {key}:')
    for key1, value1 in mas.items():
        print(f'         {key1}:', end='')
        len_new = 20 - len(key1)
        for i in range(len_new):
            print(' ', end='')
        print(f'{value1}')
    print()

# Редактирование личных данных
def editing_data(firma_f, key1, key2):
    for value1f in firma_f.values():
        for key2f, value2f in value1f.items():
            if key2f.lower() in key1.lower():
                for key3f in set(value2f.keys()):
                    if key3f.lower() in key2.lower():
                        с = input('Введите новое значение: ')
                        value2f[key3f] = с
                        print('Данные изменены')
                        return
    print('Вы ввели не верные данные')

# Вывод всех работников
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


firma = {}
count = 0
file_status = 0
department = {}
pattern = {'Возраст': '', 'Телефон': '', 'email': '', 'Должность': '', 'Номер кабинета': '', 'skype': ''}

while True:

    if file_status == 0:
        name = input('\nУкажите имя открываемого файла с расширением, "0" выйти: ')
        if name == '0':
            print('Вы вышли из программы')
        else:
            try:
                if len(load_dict_from_file(name)) > 0:
                    firma = load_dict_from_file(name)
                    file_status = 1

            except FileNotFoundError:
                print('такого файла не существует, файл будет создан автоматически при добавлении в список сотрудников')
                file_status = 1

    else:
        print()
        main = int(input(f'Укажите цифрой номер меню\n 1. Добавить работника\n 2. Удалить работника\n 3. Поиск работника по фамилии, возрасту\n 4. Редактировать личные данные\n 5. Вывести список работников\n 6. Сохранить фаил\n 7. Открыть другой фаил\n 0. выход\n '))
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
            a = input('Введите метку для поиска работника (можно отдельно фамилию или возраст) "0" отказ от ввода: ')
            if a != '0':
                mem = employee_search(firma, a)
                if mem != 0:
                    s = input('Если желаете сохранить найденную информацию в файл введите "y" ели нет "n": ')
                    if s == 'y':
                        f = input('Введите название файла с расширением: ')
                        save_dict_to_file(mem, f)
                        print(f'Данные сохранены в файл: "{f}"')

        elif main == 4:
            a = input('Введите ФИО работника данные которого хотите отредактировать "0" отказ от ввода: ')
            if a != '0':
                if employee_search(firma, a) != 0:
                    b = input('Введите название ячейки которую хотите отредактировать "0" отказ от ввода: ')
                    if b != '0':
                        editing_data(firma, a, b)

        elif main == 5:
            print_data(firma)

        elif main == 6:
            save_dict_to_file(firma, name)
            print('Данные сохранены')

        elif main == 7:
            file_status = 0