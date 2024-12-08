matrix = [["one","two"],["three","four"]]

print(matrix[1][0])
print(matrix[0][1])

row = len(matrix)

column = len(matrix[0])

for i in range(row):
    for j in range(column):
        print(matrix[i][j])

matrixa = [[7,2],[5,3]]
matrixb = [[9,1],[8,4]]

Add = [[0,0],[0,0]]

row = len(matrixa)
column = len(matrixa[0])

for i in range(row):
    for j in range(column):
        print(matrixa[i][j])


column = len(matrixb[0])

for i in range(row):
    for j in range(column):
        print(matrixb[i][j])
        Add[i][j] = matrixa[i][j] + matrixb[i][j]

print(Add)

Subtract = [[0,0],[0,0]]

row = len(matrixa)
column = len(matrixb[0])

for i in range(row):
    for j in range(column):
        print(matrixb[i][j])
        Subtract[i][j] = matrixa[i][j] - matrixb[i][j]

print(Subtract)


Multiply = [[0,0],[0,0]]

row = len(matrixa)
column = len(matrixb[0])

for i in range(row):
    for j in range(column):
        print(matrixb[i][j])
        Multiply[i][j] = matrixa[i][j] * matrixb[i][j]

print(Multiply)

