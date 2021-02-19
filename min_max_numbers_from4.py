# ДЗ на определение и вывод наименьшего числа
print('Введите любые четыре числа, будем вычислять самое малое из них')
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
d = int(input('Введите четвертое число: '))

def minimum (x, y):
    if x < y:
        return x
    else:
        return y

def maximum(x, y):
    if x > y:
        return x
    else:
        return y

minimal = minimum(minimum(a, b), minimum(c, d))
print( minimal, 'это самое маленькое из всех введенных чисел')

maximal = maximum(maximum(a, b), maximum(c, d))
print( maximal, 'это самое большое из всех введенных чисел')