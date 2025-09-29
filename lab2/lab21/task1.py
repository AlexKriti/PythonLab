
import re

# Запрос данных у пользователя

entr_str = input("Введите строку: ")

# Приведение к нижнему регистру

entr_str = entr_str.lower()

# избавляемся от символов-разделителей

words = re.split(r'[ ,.!?]', entr_str)
words = ' '.join(words)
words = words.split()
# length = len(words)

#создадим словари

reps_dict = {}
cur_reps_dict = {}

# создадим счетчик повторений

counter = 0
print(words)
print("\n")

for word in words:
    reps_dict[word] = reps_dict.get(word, 0) + 1
print(reps_dict)

for word in reps_dict:
    if(reps_dict[word] == 1):
        counter = counter + 1

print("Кол-во уникальных слов: "  + str(counter))


# # asd ? asd ASD!!gruy Kj jk JK,,,,,
# **************
