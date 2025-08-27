def add_two_numbers():
    x = input("Enter the value of X: ")
    y = input("Enter a value for Y: ")
    name = input("What is your name: ?")
    print(f"Addition: {x + y}")
    print(f"My name is {name}")


add_two_numbers()

def new_func(add_two_numbers):
    x = 20 
    print(f"X is {x}")
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    username = input("What is your name?: ")
    add_two_numbers(x, name=username, y=second_number)
    add_two_numbers(x, name=username, y=second_number)
    add_two_numbers(x, name=username, y=second_number)
    add_two_numbers(x, name=username, y=second_number)
    add_two_numbers(x, name=username, y=second_number)
    add_two_numbers(x, name=username, y=second_number)
    return x

x = new_func(add_two_numbers)


# Variable scopes

# Scope Resolutions
def first_function():
    x = 30  # Local Variable
    print(x)

def second_function():
    # x = 20
    print(x)

x = 10   # Global Variable

# first_function(x)
# second_function()


def p_func():
    x = 20   # Enclosed Variable
    def c_func():
        print(x)
    # c_func()

p_func()

# Read about this

def main():
    pass

# if __name___ == "__main__":
#     main()