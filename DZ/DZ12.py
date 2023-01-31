

# Задание 1
# Дано два текстовых файла. Выяснить, совпадают ли
# их строки. Если нет, то вывести несовпадающую строку
# из каждого файла.

with open('one.txt', 'r', encoding = 'utf-8') as f1, open('two.txt', 'r', encoding = 'utf-8') as f2:
    for a1, a2 in zip(f1, f2):
        if a1 != a2:
            # a3 = a1.split('\n')[0]
            # a4 = a2.split('\n')[0]
            a3 = a1.strip('\n')
            a4 = a2.strip('\n')
            print(f'Строки не совпадают: {a3} и {a4}')

# Задание 2
# Дан текстовый файл. Необходимо создать новый файл
# и записать в него следующую статистику по исходному
# файлу:
#  ■ Количество символов;
#  ■ Количество строк;
#  ■ Количество гласных букв;
#  ■ Количество согласных букв;
#  ■ Количество цифр.

lines = 0
digit = 0
symbols = 0
vowels = 0
consonants = 0
vowels_mas = set('аоуыэяеёюи')
consonants_mas = set('бвгдйжзклмнпрстфхцчшщ')

file = open('one.txt', 'r', encoding = 'utf-8')

for line in file:
    lines += 1
    symbols += len(line.strip('\n'))
    for i in line:
        if i.isdigit() == True:
            digit += 1
        elif i in vowels_mas:
            vowels += 1
        elif i in consonants_mas:
            consonants += 1

file.close()
with open(file='output.txt', mode='w', encoding='UTF-8') as out:
    out.write(f'В файле символов: {symbols}, количество строк: {lines}, количество гласных букв: {vowels}, количество согласных букв: {consonants}, количество цифр: {digit}')


# Задание 3
# Дан текстовый файл. Удалить из него последнюю
# строку. Результат записать в другой файл.

with open('one.txt', 'r', encoding = 'utf-8') as f:
    lines = f.readlines()
    lines = lines[:-1]

with open(file='output.txt', mode='w', encoding='UTF-8') as out:
    out.writelines(lines)

# Задание 4
# Дан текстовый файл. Найти длину самой длинной
# строки.

str_len = 0
count = 0
l = 0
file = open('one.txt', 'r', encoding = 'utf-8')

for line in file:
    count += 1
    if len(line) > str_len:
        str_len = len(line)
        l = count
file.close()

print(f'В файле самая длинная строка под номером {l}, ее длинна: {str_len}')

# Задание 5
# Дан текстовый файл. Посчитать сколько раз в нем
# встречается заданное пользователем слово.

a = input('Введите слово для поиска: ')

count = 0

file = open('one.txt', 'r', encoding = 'utf-8')

for line in file:
    if a in line:
        count += 1

file.close()
print(f'В файле встречается слово: {a}, {count} раз')

# Задание 6
# Дан текстовый файл. Найти и заменить в нем задан-
# ное слово. Что искать и на что заменять определяется
# пользователем.

a = input('Введите слово которое нужно заменить: ')
b = input('Введите слово на которое нужно заменить: ')

with open('one.txt', 'r', encoding = 'utf-8') as f:
    lines = f.read()

text = lines.replace(a, b)

with open(file='output.txt', mode='w', encoding='UTF-8') as out:
    out.writelines(text)
