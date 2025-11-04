def transposing_matrix(matrix):
    transpose_matrix = []
    for i in range(len(matrix)):
        transpose_row = []
        for row in matrix:
            transpose_row.append(row[i])
        transpose_matrix.append(transpose_row)
    return transpose_matrix



# transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix))] через списочные включения 

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(transposing_matrix(matrix))