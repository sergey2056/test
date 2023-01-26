# Задание 1
# Пользователь вводит с клавиатуры число в диапа-
# зоне от 1 до 100. Если число кратно 3 (делится на 3 без
# остатка) нужно вывести слово Fizz. Если число кратно 5
# нужно вывести слово Buzz. Если число кратно 3 и 5 нужно
# вывести Fizz Buzz. Если число не кратно не 3 и 5 нужно
# вывести само число.
# Если пользователь ввел значение не в диапазоне от 1
# до 100 требуется вывести сообщение об ошибке.

a = int(input('Введите число в диапазоне 1-100: '))

if a < 1 or a > 100:
  print('Ошибка ввода.')
elif a % 3 == 0 and a % 5 == 0:
  print('Fizz Buzz')
elif a % 5 == 0:
  print('Buzz')
elif a % 3 == 0:
  print('Fizz')
else:
  print(a)

# Задание 2
# Написать программу, которая по выбору пользова-
# теля возводит введенное им число в степень от нулевой
# до седьмой включительно.

# #Вариант 1
a = int(input('Введите число: '))
degree = int(input('Введите степень от 0 до 7 включительно: '))

if a >= 0 and a <= 7:
  print(a**degree)
else:
  print('Ошибка ввода данных')

# #Вариант 2
a = int(input('Введите число: '))

if a >= 0 and a <= 7:
  i = 0
  while i < 8:
    print(f'{a}^{i}={a**i}')
    i += 1

# Задание 3
# Написать программу подсчета стоимости разговора
# для разных мобильных операторов. Пользователь вводит
# стоимость разговора и выбирает с какого на какой опе-
# ратор он звонит. Вывести стоимость на экран.

# стоимость звонков с билайна на другие операторы 1,25 условно
# стоимость звонков с мегафона на другие операторы 1,5 условно
# стоимость звонков с мтс на другие операторы 1,3 условно

beeline = 1.25
megafon = 1.5
mts = 1.3

a = int(input('Введите число проговоренных минут: '))
b =  int(input('Введите номер оператора beeline - 1; megafon - 2; mts - 3: '))

if b == 1:
  print(f'Стоимость звонка с beeline составит: {a * beeline}')
elif b == 2:
  print(f'Стоимость звонка с megafon составит: {a * megafon}')
elif b == 3:
  print(f'Стоимость звонка с mts составит: {a * mts}')
else:
  print('Оператора с такин номером нет в списке')

# Задание 4
# Зарплата менеджера составляет 200$ + процент от про-
# даж, продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше
# 1000 — 8%. Пользователь вводит с клавиатуры уровень
# продаж для трех менеджеров. Определить их зарплату,
# определить лучшего менеджера, начислить ему премию
# 200$, вывести итоги на экран.

manager_1 = int(input('Введите уровень продаж первого менеджера: '))
manager_2 = int(input('Введите уровень продаж второго менеджера: '))
manager_3 = int(input('Введите уровень продаж третьего менеджера: '))

salary_1 = salary_2 = salary_3 = 200

if manager_1 < 500:
  salary_1 = salary_1 + manager_1 / 100 * 3
elif manager_1 > 1000:
  salary_1 = salary_1 + manager_1 / 100 * 8
else:
  salary_1 = salary_1 + manager_1 / 100 * 5

if manager_2 < 500:
  salary_2 = salary_2 + manager_2 / 100 * 3
elif manager_2 > 1000:
  salary_2 = salary_2 + manager_2 / 100 * 8
else:
  salary_2 = salary_2 + manager_2 / 100 * 5

if manager_3 < 500:
  salary_3 = salary_3 + manager_3 / 100 * 3
elif manager_3 > 1000:
  salary_3 = salary_3 + manager_3 / 100 * 8
else:
  salary_3 = salary_3 + manager_3 / 100 * 5

#Рейтинг менеджеров
if salary_1 > salary_2 and salary_1 > salary_3:
  salary_1 = salary_1 + 200
  print(f'manager_1: {salary_1}')
  if salary_2 > salary_3:
    print(f'manager_2: {salary_2}')
    print(f'manager_3: {salary_3}')
  else:
    print(f'manager_3: {salary_3}')
    print(f'manager_2: {salary_2}')
elif salary_2 > salary_3:
  salary_2 = salary_2 + 200
  print(f'manager_2: {salary_2}')
  if salary_1 > salary_3:
    print(f'manager_1: {salary_1}')
    print(f'manager_3: {salary_3}')
  else:
    print(f'manager_3: {salary_3}')
    print(f'manager_1: {salary_1}')
else:
  salary_3 = salary_3 + 200
  print(f'manager_3: {salary_3}')
  if salary_1 > salary_2:
    print(f'manager_1: {salary_1}')
    print(f'manager_2: {salary_2}')
  else:
    print(f'manager_2: {salary_2}')
    print(f'manager_1: {salary_1}')

