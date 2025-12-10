# # определяем функцию

# def merged_sorted_list(lst1, lst2): 

#     # инициализируем начальные данные

#     lst = []
#     i = 0 
#     j = 0 

#     # проходим основной цикл слияния(сравниваем/добавляем элементы)

#     while i < len(lst1) and j < len(lst2) : 
#         if lst1[i] <= lst2[j]: 
#             lst.append(lst1[i])
#             i+= 1 
#         else: 
#             lst.append(lst2[j])
#             j+=1 

#     # добавляем оставшиеся элементы

#     while i < len(lst1): 
#         lst.append(lst1[i])
#         i+=1
#     while j < len(lst2): 
#         lst.append(lst2[j]) 
#         j+=1
#     return lst 

# # пример для исполнения

# lst1= [1, 2, 3]
# lst2 = [-1, 0, 1, 2, 6]
# res_lst = merged_sorted_list(lst1, lst2)
# print(res_lst)

def merged_sorted_list(lst1, lst2):
    """Функция для слияния двух отсортированных списков в один отсортированный список"""
    lst = []
    i = 0
    j = 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            lst.append(lst1[i])
            i += 1
        else:
            lst.append(lst2[j])
            j += 1

    while i < len(lst1):
        lst.append(lst1[i])
        i += 1
    while j < len(lst2):
        lst.append(lst2[j])
        j += 1
    return lst

# Ввод данных от пользователя
print("Введите элементы первого отсортированного списка через пробел:")
lst1 = list(map(int, input().split()))

print("Введите элементы второго отсортированного списка через пробел:")
lst2 = list(map(int, input().split()))

# Сортировка списков на случай, если пользователь ввел неотсортированные данные
lst1.sort()
lst2.sort()

# Слияние и вывод результата
result = merged_sorted_list(lst1, lst2)
print(f"Результат слияния: {result}")