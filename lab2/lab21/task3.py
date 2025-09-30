# Запрос данных у пользователя

entr_str = input("Введите ваши числа через пробел: ")

# разбиваем на отдельные числа

nums = entr_str.split()

# переопределим список строковых как список числовых значений 
nums = [float(a) if '.' in a else int(a) for a in nums]


if nums[0] > nums[1]:
    fist_num = nums[0]
    sec_num = nums[1] 
else:
    fist_num = nums[1]
    sec_num = nums[0] 

# проходимся по всему списку и сравниваем каждый элемент с известным нам самым большим элементом

for num in nums:
    if num > fist_num:
        sec_num = fist_num
        fist_num = num

print("Ваше число: " + str(sec_num))

# варианты для проверки : 5.5 3 43.0 78 1542 -100 105 69 1923
# -985.5 12 -20 6.999 205