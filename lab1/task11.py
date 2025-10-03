# Запрос данных у пользователя
birth = input("Введите вашу дату рождения в формате XX.XX.XXXX (день:месяц:год): ")

# разбиваем дату на части
birth_parts = birth.split('.')

# определяем знак зодиака через месяц и день
match int(birth_parts[1]):
    case 1:
        if(int(birth_parts[0])<=19):
            print("Вы - Козерог")
        else:
            print("Вы - Водолей")
    case 2:
        if(int(birth_parts[0])<=18):
            print("Вы - Водолей")
        else:
            print("Вы - Рыбы")
    case 3:
        if(int(birth_parts[0])<=20):
            print("Вы - Рыбы")
        else:
            print("Вы - Овен")
    case 4:
        if(int(birth_parts[0])<=19):
            print("Вы - Овен")
        else:
            print("Вы - Телец")
    case 5:
        if(int(birth_parts[0])<=20):
            print("Вы - Телец")
        else:
            print("Вы - Близнецы")
    case 6:
        if(int(birth_parts[0])<=20):
            print("Вы - Близнецы")
        else:
            print("Вы - Рак")
    case 7:
        if(int(birth_parts[0])<=22):
            print("Вы - Рак")
        else:
            print("Вы - Лев")
    case 8:
        if(int(birth_parts[0])<=22):
            print("Вы - Лев")
        else:
            print("Вы - Дева")
    case 9:
        if(int(birth_parts[0])<=22):
            print("Вы - Дева")
        else:
            print("Вы - Весы")
    case 10:
        if(int(birth_parts[0])<=22):
            print("Вы - Весы")
        else:
            print("Вы - Скорпион")
    case 11:
        if(int(birth_parts[0])<=21):
            print("Вы - Скорпион")
        else:
            print("Вы - Стрелец")
    case 12:
        if(int(birth_parts[0])<=21):
            print("Вы - Стрелец")
        else:
            print("Вы - Козерог")
    case _:
        print("Вы неправильно ввели дату рождения")