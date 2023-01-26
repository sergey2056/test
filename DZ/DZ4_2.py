number = ''

while True:
    number = input('Введите номер картинки из диапазона (а - к), указав номер картинки буквой, если пожелаете выйти из программы нажмите 0: ')

    if number == '0':
        print('Вы вышли из программы')
        break

    for i in range(0, 10):
        b = ''

        if number == 'а':
            for j in range(0, 10):
                if j >= i:
                    b += '* '
                else:
                    b += '  '

        if number == 'б':
            for j in range(0, 11):
                if j > i:
                    b += '  '
                else:
                    b += '* '

        if number == 'в':
            if i < 5:
                for j in range(0, 10):
                    if j < i or j > 9 - i:
                        b += '  '
                    else:
                        b += '* '

        if number == 'г':
            if i > 4:
                for j in range(0, 10):
                    if j > i or j < 9 - i:
                        b += '  '
                    else:
                        b += '* '

        if number == 'д':
            for j in range(0, 10):
                if i < 5:
                    if j < i or j > 9 - i:
                        b += '  '
                    else:
                        b += '* '
                else:
                    if j > i or j < 9 - i:
                        b += '  '
                    else:
                        b += '* '

        if number == 'е':
            for j in range(0, 10):
                if i < 5:
                    if j > i and j < (9 - i):
                        b += '  '
                    else:
                        b += '* '
                if i > 4:
                    if j < i and j > (9 - i):
                        b += '  '
                    else:
                        b += '* '

        if number == 'ж':
            for j in range(0, 5):
                if i < 5:
                    if j > i:
                        b += '  '
                    else:
                        b += '* '
                else:
                    if j < 10 - i:
                        b += '* '
                    else:
                        b += '  '

        if number == 'з':
            for j in range(0, 10):
                if i < 5:
                    if j > 8 - i:
                        b += '* '
                    else:
                        b += '  '
                else:
                    if j >= i :
                        b += '* '
                    else:
                        b += '  '
        if number == 'и':
            for j in range(0, 10):
                if j < 10 - i:
                    b += '* '
                else:
                    b += '  '

        if number == 'к':
            for j in range(0, 10):
                if j < 9 - i:
                    b += '  '
                else:
                    b += '* '

        print(b)

