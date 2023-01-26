# Задание 1
# Написать рекурсивную функцию нахождения наи-
# большего общего делителя двух целых чисел.

def communis_divisor(a, b):
    if (b == 0):
        return a
    else:
        return communis_divisor(b, a % b)
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))

print("НОД: ")
print(communis_divisor(a, b))

# Задание 2
# Написать игру «Быки и коровы». Программа «за-
# гадывает» четырёхзначное число и играющий должен
# угадать его. После ввода пользователем числа программа
# сообщает, сколько цифр числа угадано (быки) и сколько
# цифр угадано и стоит на нужном месте (коровы). После
# отгадывания числа на экран необходимо вывести коли-
# чество сделанных пользователем попыток. В программе
# необходимо использовать рекурсию.

from  random import choice
z = '0123456789'
def rand_fun(out_f:str, z_f:str, count:int):
    x = choice(z_f)
    if out_f.find(x) == -1:
        out_f += x
        count -= 1

    if count > 0:
        return rand_fun(out_f, z_f, count)

    return out_f


def tauri_et_vaccae(number, count):
    bulls = 0
    cows = 0
    b = input('введите четырехзначное число что бы цифры не повторялись: ')
    for i in range(len(number)):
        if number[i] == b[i]:
            bulls += 1
        elif b.find(number[i]) != -1:
            cows += 1
    count += 1
    if bulls == 4:
        return count
    else:
        print(f'Быков: {bulls}, Коров: {cows}')
        return tauri_et_vaccae(number, count)



a = rand_fun('', z, 4)
print(a)
print(f'Выше колличество попыток угадать число "{a}" равно: {tauri_et_vaccae(a, 0)}')

import  random
a = [random.randint(0, 100) for i in range(30)]
a.sort()

def bin_search(mas, index, l, h):
    x = (l + h) // 2
    if mas[x] == index:
        return x
    elif mas[x] > index:
        h = x + 1
        print('mas[x] > index:')
        return bin_search(mas, index, l, h)
    elif mas[x] < index:
        l = x - 1
        print('mas[x] < index:')
        return bin_search(mas, index, l, h)

print(a)
b = bin_search(a, 53, 0, len(a), 0)
print(b)
if b == -1:
    print('no elements')
else:
    print(b)
