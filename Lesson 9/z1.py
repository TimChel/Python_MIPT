# 2) Написать функцию, выполняющую аналогичные
# вычисления, но с использованием библиотеки
# `multiprocessing`, причем функция должна принимать
# аргументом число вспомогательных подпроцессов.
import csv
import multiprocessing as mp
import time
# def work(x):
#     time.sleep(0.0000000000001)
#     print(x)
#     return x

def time_decorator(func):
    def wrapper(*args, **kwargs):

        start_time = time.time()
        res = func(*args, **kwargs)
        res2 = None
        if __name__ == "__main__":
            res2 = time.time() - start_time
            print(res2)
        return res, res2
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
def main_function(proc):
    global n, p
    if __name__ == "__main__":
        pond = mp.Pool(proc)
        res = pond.map(work, ((i, j) for i in range(n) for j in range(p)))
        for i in range(n):
            print([res[i*p + j] for j in range(p)])


time_list=[]
main_function(mp.cpu_count() - 1)
for i in range(mp.cpu_count() - 1):
    time_list.append((i+1, main_function(i+1)[1]))
print(time_list)