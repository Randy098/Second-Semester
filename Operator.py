Choices = ("+, -, /, *")
operator = input("enter operator: ")
num1 = input("enter first number: ")
num2 = input("enter second number: ")

if Choices == "+":
    result = num1 + num2
    print(result)

elif Choices == "-":
    result = num1 - num2
    print(result)

elif Choices == "/":
    result = num1 / num2
    print(result)

elif Choices == "*":
    result = num1 * num2
    print(result)
else:
    print("Error! Invalid Operator")