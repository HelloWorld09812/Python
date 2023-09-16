from math import sqrt

a = float(input())
b = float(input())
c = float(input())

d = (b ** 2) - 4 * a * c  # Дискриминант

if d < 0:
    print('Нет корней')
elif d == 0:
    print(-b / (2 * a))
elif d > 0:
    x_1 = (-b - sqrt(d)) / (2 * a)
    x_2 = (-b + sqrt(d)) / (2 * a)
    print(min(x_1, x_2))
    print(max(x_1, x_2))
