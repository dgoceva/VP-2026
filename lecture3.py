
def fibLimit(limit: int) -> None: 
    a,b = 0,1
    while a < limit:
        print(a, end=' ')
        a,b = b,a+b
    print()

def fibLimit1(limit: int) -> int: 
    a,b = 0,1
    while a < limit and b < limit:
        a,b = b,a+b
    return a
def fibMembers(N:int)->None:
    a,b = 0,1
    for _ in range(N):
        print(a, end=' ')
        a,b = b,a+b
    print()    

def fibLimitList(limit: int =50) -> list:
    a,b = 0,1
    fib = []
    while a < limit:
        fib.append(a)
        a,b = b,a+b
    return fib

def addElement(element: float, result: list = []) -> list:
    result.append(element)
    return result

def addElement1(element: float, result: list = None) -> list:
    if result == None:
        result = []
    result.append(element)
    return result

if __name__ == "__main__":
    print(fibLimit)
    print(fibLimit(10))
    fibLimit(100)
    print(fibLimit1(100))
    fibMembers(20)
    print(fibLimitList())
    print(fibLimitList(150))
    print(addElement(3.4))
    print(addElement(44.2))
    print(addElement(21.))
    print(addElement(10.7,[11,21,31]))

    print(addElement1(3.4))
    print(addElement1(44.2))
    print(addElement1(21.))
    print(addElement1(11.5,[1,2,3]))
