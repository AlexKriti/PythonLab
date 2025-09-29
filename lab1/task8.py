# Запрос данных у пользователя
string = input("Введите вашу строку: ")
length = len(string)

#Сравним две половины строки
    # определяем, если строка имеет четное количество символов
if length%2 == 0:
    first_half = string[0:(length // 2)]
    second_half = string[(length // 2):length]

    # перевернем вторую часть строки
    second_half_rev = ''.join(reversed(second_half))

    print("Количество символов в строке четно")

    #сравниваем строки
    if first_half == second_half_rev:
        print(first_half)
        print(second_half)
        print(second_half_rev)
        print("Ваша строка - палиндром.")
    else:
        print(first_half)
        print(second_half)
        print(second_half_rev)
        print("Ваша строка - не палиндром.")
   
    # определяем, если строка имеет нечетное количество символов
else:
    first_half = string[0:(length // 2)]
    second_half = string[(length // 2 + 1):length]

    # перевернем вторую часть строки
    second_half_rev = ''.join(reversed(second_half))
    print("Количество символов в строке четно")
    
    #сравниваем строки
    if first_half == second_half_rev:
        print(first_half)
        print(second_half)
        print(second_half_rev)        
        print("Ваша строка - палиндром.")
    else:
        print(first_half)
        print(second_half)
        print(second_half_rev)
        print("Ваша строка - не палиндром.")