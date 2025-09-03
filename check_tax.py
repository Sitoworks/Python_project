price = float(input(f" what is the value of your purchase? "))

if price >= 1.00:
    tax = 0.07
else:
    tax = 0
print(f'your tax rate is {tax} dollar')
