word = input('введите ваше слово: ')
w1 = list(word.lower())

if w1[0].isalpha() or w1[0] == '_':
    for x in w1[1:]:
        if not x.isalpha() or x.isdigit():
            print('в вашем слове присутствуют недопустимые символы для индетификатора')
            quit()
    print('ваше слово: {}'.format(word), 'является индетификатором')
else:
    print('ваше слово не является индентификатором')