def get_number(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number.")

def get_operator():
    operators = ["+", "-", "*", "/"]
    while True:
        op = input("Choose an operator (+, -, *, /): ")
        if op in operators:
            return op
        print("Please enter a valid operator (+, -, *, /).")

def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Error: Division by zero."
        return a / b

def main():
    print("Welcome to Sitoworks Calculator")
    a = get_number("Enter a number: ")
    operator = get_operator()
    b = get_number("Enter another number: ")
    result = calculate(a, b, operator)
    print("Result:", result)


  
if __name__ == "__main__":
    main()
