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
    def procent(value):
        return value/(Elevator.total/100)

    def __str__(self, value):
        return value


class MyError(Elevator):
    pass

lift_num = int(input('enter number of lifts: '))
l = [Elevator() for j in [input('enter name lift: ') for i in range(lift_num)]]

print(l)