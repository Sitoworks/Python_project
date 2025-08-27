# Print a welcome message
print("Welcome to Sitoworks Calculator")
# Ask the user to enter a number 
first_number = input("Enter a number: ")

while not first_number.isnumeric():
    first_number = input("Please enter a valid number: ")
    
# Ask the user to choose an operator
operator = input("Choose an operator (+, -, *, and /)")
while operator not in ["+", "-", "*", "/"]:
    operator = input("Please enter a valid operator (+, -, *, and /): ")
# Ask the user to enter another number
second_number = input("Enter another number: ")
while not second_number.isnumeric():
    second_number = input("Please enter a valid number: ")

first_number = float(first_number)
second_number = float(second_number)

# Print the result
if operator == "+":
    result = first_number + second_number

elif operator == "-":
    result = first_number - second_number

elif operator == "*":
    result = first_number * second_number

elif operator == "/":
    result = first_number / second_number

print(result)