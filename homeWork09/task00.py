'''Реализовать класс лифта Elevator. Класс должен обладать методом, lift, отвечающий за вызов лифта.
При сложении/вычитании экземпляров класса должно возвращаться значение производимой математической операции.
Если производить вычитание у лифта, который еще не совершал поднятий, должна быть выведена ошибка неправильной операции.
Предусмотреть возможность сравнения какой из лифтов совершил большее количество поднятий.
Также необходимо предусмотреть подсчет общего количества поднятий всех лифтов.
При строчных операциях необходимо вывести детальную информацию по лифту: наименование,
количество поднятий и процент от общего количества поднятий всех лифтов.'''


class Elevator:
    total = 0

    def __init__(self):
        self.call_lift = 0

    def lift(self):
        Elevator.total += 1
        self.call_lift += 1
        print(self.call_lift)
        return self.call_lift

    def __sub__(self, value):
        try:
            if value == 0:
                raise MyError
        except MyError:
            print('Error! this lift was not called')
        return value - self.call_lift

    def __rsub__(self, value):
        try:
            if self.call_lift == 0:
                raise MyError
        except MyError:
            print('Error! this lift was not called')
        return self.call_lift - value

    def __add__(self, value):
        return value + self.call_lift

    def __radd__(self, value):
        return self.call_lift + value

    @staticmethod
    def percent(value):
        return value/(Elevator.total/100)


class MyError(Elevator):
    pass


def my_percent(): # asking about name lift and print percent of total
    print('your lifts: ' + str(list_name))
    for_per = input('enter name lift: ')
    if for_per in list_name:
        ind_per = list_name.index(for_per)
        print('percentage of total ' + str(Elevator.percent(list_obj[ind_per].call_lift)))
    else:
        print('check input name and try again')
        my_percent()
    return


def mat_op(): # all mathematical operations
    op = input('What do you want? addition - a, subtraction - s, percent - p, greatest value call - g? ')
    if op == 'a': # asking 2 names lift and printing add
        print('your lifts: ' + str(list_name))
        first_lift = input('enter name first lift: ')
        second_lift = input('enter name second lift: ')
        if first_lift and second_lift in list_name:
            ind1 = list_name.index(first_lift)
            ind2 = list_name.index(second_lift)
            print('your result add ' + str(list_obj[ind1] + list_obj[ind2]))
            navigation()
        else:
            print('check input names and try again')
            mat_op()

    elif op == 's': # asking 2 names lift and printing sub
        print('your lifts: ' + str(list_name))
        first_lift = input('enter name first lift: ')
        second_lift = input('enter name second lift: ')
        if first_lift and second_lift in list_name:
            ind1 = list_name.index(first_lift)
            ind2 = list_name.index(second_lift)
            print('your result sub' + str(list_obj[ind1] - list_obj[ind2]))
            navigation()
        else:
            print('check input names and try again')
            mat_op()
    elif op == 'p': # asking about name lift and displays percentage of total
        my_percent()
        navigation()
    elif op == 'g': # asking about names 2 lifts and displays the name with the most elevations
        print('your lifts: ' + str(list_name))
        first_lift = input('enter name first lift: ')
        second_lift = input('enter name second lift: ')
        if first_lift and second_lift in list_name:
            ind1 = list_name.index(first_lift)
            ind2 = list_name.index(second_lift)
            if list_obj[ind1] > list_obj[ind2]:
                print('this lift caused more' + first_lift)
            else:
                print('this lift caused more' + second_lift)
        else:
            print('check input names and try again')
            mat_op()
    else:
        print('i do not know what do you want')
        navigation()


def navigation():
    nav = input('What will we do? s - start call lift, c - calculation, e - exit ')
    if nav == 's':
        start_l()
    elif nav == 'c':
        mat_op()
    elif nav == 'e':
        exit()
    else:
        print('i do not know this command')
        navigation()


def start_l(): # overloads method lift, ask about name for loads
    start_lift = input('what lift need call? ' + str(list_name) + ': ')
    if start_lift in list_name:
        ind = list_name.index(start_lift)
        list_obj[ind].lift()
        start_l()
    else:
        print('this lift does not exist')
        navigation()

lift_num = int(input('enter number of lifts: ')) # numbers of obj
list_name = [input('enter name lift: ') for i in range(lift_num)] # name for all obj
list_obj = [Elevator() for j in list_name] # make obj for each name

start_l()
