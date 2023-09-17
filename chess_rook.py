# Игровое поле 8 на 8
# Шахматная ладья ходит по горизонтали или вертикали
n_1 = int(input()) # Номер столбца 1 (изначальные координаты)
n_2 = int(input()) # Номер строки 1 (изначальные координаты)
n_3 = int(input()) # Номер столбца 2 (координаты после совершения хода)
n_4 = int(input()) # Номер строки 2 (координаты после совершения хода)
# Что значит ходит по горизонтали? Это значит, что при ходе меняется номер столбца 1, то номер строки поменяться не должен, кроме случая, когда столбец 1 совпадает со столбцом 2.
# Что значит ходит по вертикали? Это значит, что при ходе меняется номер строки, а номер столбца остается, кроме случая, когда строка 1 совпадает со строкой 2.
# n_1 == n_3 and n_2 != n_4 - Вертикальный ход (поменялись только строки)
# n_2 == n_4 and n_1 != n_3 - Ход по горизонтали (поменялись только столбцы)
# Далее объединяем условия:
if n_1 == n_3 and n_2 != n_4 or n_2 == n_4 and n_1 != n_3:
    print('YES')
else:
    print('NO')
