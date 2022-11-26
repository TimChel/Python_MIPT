#2) Написать декоратор, печатающий аргументы, переданные функции, после её выполнения.
def print_arg(func):
    def new_func(*arg):
        res = func(*arg)
        print(*arg)
        return res
    return new_func


@print_arg
def foo(*x):
    print(x, 'gfhg')

foo(3, 5, 6, "v", "w")