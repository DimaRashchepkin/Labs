lst = [3, -4, 2, -3, 1, -5, -1, 5, 5]
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

mx = max(lst)
mx_id = lst.index(mx)
if lst.count(modas[mx_id]) == 1:
    print('Мода:', max(lst))
else:
    print('Мода не существует')
