lst = [3, -4, 5, 2, -3, 1, 3, -5, -1, 5]
lst = sorted(lst)
moda = 1
modas = []

tmp_elem = lst[0]
for i in range(1, len(lst)):
    if lst[i] == tmp_elem:
        moda += 1
        tmp_elem = lst[i]
    else:
        modas.append(moda)
        moda = 1
        tmp_elem = lst[i]
modas.append(moda)

if lst.count(lst.index(max(lst))) == 1:
    print('Мода:', max(lst))
else:
    print('Мода не существует')
