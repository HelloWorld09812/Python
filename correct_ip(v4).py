n1, n2, n3, n4 = [int(i) for i in input().split('.')]

if 255 == n1 == n2 == n3 == n4 or 0 == n1 == n2 == n3 == n4:
    print(False)
elif (0 <= n1 <= 255) and (0 <= n2 <= 255) and (0 <= n3 <= 255) and (0 <= n4 <= 255):
     print(True)
else:
     print(False)
