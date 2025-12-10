# Запрос данных у пользователя

entr_str = input("Введите ваши числа через пробел: ")

# разбиваем строку на части и преобразуем в числа с учетом точки

numbers_str = entr_str.split()
numbers = []
numbers = [float(num) if '.' in num else int(num) for num in numbers_str]

# определим список уникальных чисел после использования итератора множества

unique_numbers = list(set(numbers))

# определяем повторяющиеся элементы через список уникальных элементов

repeated_numbers= [num for num in unique_numbers if numbers.count(num) > 1  ]

# определяем четные/нечетные элементы (isinstance - проверка типа элемента)

even =  [ num for num in numbers if isinstance(num, int) and  num % 2 == 0 ]
odd = [num for num in numbers if isinstance(num, int) and num % 2 != 0] 

# определяем отрицательные и числа с плавающей точкой

negatives = [num for num  in numbers if num < 0 ]
float_num = [num for num in numbers if isinstance(num, float)]

# суммируем, если число делится на 5 без остатка

sum_numbers_5 = sum(num for num in numbers if num % 5 == 0)

# берем макс и мин значения в списке

max_numbers = max(numbers)
min_numbers = min(numbers)

# выводим на экран
print("Уникальные числа: ")
print(unique_numbers)
print('\n' + "Повторяющиеся числа: ")
print(repeated_numbers) 

# определяются из общего списка, могут повторяться
# ///
print('\n' + "Чётные числа: ")
print(even)
print('\n' + "Нечётные числа: ")
print(odd)
print('\n' + "Отрицательные числа: ") 
print(negatives)
print('\n' + "Числа с плавающей точкой: ")
print(float_num)
# ///

print('\n' + "Сумма всех чисел, кратных 5: ")
print(sum_numbers_5)
print('\n' + "Самое большое число: ")
print(max_numbers)
print('\n' + "Самое маленькое число: ")
print(min_numbers)

# пример для ввода: 25 32 0.32 157 80 -95 16.44 83 80 0.32 625