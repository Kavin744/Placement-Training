def matrix_multiply(A, B):
    result = [[sum(a * b for a, b in zip(row_A, col_B)) for col_B in zip(*B)] for row_A in A]
    return result

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
result_matrix = matrix_multiply(matrix1, matrix2)
print("Matrix multiplication result:")
for row in result_matrix:
    print(row)
