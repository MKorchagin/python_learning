from typing import Any

import numpy as np
from statistics import mean

# creating random list
lst = list(np.random.randint(0, 1000, 100))
print('random list:', lst)

# sort list from min to max(without using sort()). Method from Google

for run in range(len(lst) - 1):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
print('\nsorted list:', lst)

# calculate average for even and odd numbers, for calculating average use operator mean(list)
even = [k for k in lst if k % 2 == 0]
odd = [k for k in lst if k % 2 != 0]
print('\neven:', even, '\navg even:', mean(even))
print('\nodd:', odd, '\nacg odd:', mean(odd))
