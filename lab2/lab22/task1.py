# определяем функцию разбиения вложенных списков

def flat_list(lst):
    def step(index):

        # завершаем рекурсию, если индекс выходит за пределы

        if index >= len(lst):
            print("Полученный список в результате разбиения: ")
            print(lst)
            return

        # проверяем, является ли данный элемент списком

        if isinstance(lst[index], list):

            # если является, разворачиваем элемент на месте

            current = lst.pop(index)
            lst[index:index] = current
            step(index)
        else:
            step(index + 1)
    step(0)

# проверяем на значениях

lst = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
lst2 = [1, [2, 3], [4, [[10], 11]], 5, [6, [7, [], 8, [9]]], [12]]
flat_list(lst)
flat_list(lst2)
