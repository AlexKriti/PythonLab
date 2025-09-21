import random

#Задаем рандомное число от 1 до 100
num = random.randint(1,100)
print("Вам нужно отгадать число от 1 до 100\n")

# Запрос данных у пользователя
ent_num = int(input("Введите ваше число: "))
while ent_num != num:
    if ent_num > num:
        print("Ваше число больше загаданного\n")
    else:
        print("Ваше число меньше загаданного\n")
    ent_num = int(input("Введите новое число: "))

print("Ура! Вы отгадали число!")