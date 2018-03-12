def ex0():
    L = input('введите ваши числа: ')
    L1 = list(map(int, L.split()))

#сравнивает ключи словаря, в случае наличия увеличивает значение на 1
    def wor(lis):
        d = {}
        for i in lis:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return d

    new_lis = wor(L1)
    M_L = max(new_lis.items(), key=lambda x: x[1])

    print('число {} встречается {} раз(а)'.format(*M_L))