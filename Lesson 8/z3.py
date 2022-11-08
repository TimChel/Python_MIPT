#3) Написать декоратор, пробующий запустить переданную функцию, и возвращающий
#строку "error" в случае возникновения исключения.
def error_founder(func):
    def new_func(*arg):
        try:
            res = func(*arg)
            return res
        except Exception:
            print('error')
    return new_func


@error_founder
def foo(x):
    print(x + 5)


foo('i')
