import os
import copy

# смена директории, пользователь вводит новую
def leave_dir():
    new_dir = input('enter new path: ')
    os.chdir(new_dir)
# функция изменяет имя выбранному объекту в текущей директории
def ren_f():
    old_name = input('enter name file for rename: ')
    new_name = input('enter new name for rename file: ')
    os.rename(old_name, new_name)
# функция копирует файл и возвращает его копию
def copy_f():
    my_odj = input('enter file name for copy: ')
    cop_f = copy.deepcopy(my_odj)
    return cop_f
# создание нового файла(имя вводит пользователь), доступен для записи
def make_f():
    new_f = open(input('enter name your file: '), 'w+')
    new_f.close()
# удаляет файл, имя вводит пользователь
def del_f():
    rem_f = input('enter name del file: ')
    os.remove(rem_f)