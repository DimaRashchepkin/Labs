def count_a(string):
    return string.count('а')


f = open('data.txt', 'r')
lst = f.read().split('\n')
lst.sort(key=count_a, reverse=True)
print(*lst)
