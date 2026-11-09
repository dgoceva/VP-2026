import statistics

import numpy as np

import utils.fibo

n = int(input('Input N:'))
print(utils.fibo.fib1(n))

data = [int(x) for x in input("data:").split()]
print(data)
print(statistics.mean(data), statistics.median(data))

print(np.average(data), np.mean(data), np.median(data))