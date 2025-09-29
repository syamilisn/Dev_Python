def matin(row, col):
    print("Enter elements:")
    return [[int(input(">> ")) for j in range(col)] for i in range(row)]

def matinit(row, col, x):
    return [[x for j in range(col)] for i in range(row)]

def matout(row, col, matrix, prompt):
    print(f"Elements of {prompt} are:")
    [print([matrix[i][j] for j in range(col)], end = "\n") for i in range(row)]

def matadd(row1, col1, mat1, row2, col2, mat2):
    if(row1 == row2 and col1 == col2):
        return [[mat1[i][j] + mat2[i][j] for j in range(col1)] for i in range(row1)]
    else:
        print("Addition not possible with matrices of different order.")
        return None

def matmul(row1, col1, mat1, row2, col2, mat2):
    if(col1 == row2):
        row = row1
        col = col2
        # mul = matinit(row, col, 0)
        # return [[mul[i][j] = 0, k for k in range(col)mat1[i][j] * mat2[i][j] for j in range(col)] for i in range(row)]
        # return [[[mul[i][j]+= mat1[i][k] * mat2[k][j] for k in range(col)] for j in range(col)] for i in range(row)]
        return [[sum(a * b for a, b in zip(i, j)) for j in zip(*mat2)] for i in mat1]
    else:
        print("Multiplication not possible with matrices of different order.")
        return matinit(row, col, 0)

if __name__ == "__main__":
    """ FOR TESTING MODULE """
    row = 2
    col = 2
    # matrix = matin(row, col)
    # matout(row, col, matrix)
        # take a 3x3 matrix
    A = [[12, 7, 3],
        [4, 5, 6],
        [7, 8, 9]]
    
    # take a 3x4 matrix
    B = [[5, 8, 1, 2],
        [6, 7, 3, 0],
        [4, 5, 9, 1]]

    res = matmul(3, 3, A, 3, 4, B)
    matout(3, 4, res, "mul result")