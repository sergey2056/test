# Задание 1
# Показать на экран все простые числа в диапазоне,
# указанном пользователем. Число называется простым,
# если оно делится без остатка только на себя и на единицу.
# Например, три — это простое число, а четыре нет.

number_min = int(input('Введите нижнюю границу диапазона: '))
number_max = int(input('Введите верхнюю границу диапазона: '))
number = []
a = []
for i in range(number_min, number_max):
    d = 2
    while i % d != 0:
        d += 1
    if d == i:
        a.append(i)
print(a)

# Задание 2
# Показать на экране таблицу умножения для всех чисел
# от 1 до 10. Например:
# 1 * 1 = 1          1 * 2 = 2   …..  1 * 10  = 10
# .........................................................................
# 10 * 1 = 10    10 * 2 = 20 …. 10 * 10 = 100.

for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} * {j} = {i*j}\t\t', end='')
    print()

# Задание 3
# Показать на экран таблицу умножения в диапазоне,
# указанном пользователем. Например, если пользователь
# указал 3 и 5, таблица может выглядеть так
# 3*1 = 3    3*2 = 6       3*3 = 9       ...     3 * 10 = 30
# .....................................................................................
# 5*1 = 5    5 *2 = 10    5 *3 = 15    ...     5 * 10 = 50

number_min = int(input('Введите нижнюю границу диапазона: '))
number_max = int(input('Введите верхнюю границу диапазона : '))

for i in range(number_min, number_max + 1):
    for j in range(1, 11):
        print(f'{i} * {j} = {i*j}\t\t', end='')
    print()