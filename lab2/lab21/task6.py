# Запрос данных у пользователя

print("Введите любой список: ")

# определяем список списки

fir_list = input().split()
unique_list = []

# выявляем дубликаты

for item in fir_list:
    if item not in unique_list:
        unique_list.append(item)

# выводим на экран

fir_list = unique_list
print(fir_list)