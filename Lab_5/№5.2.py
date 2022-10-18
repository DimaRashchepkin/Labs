import re


string = input('Введите строку: ').strip().capitalize()

end = None
for i in range(1, len(string)):
    res = re.findall(r"[^a-z ]", string[-i])
    if res:
        end = len(string) - i
    else:
        break
if end:
    string = string[:end] + "."
else:
    string += '.'

print(string)
