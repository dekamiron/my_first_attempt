lis = input('enter your line: ')
se = input('enter your separator: ')

# функция принимает (строка, разделитель) и выдает список слов с длинной слова впереди
def final_list(your_line, sep):
    f_l = [str(len(x))+x for x in list(your_line.split(sep))]
    return f_l

a = final_list(lis, se)
print(a)


# функция-тест для строки "Hello World", разделитель пробел
def test_final_list():
    if final_list('Hello World', ' ') == ['5Hello', '5World']:
        print('All right!!!')

test_final_list()