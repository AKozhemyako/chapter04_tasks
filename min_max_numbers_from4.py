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

maximal = maximum(maximum(a, b), maximum(c, d))

count_max = 0
if maximal == a:
    count_max+=1
if maximal == b:
    count_max+=1
if maximal == c:
    count_max+=1
if maximal == d:
    count_max+=1

count_min = 0
if minimal == a:
    count_min+=1
if minimal == b:
    count_min+=1
if minimal == c:
    count_min+=1
if minimal == d:
    count_min+=1

print( minimal, 'это самое маленькое из всех введенных чисел')
print( maximal, 'это самое большое из всех введенных чисел')
print(count_max, 'повторяющихся больших чисел')
print(count_min, 'повторяющихся малых чисел')