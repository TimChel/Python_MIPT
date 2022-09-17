def sortx(mass, start = 0, stop = None):
    if stop is None:
        stop = len(mass) - 1
    if stop - start < 2:
        return
    i = start
    j = stop
    while i < j:
        while mass[i] < mass[stop]:
            i += 1
        while j > 0 and mass[j] >= mass[stop]:
            j -= 1
        if i < j:
            mass[i], mass[j] = mass[j], mass[i]
    mass[i], mass[stop] = mass[stop], mass[i]
    sortx(mass, start, i - 1)
    sortx(mass, i + 1, stop)

print('Здравствуйте. Вас приветствует сортировка Хоара. Введите свой массив:')
mass = list(map(int, input().split()))
sortx(mass)
print('Отсортированный массив: ', *mass)