from math import sqrt
from matplotlib import pyplot as pp
import numpy as np


X = [10, 12, 14, 20, 13, 35, 65, 5, 0, 13]

sum_ = sum(X)
len_ = len(X)
mean = sum_ / len_ if sum_ > 0 and len_ > 0 else 0
standard_deviasion = sqrt(sum([(x**2 - 2 * (x * mean) + mean**2) for x in X]) / len_)

print("mean:", mean)
print("standard_deviasion:", standard_deviasion)
print()


def normalize(n:int) -> float:
    if standard_deviasion == 0:
        return .0
    return (n - mean) / standard_deviasion


fig = pp.figure()
ax = fig.add_subplot()
ax.grid(True)
ax.set_ylim(-1.2, 1.2)
Y = []

for n in X:
    normed = normalize(n)
    Y.append(normed)

print(Y)

ax.plot(X, Y, marker='o', linestyle='', color='red', label='Normalized X Data')




