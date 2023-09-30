num = int(input())

n_1, n_2 = 1, 1

for i in range(1, num + 1):
    if num == 1:
        print(1)
    else:
        print(n_1, end=' ')
        n_1, n_2 = n_2, n_1 + n_2
