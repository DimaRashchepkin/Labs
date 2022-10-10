check_symbols = ['<', '>', '/', '\\', '''|''', '', '']
formats = ['.txt', '.doc', '.docx', '.odt', '.rtf']
print("Вводите названия файлов: ")
string = input()
while string:
    flag = 1
    if string[-4:] in formats:
        for sym in string:
            if sym in check_symbols:
                print('Не может быть названием файла\n')
                flag = 0
                break
        if flag:
            print('Название подходит\n')
    else:
        print('Не может быть названием файла\n')
    string = input()
