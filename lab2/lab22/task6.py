from task1 import flatten_list 

def unique_elements(nested_list):
    flatten_list(nested_list)
    unique_list  = []

    for item in nested_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# используем на примере для конкретного списка

list_try = [1,2,3 , [4,3,1], 5 , [6, [7,[10], 8,[9,2,3]]]]

print(unique_elements(list_try)) 

