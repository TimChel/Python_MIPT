# 3) Построить график (можно использовать __excel__) функции
# __f(n) = T<sub>1</sub> / T<sub>n</sub>__,
# где __T<sub>n</sub>__ - время работы функции
# перемножения матриц с использованием __n__ подпроцессов.
import csv
import multiprocessing as mp
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter


def time_decorator(func):
    def wrapper(*args, **kwargs):

        start_time = time.time()
        res = func(*args, **kwargs)
        res2 = 1
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
for i in range(mp.cpu_count() - 1):
    time_list.append([i+1, main_function(i+1)[1]])
    time_list[i][1] = time_list[0][1] / time_list[i][1]
if __name__ == "__main__":
    print(time_list)


np.random.seed(19680801)

X = [time_list[i][0] for i in range(len(time_list))]
Y1 = [time_list[i][1] for i in range(len(time_list))]
print(X, Y1)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, aspect=1)


def minor_tick(x, pos):
    if not x % 1.0:
        return ""
    return "%.2f" % x

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(4))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(4))
ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.set_xlim(0, 4)
ax.set_ylim(0, 4)

ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=10)
ax.tick_params(which='minor', width=1.0, labelsize=10)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.25')

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Blue signal", zorder=10)


ax.set_title("Anatomy of a figure", fontsize=20, verticalalignment='bottom')
ax.set_xlabel("X axis label")
ax.set_ylabel("Y axis label")

ax.legend()


def circle(x, y, radius=0.15):
    from matplotlib.patches import Circle
    from matplotlib.patheffects import withStroke
    circle = Circle((x, y), radius, clip_on=False, zorder=10, linewidth=1,
                    edgecolor='black', facecolor=(0, 0, 0, .0125),
                    path_effects=[withStroke(linewidth=5, foreground='w')])
    ax.add_artist(circle)


def text(x, y, text):
    ax.text(x, y, text, backgroundcolor="white",
            ha='center', va='top', weight='bold', color='blue')


color = 'blue'
ax.annotate('Spines', xy=(4.0, 0.35), xycoords='data',
            xytext=(3.3, 0.5), textcoords='data',
            weight='bold', color=color,
            arrowprops=dict(arrowstyle='->',
                            connectionstyle="arc3",
                            color=color))

ax.annotate('', xy=(3.15, 0.0), xycoords='data',
            xytext=(3.45, 0.45), textcoords='data',
            weight='bold', color=color,
            arrowprops=dict(arrowstyle='->',
                            connectionstyle="arc3",
                            color=color))

ax.text(4.0, -0.4, "Made with http://matplotlib.org",
        fontsize=10, ha="right", color='.5')

if __name__ == "__main__":
    plt.show()