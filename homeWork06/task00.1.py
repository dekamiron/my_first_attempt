# Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.

fi = open('my_file', 'r+')

# This fun add in new doc user's words
def wr_str(my_f2):
    my_str = input('enter your word:')
    if my_str:
        my_str += '\n'
        my_f2.write(my_str)
        wr_str(my_f2)
    return

wr_str(fi)