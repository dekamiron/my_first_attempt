'''Реализовать программу, позволяющую осуществлять управление файлами:
копирование, создание, удаление, переименование. Необходимо предусмотреть возможность
смен директории. Изначально используется текущий каталог запуска скрипта программы.'''
import copy
import os
from fun import my_fun_for_task05 as a
# все функции работы с фалами вынес в отдельный документ my_fun_for_task05.py

# переход в другую деректорию, заново запрашивает работу с файлами
def leaving():
    a.leave_dir(), file_man()

# управляет работой файлового мененджера и возможностью перехода в другую дерикторию
def navigation():
    l = input("sorry, i can't do it, continue?(N - exit) Y/N: ")
    if l == 'Y':
        file_man()
    elif l == 'N':
        exit()
    else:
        navigation()

# позволяет копировать, создавать, удалять и переименовывать файлы
def file_man():
    com = input('what we will be do with files?(copy - c, new - n, del - d, rename - r, leave dir - l): ')
    if com == 'r':
        a.ren_f(), file_man()
    elif com == 'c':
        a.copy_f(), file_man()
    elif com == 'n':
        a.make_f(), file_man()
    elif com == 'd':
        a.del_f(), file_man()
    elif com == 'l':
        leaving()
    else:
        navigation()

file_man()
