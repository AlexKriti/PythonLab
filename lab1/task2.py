# Запрос данных у пользователя
text = input("Введите строку: ")

#строка со всеми гласными
vowels = "aeiouAEIOU"

#создаем таблицу перевода строки и указываем нашу строку, как символы, которые необходимо удалить
translation_table = str.maketrans('', '', vowels)

#применяем таблицу 
result = text.translate(translation_table)
print("Результат:", result)