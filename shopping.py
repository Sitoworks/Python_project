item = input("what item would you like to shop today?: ")
price = float(input("what is the price of each item?: "))
quantity = int(input("How many would you be going for? "))
Total = price * quantity
name = input("what is your name? ")
print(f"Hello {name} you have bought ${Total} worth of {item} today!")