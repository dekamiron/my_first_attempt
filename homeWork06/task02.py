# В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу.

# This fun add in new doc user's words
def wr_str(my_f):
    my_str = input('enter your word:')
    if my_str:
        my_str += '\n'
        my_f.write(my_str)
        wr_str(my_f)
    return
my_file1 = open('new_file_t02', 'w+')

wr_str(my_file1)
my_file1.close()

my_file1 = open('new_file_t02', 'r+')
new_file2 = [i.rstrip().split() for i in my_file1]

# возвращает среднюю оценку среди списка
av_num = sum(int(i[2]) for i in new_file2) / len(new_file2)

bad_study = [i for i in new_file2 if int(i[2]) < 3]

print('mean points: ', av_num)
print('bad study: ', bad_study)
