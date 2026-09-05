# Make a MINI Calculator 
num1 = float(input("Enter the first Number: "))
num2 = float(input("Enter the second Number: "))
symbol = input("Select Operator (+, -, *, %, **): ") 

if symbol == "+":
    print(num1 + num2)
elif symbol == "-":
    print(num1 - num2)
elif symbol == "*":
    print(num1 * num2)
elif symbol == "%":
    print(num1 % num2)
elif symbol == "**":
    print(num1 ** num2)
else:
    print("INVALID OPERATOR")