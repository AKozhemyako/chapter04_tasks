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
minimal1 = minimum(a, b)
minimal2 = minimum(c, d)
minimal = minimum(minimal1, minimal2)
print( minimal, 'это самое маленькое из всех введенных чисел')

