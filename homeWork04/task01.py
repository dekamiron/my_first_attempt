input('Hello. We will find integers starting with 2 to n, to continue press "Enter"')
n = int(input('enter your last integer number(n): '))
line = [i for i in range(2, n + 1)]


# функция заменяет все составные числа в списке от 2 до n на 0, возвращает новый список
def resheto(your_line):
    for number in your_line:
        if number != 0:
            for maybe_int in range(2 * number, n + 1, number):
                your_line[maybe_int - 2] = 0
    return your_line


a = resheto(line)
# фильтруем список от 0-й
final_a = list(filter(lambda x: x != 0, a))
print(final_a)


# фкнкция тест
def test_resheto():
    if resheto([2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 0, 5, 0, 7, 0, 0, 0]:
        print('All good')


test_resheto()