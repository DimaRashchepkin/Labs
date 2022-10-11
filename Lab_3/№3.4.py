import datetime

try:
    print('Введите дату рождения в формате ДД/ММ/ГГГГ:')
    date = [int(x) for x in input().split('/')]
    birthday = datetime.date(date[2], date[1], date[0])
except ValueError:
    print("Данные неверны")
    exit(0)

interval1 = datetime.timedelta(days=10000)
interval2 = datetime.timedelta(minutes=1000000)
interval3 = datetime.timedelta(seconds=1000000000)

print(birthday + interval1)
print(birthday + interval2)
print(birthday + interval3)
