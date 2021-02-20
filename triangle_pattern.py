# программа выводит треугольную комбинацию
BASE_SIZE = 10
for r in range(BASE_SIZE):
    for c in range(r):
        if r == 7 or c == 2 or c == 7 or r ==0:
            print(' ', end='')
        else:
            print('#', end='')
    print()