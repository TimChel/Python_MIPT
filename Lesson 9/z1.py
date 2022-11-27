# 1) Считать матрицы (заполненные целыми числами) из файлов
# __matrix_1.csv__ и __matrix_2.csv__. Написать функцию, выполняющую
# печатающую матрицу - результат перемножения первой на вторую,
# задекорировать ее своим временным декоратором (Я вам
# запрещаю использовать готовые библиотеки
# типа `numpy` или `pandas`).
import csv
import multiprocessing as mp
import time


def time_decorator(func):
    def wrapper(*args, **kwargs):

        start_time = time.time()
        res = func(*args, **kwargs)
        res2 = time.time() - start_time
        print(res2)
        return
    return wrapper


def work(coord):
    global matrix_1
    global matrix_2
    global m
    result = 0
    for i in range(m):
        result += matrix_1[coord[0]][i] * matrix_2[i][coord[1]]
    return result


matrix_1 = []
matrix_2 = []
with open("matrix_1.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter = ";")
    for row in file_reader:
        matrix_1.append(list(map(int, row)))
with open("matrix_2.csv", encoding='utf-8') as l_file:
    file_reader = csv.reader(l_file, delimiter = ";")
    for row in file_reader:
        matrix_2.append(list(map(int, row)))
# matrix_1 = [[1, 2], [2, 1]]
# matrix_2 = [[9], [1]]
n = len(matrix_1)
m = len(matrix_1[0])
p = len(matrix_2[0])


@time_decorator
def main_function():
    global n, p
    res = [work((i, j)) for i in range(n) for j in range(p)]
    for i in range(n):
        print([res[i * p + j] for j in range(p)])


main_function()
