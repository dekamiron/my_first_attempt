'''Реализовать программу, которая выводит содержимое каталога в файловой системе.
Путь к каталогу запрашивается у пользователя.'''
import os

way = input('enter your path for directory: ')


def dir_cont(path):
    new_list = os.listdir(path)
    for i in new_list:
        print(i)

dir_cont(way)