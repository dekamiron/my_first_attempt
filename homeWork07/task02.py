'''Реализовать программу с базой учащихся группы (данные хранятся в файле).
Записи по учащемуся: имя, фамилия, пол, возраст. Программа должна предусматривать поиск
по одному или нескольким полям базы. Результат выводить в удобочитаемом виде с порядковым номером записи.
Скрипт программы должен принимать параметр, который определяет формат хранения и реализации БД:
в текстовом файле с определенной структурой; в файле json'''
import json

# преобразует файл в список словарей(дескриптор файла)
def my_new_dict(file_d):
    d = [i.rstrip().split() for i in file_d]
    new_dict = [{k: j for k, j in enumerate(y, start=0)}for y in d]
    return new_dict

# поиск по значению в словарях, вывод найденых значений(список словарей, слово для поиска)
def my_search(my_d, search):
    for i in my_d:
        if search in i.values():
            print(my_d.index(i), 'name: {0[0]} second name: {0[1]} sex: {0[2]} age: {0[3]}'.format(i))
        else:
            pass

# запрашивает формат базы данных и работает с ним
def start_work(data_format):
    if data_format == 'txt':
        my_file = open('new_file_t02', 'r+')
        new_dict1 = my_new_dict(my_file)
        print(new_dict1)

        your_search = input('введите ключевое слово для поиска(name, second name, sex, age): ')
        my_search(new_dict1, your_search)
    elif data_format == 'json':
        pass '''my_file_j = open('new_file_t02', 'r+')
        реализовать работу с форматом json'''
    else:
        print('unknown format')
        
your_format = input('введите формат базы данных txt, json: ')

start_work(your_format)
