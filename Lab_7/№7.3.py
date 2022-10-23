first_str = set(input('Введите числа первого набора: ').split())
sec_str = set(input('Введите числа второго набора: ').split())
for num in first_str & sec_str:
    print(num)
