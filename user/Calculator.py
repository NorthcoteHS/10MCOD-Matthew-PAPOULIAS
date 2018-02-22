import sys

# Get the first numbers
firstNum = int(input("Enter the first number: "))
# Get the operation
operation = input("Enter the operation: ")
# Get the second number
secondNum = int(input("Enter the second number: "))
# Create the answer variable
answer = 0
# Go through the operations and evaluate them
if operation == "+":
	answer = firstNum + secondNum
elif operation == "-":
	answer = firstNum - secondNum
elif operation == "*":
	answer = firstNum * secondNum
elif operation == "/":
	answer = firstNum / secondNum
else:
	print("Incorrect operation")
	sys.exit(0)

# Print the answer
print(answer)