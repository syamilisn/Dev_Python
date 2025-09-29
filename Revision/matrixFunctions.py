def minput(row, col):
    order = row * col
    print("Enter elements:")
    matrix = [[int(input(">> ")) for j in range(col)] for i in range(0, order, col)]     #input elements in newline on console
    print(matrix)
    return matrix

print("Enter row, col:")
row, col = map(int, input().split())
max1 = minput(row, col)
max2 = minput(row, col)