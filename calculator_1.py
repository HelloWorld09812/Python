n_1 = int(input())
n_2 = int(input())

action = input()

if action == '+':
    print(n_1 + n_2)
elif action == '-':
    print(n_1 - n_2)
elif action == '*':
    print(n_1 * n_2)
elif action == '/' and n_2 == 0:
    print('На ноль делить нельзя!')
elif action == '/':
    print(n_1 / n_2)
else:
    print('Неверная операция')
