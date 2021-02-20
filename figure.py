#Вывод на экран геометрических фигур
print('Выводим на экран квадрат')
for i in range(10):
    for j in range(10):
        if i == 0 or j == 9 or j == 0 or i == 9:
            print('x ',end='')
        else:
            print('  ',end='')
    print()



