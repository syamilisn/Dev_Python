from mod_matrix import matin, matout, matadd, matmul

row1, col1 = map(int, input("Enter order of matrix 1:\n>> ").split())
order1 = row1 * col1
mat1 = matin(row1, col1)
matout(row1, col1, mat1, "matrix 1")

row2, col2 = map(int, input("Enter order of matrix 2:\n>> ").split())
order2 = row2 * col2
mat2 = matin(row2, col2)
matout(row2, col2, mat2, "matrix 2")

mat3 = matadd(row1, col1, mat1, row2, col2, mat2)
matout(row1, col1, mat3, "matrix 3 (sum)")

mat4 = matmul(row1, col1, mat1, row2, col2, mat2)
matout(row1, col1, mat4, "matrix 4 (mul)")