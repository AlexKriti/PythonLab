# определим фунцию транспонирования матрицы

def transposing(matrix):

    # определяем размеры матрицы

    rows = len(matrix)
    cols = len(matrix[0])

    # подготовим основу для транспонированной матрицы 

    transposed_matrix = [[0] * rows  for _ in range(cols )]

    # заполняем основу транспонированной матрицы значениями из данной матрицы   

    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    # возвращаем транспонированную матрицу
    
    return transposed_matrix

# выведем результат транспонирования пробной матрицы

print("Транспонируем матрицу [[56, 25], [78, 42]]: ")
print(transposing([[56, 25], [78, 42]]))