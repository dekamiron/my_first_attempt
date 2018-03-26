'''Реализовать программу, которая отображает дерево каталогов. Путь к целевому каталогу запрашивается у пользователя.
 В программе не должно использоваться циклов. Вывод результата программы должен быть следующего вида:
|__ Folder 1
|___ Folder 2
|___ File 2.1
|___ File 2.2
|__ File 1.1
|__ File 1.2'''

import os

def main(your_path):
    for i in os.listdir(your_path):
        if os.path.isdir(your_path + '/' + str(i)):
            print(i)
            main(your_path + '/' + str(i))
        else:
            print('_', i)
    return

your_pa = input('enter new path: ')
main(your_pa)