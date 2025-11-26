# Запрос данных у пользователя

print("Введите строку: ")
string = input() 

# определяем счетчик, список для новой строки и первый символ строки

encoded_list = [] 
count= 1 
previous_char = string[0]

# проходимся в цикле по строке

for i in  range(1, len(string)): 

    # считываем текщий символ для сравнения с предыдущим

    current_char = string[i]

    # если совпадают, увеличиваем счетчик 

    if current_char == previous_char : 
        count += 1 

    # иначе добавляем в список символ и значение счетчика, после счетчик обновляем

    else :
        encoded_list.append(previous_char + str(count))
        previous_char = current_char
        count = 1

# добавляем последний символ в список 

encoded_list.append(previous_char + str(count))

# объединяем список в строку

encoded_string = ''.join(encoded_list)

# выводим на экран

print(encoded_string)