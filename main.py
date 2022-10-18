formats = ('.txt', '.doc', '.docx', '.odt', '.rtf')
while True:
    string = input()
    if string.endswith(formats):
        print(1)
    else:
        print(0)

