import math


print('Введите значение угла в градусах:')
try:
    value = float(input())
except ValueError:
    print('Данные неверны')
    exit(0)
trig = math.radians(value)

sn = round(math.sin(trig), 3)
if value == 270:
    cs = 0.0
else:
    cs = round(math.cos(trig), 3)
if sn == 0:
    tg = 0
elif cs == 0:
    tg = "Не существует"
else:
    tg = round(math.tan(trig), 3)

print("Синус:", sn)
print("Косинус:", cs)
print("Тангенс:", tg)
