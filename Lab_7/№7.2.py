first_str = set(input('Введите первую строку: '))
sec_str = set(input('Введите вторую строку: '))
res = first_str - sec_str
for sym in res:
    print(sym)
