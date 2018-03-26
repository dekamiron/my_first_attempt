# декоратор, позволяющий вместе с результатом функции возвращать время ее работы;
import time, inspect
def timer(fun):
    def tmp(*args, **kwargs):
        t = time.time()
        res = fun(*args, **kwargs)
        print("Время выполнения функции: %f" % (time.time()-t))
        return res
    return tmp

@timer
def hello():
    time.sleep(1)
    print('Hello World')
    return

hello()

# декоратор, позволяющий записывать время работы функции, имя функции и переданные ей параметры
# в текстовый файл;

def write_in_file(fun):
    def tmp(*args):
        t = time.time()
        res = fun(*args)
        name = fun.__name__
        arg = [str(i) for i in args]
        with open('new_file02.txt', 'w+') as e:
            e.write('Time work: %f' % (time.time()-t) + '\n')
            e.write('name function: ' + name + '\n')
            e.write('args function: ' + ' '.join(arg))
        return res
    return tmp

@write_in_file
def sum_numb(x, y):
    return x + y

sum_numb(5, 6)

# декоратор, проверяющий типы, переданных декорируемой функции, аргументов.

def type_args(fun):
    def test_a(*args):
        res = fun(*args)
        l = [type(i) for i in args]
        print(l)
        return res
    return test_a

@type_args
def sum_arg(x, y):
    return x + y

sum_arg(5, 6)

# декоратор, который кэширует результат работы функции, тем самым обеспечивает единственный вызов функции


def memo_func(fun):
    memory = {}

    def memo(*args, **kwargs):
        hash = (tuple(args), frozenset(kwargs.items()))
        if hash not in memory:
            memory[hash] = fun(*args, **kwargs)
        return memory[hash]
    return memo

@memo_func
def cache_sum(x, y):
    return x + y

cache_sum(3, 5)
