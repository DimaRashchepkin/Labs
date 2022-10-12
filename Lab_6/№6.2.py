A = [[3, -4, 5],
     [2, -3, 1],
     [3, -5, -1]]

B = [[3, 29],
     [2, 18],
     [0, -3]]

res = []
for i in range(len(A)):
    res.append([])
    for j in range(len(B[0])):
        res[i].append(0)

for i in range(len(A)):
    for j in range(len(B[0])):
        value = 0
        for k in range(len(A[0])):
            value += A[i][k] * B[k][j]
        res[i][j] = value

print(res)
