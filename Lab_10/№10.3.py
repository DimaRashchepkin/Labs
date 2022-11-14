from operator import itemgetter


f = open('people.txt', 'r')
num = len(f.readlines())
f.close()
f = open('people.txt', 'r')
data = []
for i in range(num):
    data.append(tuple(f.readline().split()))
print(sorted(data, key=itemgetter(0, 1)))