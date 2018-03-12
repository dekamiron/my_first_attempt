def ex1():
    M = [
        [2, 1, 4],
        [3, 2, 4],
        [6, 1, 4],
    ]

    # функция считающая среднеарифметическое значение всех элементов матрицы
    def sr_sum(y):
        sum_l = 0
        for i in y:
            for j in i:
                sum_l += j / (len(y) * len(i))
        return sum_l

    P = sr_sum(M)
    print(P)