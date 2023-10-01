from math import sqrt


x_1, y_1, x_2, y_2 = float(input()), float(input()), float(input()), float(input())

p = sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)

print(p)
