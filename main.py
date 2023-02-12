# Задание 1
# К уже реализованному классу «Дробь» добавьте ста-
# тический метод, который при вызове возвращает коли-
# чество созданных объектов класса «Дробь».

class Fraction:
    __counter = 0
    def __init__(self, numerator: int = 0, denominator: int = 1):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.__counter += 1

    def reset(self):
        self.numerator = int(input('Введите новый числитель: '))
        self.denominator = int(input('Введите новый знаменатель: '))

    def sum(self, another: 'Fraction'):
        shared_denom = self.denominator * another.denominator
        shared_num = self.numerator * another.denominator + \
                     another.numerator * self.denominator
        i = 1
        while i < min(shared_num, shared_denom):
            if shared_num % i == 0 and shared_denom % i == 0:
                shared_num //= i
                shared_denom //= i
                i = 1
            i += 1
        return Fraction(shared_num, shared_denom)

    @staticmethod
    def get_counter():
        return Fraction.__counter


a = Fraction(3, 4)
b = Fraction(7, 8)
print(b)
c = a.sum(b)
print(c.numerator, c.denominator)
print(Fraction.get_counter())

# Задание 2
# Создайте класс для конвертирования температуры из
# Цельсия в Фаренгейт и наоборот. У класса должно быть
# два статических метода: для перевода из Цельсия в Фа-
# ренгейт и для перевода из Фаренгейта в Цельсий. Также
# класс должен считать количество подсчетов температуры и
# возвращать это значение с помощью статического метода.

class temperatureСonverter:
    __counter = 0

    @staticmethod
    def get_fahrenheit(number: int):
        result = number * 1.8 + 32
        temperatureСonverter.__counter += 1
        return result

    @staticmethod
    def get_celsius(number: int):
        result = (number - 32) * 0.5555555555555556
        temperatureСonverter.__counter += 1
        return result

    @staticmethod
    def get_counter():
        return temperatureСonverter.__counter

a = temperatureСonverter.get_fahrenheit(10)
print(a)
b = temperatureСonverter.get_celsius(a)
print(b)
print(temperatureСonverter.get_counter())

# Задание 3
# Создайте класс для перевода из метрической системы
# в английскую и наоборот. Функциональность необходимо
# реализовать в виде статических методов. Обязательно
# реализуйте перевод мер длины.

class converter:

    @staticmethod
    def get_inch():
        number = int(input('Введите значение для перевода в дюймы: '))
        data_type = input('Укажите меру длинны mm, sm, m: ')
        if data_type == 'mm':
            return number / 25.4
        elif data_type == 'sm':
            return number / 2.54
        elif data_type == 'm':
            return number / 0.254


    @staticmethod
    def get_foot():
        number = int(input('Введите значение для перевода в футы: '))
        data_type = input('Укажите меру длинны mm, sm, m: ')
        if data_type == 'mm':
            return number / 304.8
        elif data_type == 'sm':
            return number / 30.48
        elif data_type == 'm':
            return number / 3.048

    @staticmethod
    def get_yard():
        number = int(input('Введите значение для перевода в ярды: '))
        data_type = input('Укажите меру длинны mm, sm, m: ')
        if data_type == 'mm':
            return number / 914.4
        elif data_type == 'sm':
            return number / 91.44
        elif data_type == 'm':
            return number / 9.144

    @staticmethod
    def get_mm():
        number = int(input('Введите значение для перевода в миллиметры: '))
        data_type = input('Укажите меру длинны i - inch, f - foot, y - yard: ')
        if data_type == 'i':
            return number * 25.4
        elif data_type == 'f':
            return number * 304.8
        elif data_type == 'y':
            return number * 914.4

    @staticmethod
    def get_sm():
        number = int(input('Введите значение для перевода в сантиметры: '))
        data_type = input('Укажите меру длинны i - inch, f - foot, y - yard: ')
        if data_type == 'i':
            return number * 2.54
        elif data_type == 'f':
            return number * 30.48
        elif data_type == 'y':
            return number * 91.44

    @staticmethod
    def get_m():
        number = int(input('Введите значение для перевода в метры: '))
        data_type = input('Укажите меру длинны i - inch, f - foot, y - yard: ')
        if data_type == 'i':
            return number * 0.254
        elif data_type == 'f':
            return number * 3.048
        elif data_type == 'y':
            return number * 9.144

print(converter.get_inch())
print(converter.get_mm())