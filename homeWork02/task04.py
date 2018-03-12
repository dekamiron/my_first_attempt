sum_s = 1000
sum_e = 1100
per = 0

mont = 0
while sum_s < sum_e:
    per = float(input('введите желаемые проценты(от 0 до 25):'))
    if 0 < per < 25:
        sum_s += sum_s/100*per
        mont += 1
    else:
        print('вы ввели неверное количество процентов, попробуйте еще раз')

print('через {} месяцев, сумма составит {}'.format(mont, sum_s))