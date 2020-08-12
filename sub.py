x = int(input("Enter your first no.: "))
y = int(input("Enter your second no.: "))
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

print("Difference of x and y is: ", sub(x,y))
