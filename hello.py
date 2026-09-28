

print("Hello")
print(3/5,3//5,3%5)
print(3+5,3-5,3*5)
print(4./2,4.5*2.3,4.1+2.2,3.1-4.5)


# variables
x = int(input('x='))
y = float(input("y="))
print(x+y)

"""
x       y       x and y     x or y      not y
False   False   False       False       True
False   True    False       True        False
True    False   False       True
True    True    True        True
"""
print(x<y,x>=y,x==y,x!=y)

s = input()
print(len(s),s)
print(s[0],s[-1])
print(s[:],s[3:],s[:3],s[2:4],sep="\n")
print(s.capitalize(),s.lower(),s.upper(),sep="#")