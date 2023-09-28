# объявление функции
from math import sqrt
def solve(a, b, c):
    d = b**2-4*a*c
    x_1 = (-b - d ** 0.5) / (2*a)
    x_2 = (-b + d ** 0.5) / (2*a)
    if d == 0:
        return x_1, x_2
    else:
        if x_1 > x_2:
            return x_2, x_1
        else:
            return x_1, x_2

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x_1, x_2 = solve(a, b, c)
print(x_1, x_2)
