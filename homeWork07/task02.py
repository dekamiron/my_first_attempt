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

new_d = []
my_js = open('new_file_t02_j.js', 'r+')
for i in my_js:
    new_d.append(json.load(i))
    
your_word = input('enter your word for searching: ')
my_search(new_d, your_word)
