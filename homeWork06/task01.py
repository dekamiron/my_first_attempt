# В текстовом файле посчитать количество строк,
# а также для каждой отдельной строки определить количество в ней символов и слов.

my_file2 = open('my_file', 'r')
new_file2 = [i.rstrip('\n') for i in my_file2]


def sum_str_cha_wor(new_list):
    sum_str = len(new_list)
    sum_cha = [len(y) for y in new_list]
    sum_wor = [len(z.split()) for z in new_list]
    return sum_str, sum_cha, sum_wor

a = sum_str_cha_wor(new_file2)
print('this file has', a[0], 'string, in each string of', a[1], 'characters and of', a[2], 'words')

