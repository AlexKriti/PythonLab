# Запрос данных у пользователя
IP = input("Введите ваше IP в формате ХХХ.ХХХ.ХХХ.ХХХ: ")

#Разбиваем IP на части
IP_parts = IP.split('.')

# Проверяем части IP
if (int(IP_parts[0])>=0 and int(IP_parts[0]) <= 255) and (int(IP_parts[1])>=0 and int(IP_parts[1]) <= 255) and (int(IP_parts[2])>=0 and int(IP_parts[2]) <= 255) and (int(IP_parts[3])>=0 and int(IP_parts[3]) <= 255):
    print("Ваш IP введен корректно.")
else:
    print("Ваш IP введен некорректно.")