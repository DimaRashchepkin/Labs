import re


string = input('Введите строку: ')

start = 0
end = -1
for i in range(len(string)):
    if string[i] != ' ':
        start = i
        break
for i in range(1, len(string)):
    if string[-i] != ' ':
        end = len(string) - i
        break
string = string[start:end + 1]
string = string[0].upper() + string[1:].lower()

end = -1
for i in range(1, len(string)):
    res = re.findall(r"[^a-z ]", string[-i])
    if res:
        end = len(string) - i
    else:
        break
string = string[:end] + "."

print(string)
