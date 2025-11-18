# def transposing_matrix(matrix):
#     transpose_matrix = []
#     for i in range(len(matrix)):
#         transpose_row = []
#         for row in matrix:
#             transpose_row.append(row[i])
#         transpose_matrix.append(transpose_row)
#     return transpose_matrix



# # transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix))] через списочные включения 

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(transposing_matrix(matrix))

def transposing_matrix(matrix):
    transpose_matrix = []
    for i in range(len(matrix[0])):  # Исправлено: берем длину первой строки
        transpose_row = []
        for row in matrix:
            transpose_row.append(row[i])
        transpose_matrix.append(transpose_row)
    return transpose_matrix

def input_matrix():
    matrix = []
    print("Введите матрицу построчно. Числа вводите через пробел.")
    print("Для завершения ввода введите пустую строку.")
    
    while True:
        row_input = input("Введите строку матрицы: ").strip()
        if not row_input:  # Пустая строка - завершение ввода
            break
        
        try:
            # Преобразуем введенные числа в список целых чисел
            row = list(map(int, row_input.split()))
            matrix.append(row)
        except ValueError:
            print("Ошибка! Вводите только числа, разделенные пробелами.")
            continue
    
    return matrix

def print_matrix(matrix, title = "Матрица"):
    print(f"\n{title}:")
    for row in matrix:
        print(row)

matrix = input_matrix()
    
if not matrix:
    print("Матрица пуста!")
else:
    # Проверка, что все строки имеют одинаковую длину
    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) != 1:
        print("Ошибка! Все строки матрицы должны иметь одинаковую длину.")
    else:
        # Вывод исходной матрицы
        print_matrix(matrix, "Исходная матрица")
        
        # Транспонирование и вывод результата
        transposed = transposing_matrix(matrix)
        print_matrix(transposed, "Транспонированная матрица")