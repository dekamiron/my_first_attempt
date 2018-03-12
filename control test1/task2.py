'''в числовой матрице поменять местами два столбца. Матрица заполняется пользователем
    После запрашиваются номера столбцов которые нужно поменять местами.'''

matrix = [[int(input('Enter your numbers for matrix(3*4): ')) for j in range(4)] for i in range(3)]

x1 = int(input('Enter first column: '))
x2 = int(input('Enter second column: '))

print(matrix)

for x in matrix:
        x[x1], x[x2] = x[x2], x[x1]

print(matrix)
