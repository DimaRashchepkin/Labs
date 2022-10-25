data = {'кот': 'cat', 'собака': 'dog', 'дерево': 'tree', 'дом': 'house', 'дорога': 'road', 'лес': 'forest', 'книга': 'book'}
words = input('').lower().split()
new_word = 0
res = ""
for word in words:
    if word in data:
        res += data[word] + " "
    else:
        new_word += 1
if new_word:
    print("К сожалению,", new_word, "слов из введенных вами пока нет в словаре")
print("Результат:")
print(res[:-1].capitalize())
