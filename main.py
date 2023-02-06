# 3.
# Вам дана матричная сетка размера m x n,
# состоящая из положительных целых чисел.
#
# Выполняйте следующую операцию, пока сетка не станет пустой:
#
# Удалите элемент с наибольшим значением из каждой строки.
# Если существует несколько таких элементов, удалите любой из них.
# Добавьте к ответу максимальный из удаленных элементов.
# Обратите внимание, что количество столбцов уменьшается на
# один после каждой операции.
#
# Верните ответ после выполнения операций, описанных выше.
#
# Пример: [[1, 2, !4!], => [[1, !2!], => [[!1!], => [[],
#          [!3!, 3, 1]] =>  [!3!, 1]] =>  [!1!]] =>  []]
#             0 + 4   ||   4 + 3  ||  7 + 1 => Ответ: 8

a = [[1, 2, 4], [3, 3, 1]]

def matrix(mas_f):
    result = 0
    y = 0
    end = 1
    while end > 0:
        number_old = 0
        for i in range(len(mas_f)):
            number = 0

            for j in range(len(mas_f[i])):
                if mas_f[i][j] > number:
                    number = mas_f[i][j]
                    y = j

            if number != 0:
               mas_f[i].pop(y)
            if number > number_old:
                number_old = number
        end = number
        result = result + number_old

    return result

print(f'Результат равен: {matrix(a)}')

# 8.
# Вам дана целочисленная матричная сетка размера n x n.
#
# Создайте целочисленную матрицу max_local размера
# (n - 2) x (n - 2), такую, что:
#
# max_local[i][j] равно наибольшему значению матрицы
# 3 x 3 в сетке с центром вокруг строки i + 1 и столбца j + 1.
# Другими словами, мы хотим найти наибольшее значение
# в каждой непрерывной матрице 3 x 3 в сетке.
#
# Верните сгенерированную матрицу.

import  random
n = 6
matrix_r = [[random.randint(0, 60) for i in range(n)] for i in range(n)]
a = []
def print_result(matrix_f):
    for i in range(len(matrix_f)):
        print(matrix_f[i])
def matrix_1(mas_f):
    matrix_column = []
    for i in range(len(mas_f) - 2):
        matrix_line = []
        for j in range(len(mas_f[i]) - 2):
            result = 0
            # 1 проход
            for column in range(i, i + 3):
                for line in range(j, j + 3):
                    if result < mas_f[column][line]:
                        result = mas_f[column][line]
            matrix_line.append(result)
        matrix_column.append(matrix_line)
    return matrix_column

print_result(matrix_r)
print()
print_result(matrix_1(matrix_r))
