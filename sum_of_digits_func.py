# объявление функции
def print_digit_sum(num):
    s = []
    while num != 0:
        last_digit = num % 10
        s.append(last_digit)
        num //= 10
    print(sum(s))
        
# считываем данные
num = int(input())

# вызываем функцию
print_digit_sum(num)
