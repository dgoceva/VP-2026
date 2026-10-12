a,b = 0,1
while a < 100:
    print(a, end=' ')
    a,b = b,a+b
print()

a,b = 0,1
for _ in range(10):
    print(a, end=' ')
    a,b = b,a+b
print()

a,b = 0,1
fib = []
while a < 100:
    fib.append(a)
    a,b = b,a+b
print(fib)

a,b = 0,1
fib = []
for _ in range(10):
    fib.append(a)
    a,b = b,a+b
print(fib)

import math

print(round(math.sin(30/180*math.pi),2))