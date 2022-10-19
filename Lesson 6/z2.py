#2) Написать функцию генератор, создающую числа фибоначчи до N-го.
def fibonachi(do):
    a = 0
    b = 1
    for j in range(do):
        yield b
        a, b = b, a+b

print('Введите номер числа Фибоначчи N:')
do = int(input())
for i in fibonachi(do):
    print(i)