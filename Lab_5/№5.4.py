import re


string = input('Введите автомобильный номер: ')
if len(string) == 6:
    if re.search(r'[a-zA-Z]', string[0]):
        if re.search(r'[a-zA-Z]', string[1]):
            if re.search(r'[0-9]', string[2]):
                if re.search(r'[0-9]', string[3]):
                    if re.search(r'[0-9]', string[4]):
                        if re.search(r'[a-zA-Z]', string[5]):
                            print('Номер допустим')
                            exit(0)
print('Номер недопустим')
