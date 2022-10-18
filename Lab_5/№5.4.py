import re


string = input('Введите автомобильный номер: ')
if re.search(r'[a-zA-Z]{2}[0-9]{3}[a-zA-z]', string):
    print('Номер допустим')
else:
    print('Номер недопустим')
