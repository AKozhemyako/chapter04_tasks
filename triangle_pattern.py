# программа выводит треугольную комбинацию
BASE_SIZE = 8
for r in range(BASE_SIZE):
    for c in range(r):
        print('*', end='')
    print('#')