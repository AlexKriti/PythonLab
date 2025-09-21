# Запрос данных у пользователя
password = input("Введите пароль: ")

#проверка длины
if len(password) < 16:
    print("Слишком короткий")
else:
    #проверка, содержит ли только буквы (isalpha) ИЛИ только цифры (isdigit)
    if password.isalpha() or password.isdigit():
        print("Слабый пароль")
    else:
        print("Надежный пароль")