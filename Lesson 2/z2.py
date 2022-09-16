def fibon(n):
    if n == 1 or n == 2:
        return 1
    return (fibon(n-1) + fibon(n-2))

print('Прив! Это программа высчитываен n-ое число Фибоначчи, используя рекурсию. Введите n:')
n = int(input())
print('n-ое число Фибоначчи: ', fibon(n))