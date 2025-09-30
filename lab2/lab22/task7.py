# определяем функцию

def merged_sorted_list(lst1, lst2): 

    # инициализируем начальные данные

    lst = []
    i=0 
    j = 0 

    # проходим основной цикл слияния(сравниваем/добавляем элементы)

    while i < len(lst1) and j < len(lst2) : 
        if lst1[i] <= lst2[j]: 
            lst.append(lst1[i])
            i+= 1 
        else: 
            lst.append(lst2[j])
            j+=1 

    # добавляем оставшиеся элементы

    while i < len(lst1): 
        lst.append(lst1[i])
        i+=1
    while j < len(lst2): 
        lst.append(lst2[j]) 
        j+=1
    return lst 

# пример для исполнения

lst1= [1,2,3 ]
lst2 = [-1, 0, 1,2,6]
lst = merged_sorted_list(lst1, lst2)
print(lst)