lst = [1, 0, 2, 3, 5]
res = 0
cntr = 0
for x in lst:
    if x == 0:
        cntr += 1
    else:
        if cntr > res:
            res = cntr
        cntr = 0
print(res)
