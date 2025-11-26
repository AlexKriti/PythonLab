# запрашиваем у пользователя первый список чисел

fir_list = input("Введите числа первого списка: ").split()

# создадим список с результатами применения итератора map, 
# который переделывает все значения в списке из строки в float

fir_list = list(map(float, fir_list))

# запрашиваем у пользователя второй список чисел

sec_list = input("Введите числа второго списка: ").split()

# создадим список чисел так же, как и для первого списка строк

sec_list = list(map(float, sec_list))

# найдем объединение путем добаления числа num в список, доставая его 
# из первого списка и проверяя, есть ли он во втором списке 

intersection = [num for num in fir_list if num in sec_list ]

# похожим образом составляем список из значений, содержащихся только в первом списке

fir_without_sec = [num for num in fir_list if num not in sec_list ]

# так же составим список из элементов обоих списков, входящих в один из двух списков
not_intersection = [num for num in fir_list + sec_list if num not in intersection ]

# выводим на экран
print(intersection)
print(fir_without_sec)   
print(not_intersection)

# примеры для ввода
# 5.5 3 43.0 78 1542 -100 105 69 1923
# 5.5 43.1 78 1544 -101 105 9 -100  