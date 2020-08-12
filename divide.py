def divide(x, y):
    return x / y
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if (num2 == 0):
    print 'Not possible'
else:
    print 'Result: ',divide(num1, num2)
