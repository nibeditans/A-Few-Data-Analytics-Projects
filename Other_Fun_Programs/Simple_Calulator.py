num1 = int(input("Enter your first number: "))
Operator = input("Which operator you want to use?\nChoose one (+, -, *, /, %, **):")
num2 = int(input("Enter your second number: "))


if Operator=='+':
    print(num1+num2)
elif Operator=='-':
    print(num1-num2)
elif Operator=='*':
    print(num1*num2)
elif Operator=='/':
    print(num1/num2)
elif Operator=='%':
    print(num1%num2)
elif Operator=='**':
    print(num1**num2)
else:
    print("Invalid Operator!")
