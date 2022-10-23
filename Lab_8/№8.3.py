data = {'кот': 'cat', 'собака': 'dog', 'дерево': 'tree', 'дом': 'house', 'дорога': 'road', 'лес': 'forest', 'книга': 'book'}
words = input('').lower().split()
for word in words:
    print(data[word], end=' ')
