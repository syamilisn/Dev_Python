def mprint(matrix):
    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end = ' ')
        print()

row, col = 3, 2
order = row * col

matrix = [[i + j for j in range(col)] for i in range(1, order, col)]
mprint(matrix)