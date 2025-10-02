n = int(input("Enter number of rows in matrix: "))
m = int(input("Enter number of columns in matrix: "))

matrix = []

for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(int(input(f"Enter element {i + 1} {j + 1}: ")))

def printMatrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

printMatrix(matrix)

newMatrix = []

for i in range(m):
    newMatrix.append([])
    for j in range(n):
        newMatrix[i].append(matrix[j][i])

printMatrix(newMatrix)