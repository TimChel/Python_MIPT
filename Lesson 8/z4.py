# 4) Написать программу, сравнивающую скорость работы функции вычисления чисел
# Фибоначчи, написанной через циклы и через рекурсию, с использованием __@lru_cache(maxsize=None)__
# и без.
import time


def time_decorator(func):
    def wrapper(*args, **kwargs):

        start_time = time.time()
        res = func(*args, **kwargs)
        res2 = time.time() - start_time
        return res, res2
    return wrapper


@time_decorator
def fib_c(n):
    x1 = 0
    x2 = 1
    for i in range(n):
        x1, x2 = x2, x1 + x2
    return x1


@time_decorator
def fib_r(n):
    if n == 1 or n == 2:
        return 1
    return fib_r(n-1) + fib_r(n-2)


print('Без использования кэша:\nЦиклы:', fib_c(25)[1], '\nРекурсия:', fib_r(25)[1])
fib_c = lru_cache(maxsize=None)(fib_c)


print('С кэшом:\nЦиклы:', fib_c(25)[1], '\nРекурсия:', fib_r(25)[1])