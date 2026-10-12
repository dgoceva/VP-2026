import cmath

def addComplex(a: complex,b: complex) -> complex:
    return a+b

def solveSquare(a: float, b: float, c: float) -> list:
    if a == 0:
        if b == 0:
          return ["Error"]
        return [-c/b]
    d = cmath.sqrt(b**2-4*a*c)
    return [(-b-d)/(2*a),(-b+d)/(2*a)]

def funcPosOnly(a,b,/):
    return(a+b)
def funcKeyOnly(*,a,b):
    return a+b

if __name__ == "__main__":
    x = complex()
    print(x)
    x = complex(3,4)
    print(x)
    y = complex(4,2)
    print(y)
    print(addComplex(x,y))
    print(x-y,x*y,x/y)

    x = float(input("a="))
    y = float(input("b="))
    z = float(input("c="))
    print(solveSquare(a=x,b=y,c=z))    
    print(solveSquare(x,y,z))
    print(solveSquare(x,b=y,c=z))
    print(funcKeyOnly(a=3,b=12))
    print(funcPosOnly(12,3))
    # print(funcKeyOnly(12,b=3))