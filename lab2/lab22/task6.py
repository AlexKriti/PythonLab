# создаем функцию для создания списка уникальных элементов 
# и определяем пустое множетво

def unique_elements(nested_list):
    unique_set = set()

    # создадим функцию для рекурсивного обхода вложенных списков

    def flat_list(lst):
        for item in lst:         

            # вызываем функцию рекурсивно при обнаружении вложенного списка

            if isinstance(item, list):
                flat_list(item)

            # иначе - это обычный элемент, добавляем его в множетво

            else:                
                unique_set.add(item)

    # запускаем рекурсивный обход и возвращаем результат
    
    flat_list(nested_list)
    return sorted(unique_set)

# используем на примере для конкретного списка

list_try = [
    1,2,3 , [4,3,1], 5 , [6, [7,[10], 8,[9,2,3]]]]


print(unique_elements(list_try)) 

