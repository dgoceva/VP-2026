
def fib1(n):
    a,b = 0,1
    fib = []
    for _ in range(n):
        fib.append(a)
        a,b = b,a+b
    return fib

def fib2(limit=100):
    a,b = 0,1
    fib = []
    while a < limit:
        fib.append(a)
        a,b = b,a+b
    return fib

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
       n = 10
    else:
       n = int(sys.argv[1])
    print(fib1(n))
    print(fib2())