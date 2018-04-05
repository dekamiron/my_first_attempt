'''
Требуется написать программу для генерации и проверки контрольных сумм у файлов. Входные данные
Файл-манифест – текстовый файл, в котором содержится информация о контрольных суммах для некоторого набора файлов.
Структура:
<имя_файла_1>:<контрольная_сумма_для_файла_1>
<имя_файла_2>:<контрольная_сумма_для_файла_2>
<имя_файла_3>:<контрольная_сумма_для_файла_3>

Задание
Сама программа должна иметь возможность работы в двух режимах:
Режим 1. Подсчет контрольной суммы для заданного набора файлов и генерация файла-манифеста.
На вход программы в качестве аргументов командной строки подается набор имён файлов. Для каждого из этих файлов
программа должна осуществить подсчёт контрольной суммы и занести информацию об имени файла и соответствующей ему
контрольной сумме в файл-манифест.

Режим 2. Проверка целостности файлов.

На вход программы в качестве аргумента командной строки подаётся файл-манифест. Для каждого из файлов, указанных в
файле-манифесте, необходимо осуществить подсчёт контрольной суммы, сравнить с той, которая указана в манифесте,
и выдать в консоль результат о совпадении (ОК) или несовпадении (FAILED) значений.
Режим работы программы задается ключом, переданным как аргумент командной строки. Для первого режима можно использовать
ключ --calc, для второго — --check.

Пример запуска
checksum.py --calc <имя_файла_1> ... <имя_файла_N>

Вывод:
checksum for <имя_файла_1> calculated
...
checksum for <имя_файла_N> calculated

Проверка целостности файлов.
<название_бинарника> --check <имя_файла_манифеста>

Вывод:
<имя_файла_1> : <OK/FAILED>
...
<имя_файла_N> : <OK/FAILED>
'''
from hashlib import md5
import os, sys, getopt, argparse


def my_hash_fun(file_name):
    with open(file_name) as f:
        all_hash = md5(''.encode())
        for line in f:
            all_hash.update(line.encode())
    return all_hash.hexdigest()


def my_files():
    path = 'D:/python/задачи/manifest/files'
    all_file = os.listdir(path)
    hash_dic = {}
    for file in all_file:
        if file.endswith('txt'):
            hash_dic[file] = my_hash_fun(file)
    return hash_dic


def write_manifest():
    with open('manifest1.txt', 'r+') as man:
        man.write(str(my_files()))


def test_change():
    new_dic = my_files()
    with open('manifest1.txt', 'r+') as saved_dict:
        str_file = saved_dict.read()
        dic_file = eval(str_file)
    for key in new_dic:
        if new_dic[key] == dic_file[key]:
            print(key + ' OK')
        else:
            print(key + ' FAILED')

def createParser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    hello_parser = subparsers.add_parser('calc')
    hello_parser.add_argument('--calc')

    goodbye_parser = subparsers.add_parser('goodbye')
    goodbye_parser.add_argument('-c')

    return parser


#my_files()
#write_manifest()
#test_change()