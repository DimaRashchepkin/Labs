from datetime import datetime

try:
    print('Введите время отправления в формате ДД/ММ/ГГ ЧЧ:MM:')
    away = datetime.strptime(input(), '%d/%m/%y %H:%M')
    print('Введите время прибытия в формате ДД/ММ/ГГ ЧЧ:MM:')
    to = datetime.strptime(input(), '%d/%m/%y %H:%M')
except ValueError:
    print("Данные неверны")
    exit(0)

if to > away:
    print(to - away)
else:
    print("Данные неверны")
