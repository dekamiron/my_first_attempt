# Вводиться строка слов разделенных пробелами. Найти самое длинное слово,
# и вывести его на экран. Если самое длинное слово встречается несколько раз,
# вывести следующее самое длинное слово.

your_str = list(input('enter your line: ').split())
st = list(sorted(your_str, key=lambda x: len(x), reverse=True))

i = 0
while True:
    if len(st[i]) > len(st[i+1]) and len(st[i]) != len(st[i-1]):
        print('Самый длинный из уникальных элементов: ', st[i])
        break
    else:
        i += 1