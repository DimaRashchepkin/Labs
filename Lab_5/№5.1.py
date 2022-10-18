check_symbols = ['<', '>', '/', '\\', '|', '', '']
formats = ('.txt', '.doc', '.docx', '.odt', '.rtf')
print("Вводите названия файлов: ")
string = input()
while string:
    if string.endswith(formats):
        for sym in string:
            if sym in check_symbols:
                print('No')
                string = input()
                continue
        print('Yes')
    else:
        print('No')
    string = input()
