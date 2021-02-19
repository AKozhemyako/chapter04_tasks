# программа выводит треугольную комбинацию
BASE_SIZE = 1
for r in range(BASE_SIZE):
    for c in range(r + 8):
        print('*', end='')
    print('#')