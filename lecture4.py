def sumList(*args):
    return sum(args)

l1 = list(range(1,6,3))
print(l1)
l = list(range(*l1))
print(l)
# l = list(range(l1))
# print(l)

print(sumList(1,2,3,4,5))
print(sumList(1,3,4))
print(sumList([1,2,3,4,5]))