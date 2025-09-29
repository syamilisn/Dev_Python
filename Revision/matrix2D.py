
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

row = 3
col = 3
order = row * col

matrix2D = [[ i+j+1 for j in range(row)] for i in range(order) if i % 3 == 0]
# matrix2D = [if(x+1 % 3 != 0 or x == 0)[x+1, x+2, x+3] for x in range(ele)]
print(matrix2D)

list = [[i, i+1, i+2] for i in range(1, 10, 3)]
print(list)

matrix = [[ i+j for j in range(row)] for i in range(1, order, 3)]       #ANY 2D MATRIX
print(matrix)

# for i in range(3):
#     for j in range(3):
#         print(matrix[i][j], end=' ')
#     print()