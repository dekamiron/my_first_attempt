# Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.

fi = open('my_file', 'w')

while True:
    my_str = input('Enter your words: ')
    if not my_str:
        break
    my_str += '\n'
    fi.write(my_str)