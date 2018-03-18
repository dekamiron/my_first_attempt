# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи нельзя использовать строки, списки, массивы и циклы.
your_num = int(input('enter your number: '))


def sum_num(x):
    if x < 10:
        return x
    else:
        y = x % 10 + sum_num(x // 10)
        return y

print('sum of all numbers: ', sum_num(your_num))