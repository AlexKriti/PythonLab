# Запрос данных у пользователя

print("Введите два слова: ")

# понижаем регистр

fir_word = input().lower()
sec_word = input().lower()

# создаем списки из слов

letters_list_fir = [letter for letter in fir_word]
letters_list_sec = [letter for letter in sec_word]

# сортируем списки с помощью sort - метода сортировки списка с его изменением по
# key-критерию(указывается в скобках или не указывается - по умолчанию)

letters_list_fir.sort()
letters_list_sec.sort()

# сравниваем списки, если совпадают, то слова являются анаграммами
print("Ваши слова являются анаграммами!") if letters_list_fir == letters_list_sec else print("Ваши слова не являются анаграммами!")

