import random

n = int(input('введите размер стороны квадратной матрицы: '))

# генерирует квадратную матрицу с набором случайных целых чисел от -10 до 10
m = [[random.randint(-10, 10) for j in range(n)] for i in range(n)]

# выводит сумму всех положительных элементов матрицы выше главной диоганали
def sum_mat(matrix):
    sum_num = 0
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if x < y and matrix[x][y] > 0:
                sum_num += matrix[x][y]
    return sum_num

mat = sum_mat(m)
print(mat)

# тест для функции sum_mat()(выводит сумму всех положительных элементов выше главной диагонали)

# для данной матрицы решением будет 5
test_matrix = [
        [2, 1, -4],
        [3, 2, 4],
        [6, 1, 4],
        ]

def test_sum_mat(y):
    if sum_mat(y) == 5:
        print('все работает как надо!)')