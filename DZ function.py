# Простейший калькулятор с введеными двумя числами вещественного типа.
# Ввод с клавиатуры: + - * / и два числа. Операции являются функциями.
# Обработать ошибку: "Деление на ноль"
# Ноль использовать в качестве завершения программы (сделать, как отдельную операцию).
print('Добро пожаловать в Калькулятор!'
      '\nДля начала')


def s(a, b):
    return a + b


def r(a, b):
    return a - b


def m(a, b):
    return a * b


def d(a, b):

    try:
        return a / b
    except ZeroDivisionError:
        print('Делить на ноль нельзя')


while True:
    sign = input('Введите Знак(+, -, *, /, 0 - выход): ')

    if sign == '0':
        break
    elif sign in ('+', '-', '*', '/'):
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))

    else:
        print('Введён неправильный знак')

    if sign == '+':
        print(f'{a} + {b} = {s(a, b)}')
    elif sign == '-':
        print(f'{a} - {b} = {r(a, b)}')
    elif sign == '*':
        print(f'{a} * {b} = {m(a, b)}')
    elif sign == '/':
        print(f'{a} / {b} = {d(a, b)}')




