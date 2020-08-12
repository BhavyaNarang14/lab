print("""
For add press '1'
For sub press '2'
For mul press '3'
For div press '4'
""")

i = int(input("enter your choice:"))
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
def add(x,y):
    sum = x + y
    return sum
def sub(x,y):
    
    if x>y:
        z = x-y
        return z
    elif y>x:
        z = y-x
        return z
    else:
        z = 0
        return z
def mul(x,y):
    z = x*y
    return z
def divide(x, y):
    if (y == 0):
        print ('Not possible')
    return x / y

if i==1:
    print(add(x,y))
elif i==2:
    print(sub(x,y))
elif i==3:
    print(mul(x,y))
elif i==4:
    div = divide(x,y)
    print(div)
else:
    print("numbers not valid")

