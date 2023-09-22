'''
    длина логина должна быть > 4;
    длина пароля должна быть > 8;
    логин не должен быть равен паролю.
'''

login, password = input(), input()

print(len(login) > 4 and len(password) > 8 and login != password)
