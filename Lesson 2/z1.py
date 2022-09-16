print('Прив! Это программа высчитываен n-ое число Фибоначчи, используя динамическое программирование. Введите n:')
n = int(input())
fib = []
fib.append(1)
fib.append(1)
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
print('n-ое число Фибоначчи: ', fib[-1])