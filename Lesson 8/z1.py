#1) Написать декоратор, разворачивающий порядок переданных в функцию аргументов
#независимо от их количества (например декорированная __foo(4, 5)__ должна быть
#эквивалентна вызову недекорированной __foo(5, 4)__)
def reverse(func):
    def new_func(*arg):
        arg = list(arg)
        for i in range(len(arg)//2):
            arg[i], arg[-i - 1] = arg[-i - 1], arg[i]
        res = func(*arg)

        return res
    return new_func


@reverse
def foo(*x):
    print(x)

foo(2, 4, 5)