#Создайте базовый класс Shape рисования плоских фигур.
#Определите методы:
#Show() - вывод на экран информации о фигуре;
#Save() - сохранение фигуры в фаил;
#Load() - считывание фигуры из файла.

#Определите производные классы:
#Squere - квадрат, который характеризуется координатами
#левого верхнего угла и длинной стороны;
#Rectangle - прямоугольник с заданными координатами
# верхнего левого угла и размерами;
# Circle - окружность с заданными координатами центра и радиусом;
#Ellipse - эллипс с заданными координатами верхнего угла
#описанного вокруг него прямоугольника со сторонами, параллельными осям
#координат, и размерами этого прямоугольника.

#Создайте список фигур и сохраните в файл, загрузите в другой список
#и отобразите информацию о каждой фигуре

class Shape:
    def __init__(self):
        self.a = 1

    def show(self, x, y, a, b = 0, c = 0):
        print(x, y, a)

    # def save(self):
    #
    # def load(self):
s = Shape()
s.show(5, 2, 3)
# class Squere(Shape):
#     def __init__(self, x, y, a):
#         super().__init__()
#         self.coordinate_x = x
#         self.coordinate_y = y
#         self.side_length_a = a


# class Father:
#
#     def __init__(self, name, lastname):
#         self.name = name
#         self.lastname = lastname
#
#     def printname(self):
#
#         print(self.name, self.lastname)
#
# class Son(Father):
#     def __init__(self, name, lastname):
#         super().__init__(name, lastname)
#
# x = Son("Dev", "Bajaj")
# x.printname()
#
#
# x = Father("Anees", "Mulani")
# x.printname()
#
# # x = Son("Dev", "Bajaj")
# # x.printname()
