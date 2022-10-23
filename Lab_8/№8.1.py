data = {'Иванов': 20, 'Сидоров': 68, 'Петров': 26, 'Смирнов': 68, 'Васин': 54, 'Дубов': 38, 'Летов': 19}
marks = data.values()
mn = min(marks)
mid = sum(marks) / len(marks)
mx = max(marks)

for key in data:
    if data[key] > mid:
        print(key)

print()
print(mn, round(mid, 2), mx, '\n')

for key in data:
    if data[key] == mn:
        print(key, data[key])
    if data[key] == mx:
        print(key, data[key])
