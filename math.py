#Get user input for first number
num1 = float(input("Enter the first number:"))

#Get user input for second number
num2 = float(input("Enter the second number:"))

#Get user input for operation
operation = input("Enter the mathematical operation(+,-,*./):")

if operation == "+":
   result = num1 + num2
elif operation == "-":
     result = num1 - num2
elif operation == "*":
     result = num1 * num2
elif operation == "/":
    if num2 == 0:
        result = "Undefined"
    else:
        result = num1 / num2
else:
    result = "Invalid operation"

#Print result
print("The result is:",result)

