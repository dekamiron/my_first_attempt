text = input('введите ваш текст: ')
w1 = min(text.split(' '), key=len)

short_word = set(w1)
letters = {'e', 'y', 'u', 'i', 'o', 'a', 'j'}

short_word &= letters

print('букв(a/ы) в самом коротком слове:', short_word)