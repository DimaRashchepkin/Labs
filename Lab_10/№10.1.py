import random
from datetime import datetime, timedelta


def my_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i > j:
                if lst[i] < lst[j]:
                    lst[j], lst[i] = lst[i], lst[j]
            elif j > i:
                if lst[i] > lst[j]:
                    lst[j], lst[i] = lst[i], lst[j]
    return lst


results_myf = timedelta(0)
results_std = timedelta(0)
iters = 100
for k in range(iters):
    data = [random.randint(1, 1000) for i in range(1000)]

    start_time = datetime.now()
    std_sort = sorted(data)
    results_std += datetime.now() - start_time

    start_time = datetime.now()
    myf_sort = my_sort(data)
    results_myf += datetime.now() - start_time

print(results_myf / iters)
print(results_std / iters)
