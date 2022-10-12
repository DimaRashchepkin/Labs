print('Введите строку:')
# string = input().split()
string = "Такой сигнал рукой, подаваемый водителем легкового автомобиля, информирует Вас:"
cnt_elems = ['.', ',', ':', ';', '!', '?']
cntr_upper = 0
cntr_elems = 0

for x in string:
    if x[0].isupper():
        cntr_upper += 1
    if x[-1] in cnt_elems:
        cntr_elems += 1

print('Количество слов, начинающихся с заглавной буквы: ', cntr_upper)
print('Количество слов, оканчивающихся знаком препинания из списка: ', cntr_elems)
