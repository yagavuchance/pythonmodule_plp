# Calculator 
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
symbol = input("Enter any symbol (+, -, *, /): ")

if symbol == "+":
    print("The answer is: " + str(x + y))

elif symbol == "-":
    print("The answer is: " + str(x - y))

elif symbol == "*":
    print("The answer is: " + str(x * y))

elif symbol == "/":
    if y != 0:
        print("The answer is: " + str(x / y))
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Error: Invalid symbol.")





