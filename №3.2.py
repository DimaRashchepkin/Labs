from math import gcd


def nod(x, y):
    res = 1
    for i in range(1, min(abs(x), abs(y)) + 1):
        if x % i == 0 and y % i == 0:
            res = i
    return res


print('Введите два числа:')
try:
    a = int(input())
    b = int(input())
except ValueError:
    print('Данные неверны')
    exit(0)

print("Наибольший общий делитель по написанной функции:", nod(a, b))
print("Наибольший общий делитель по встроенной функции:", gcd(a, b))
