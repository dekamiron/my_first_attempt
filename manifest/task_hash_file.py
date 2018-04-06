'''
Требуется написать программу для генерации и проверки контрольных сумм у файлов. Входные данные
Файл-манифест – текстовый файл, в котором содержится информация о контрольных суммах для некоторого набора файлов.

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
'''
from hashlib import md5
import os, sys


def my_hash_fun(file_name): # this function counts hash
    with open(file_name) as f:
        all_hash = md5(''.encode())
        for line in f:
            all_hash.update(line.encode())
    return all_hash.hexdigest()


def my_files(): # this function loads all 'txt' files and make dict {name:hash}
    path = 'D:/python/задачи/manifest/files'
    all_file = os.listdir(path)
    hash_dic = {}
    for file in all_file:
        if file.endswith('txt'):
            hash_dic[file] = my_hash_fun(file)
    return hash_dic


def write_manifest(): # writing in manifest
    with open('manifest1.txt', 'r+') as man:
        man.write(str(my_files()))


def test_change(): # check for file changes
    new_dic = my_files()
    with open('manifest1.txt', 'r+') as saved_dict:
        str_file = saved_dict.read()
        dic_file = eval(str_file)
    for key in new_dic:
        if new_dic[key] == dic_file[key]:
            print(key + ' OK')
        else:
            print(key + ' FAILED')


if __name__ == '__main__':
    try:
        a = sys.argv[1]
        if a == "--calc":
            print('hash in your file', my_files())
        elif a == "--check":
            test_change()
        else:
            print('check your argument(--calc or --check)')
    except IndexError:
        print('you have to enter arg \'--calc\' or \'--check\'')
