'''Реализовать программу с базой учащихся группы (данные хранятся в файле).
Записи по учащемуся: имя, фамилия, пол, возраст. Программа должна предусматривать
поиск по одному или нескольким полям базы. Результат выводить в удобочитаемом виде
с порядковым номером записи.'''

my_file = open('new_file_t03.txt', 'r+')

d = [i.rstrip().split() for i in my_file]

'''new_dic = {k: v for k, v in enumerate(d, start=0)}
print(new_dic)'''

search = input('введите ключевое слово для поиска(name, second name, sex, age): ')

for i in d:
    if search in i:
        print(d.index(i), 'name: %s second name: %s sex: %s age %s' \
                  % (i[0], i[1], i[2], i[3]))
    else:
        pass