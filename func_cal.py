# Step 1: Define functions
def add(x, y):
    return x + y
  
def subtract(x, y):
    return x - y

def multiply(x, y):
    
    return x * y
    
def divide(x, y):
   return x / y
  
# Step 2: Ask user to choose operation
def get_operator():
    operators = ["+", "-", "*", "/"]
    while True:
        op = input("Choose an operator (+, -, *, /): ")
        if op in operators:
            return op
        print("Please enter a valid operator (+, -, *, /).")

# Step 3: Ask for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = get_operator()

# Step 4: Call the right function and print result
if operator == '+':
    print("Result:", add(num1, num2))
elif operator == '-':
    print("Result:", subtract(num1, num2))
elif operator == '*':
    print("Result:", multiply(num1, num2))
elif operator == '/':
    print("Result:", divide(num1, num2))
else:
    print("Invalid operator, please try again.")

