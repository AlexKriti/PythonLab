# Запрос данных у пользователя
string = input("Введите вашу строку: ")
length = len(string)

if string == string[::-1]:
    print("Ваша строка - палиндром.")
else:
    print("Ваша строка - не палиндром.")