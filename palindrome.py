# объявление функции
def is_palindrome(text):
    l = []
    for i in range(len(text)):
        if text[i].isalpha():
            l.append(text[i].lower())
    if l == l[::-1]:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
