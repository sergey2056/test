# 6.

# Дан массив целых чисел,
# отсортируйте массив в порядке
# возрастания в зависимости от
# частоты значений.
#
# Вернуть отсортированный массив.
#
# lst = [2, 1, 2, 2, 1, 3] => [3, 1, 1, 2, 2, 2]

mas = [2, 1, 2, 2, 1, 3]

def mas_function(mas_f):
    mas_out = []
    l = 0
    while l < len(mas_f):
        for i in  range(len(mas_f)):
            a = mas_f.count(mas_f[i])
            if a == (l + 1):
                mas_out.append(mas_f[i])
        l += 1
    return mas_out

print(mas_function(mas))

# 7.

# Вам дан массив nums, состоящий
# из целых положительных чисел.
#
# Вы должны взять каждое целое число
# в массиве, поменять местами его цифры
# и добавить новое число в конец массива.
#
# По итогу надо вернуть количество уникальных
# целых чисел в конечном массиве.

import  random

mas_r = [random.randint(0, 1000) for i in range(10)]

print(mas_r)

def u_turn(num):
    b = 0
    while True:
        if num // 10 >= 1:
            b = b * 10
            b += num % 10
            num = num // 10
        else:
            b = b * 10
            b += num % 10
            break
    return b
def mas_analysis(mas_f):
    l = len(mas_f)
    for i in range(l):
        mas_f.append(u_turn(mas_f[i]))
    return mas_f

print(mas_analysis(mas_r))

# 8.

# Дан массив целых чисел nums.
# Верните максимальное значение такое, что:
# (nums[i]-1)*(nums[j]-1).

import  random

mas_n = [random.randint(0, 100) for i in range(10)]
print(mas_n)
def composition(mas_f):
    a = max(mas_f)
    mas_f.remove(a)
    b = max(mas_f)
    return (a - 1) * (b - 1)

print(composition(mas_n))