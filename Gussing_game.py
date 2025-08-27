import random

print("welcome to SItoworks random Guessing game!")
n = int(input("input a number betwem 1,and : "))
secretNumber = random.randint(1, n)
attempts = 0

while True:
    Guess = int(input("Guess a number: "))
    while type(Guess) is not int: 
        print("You have entered a wrong input! Kindly enter a integer number: ")

    attempts += 1
    if Guess == secretNumber:
        print(f"Congratulations! You have guessed the correct number in {attempts} attempts")
        break
    elif Guess < secretNumber:
        print("Sitoworks: Try a higher number!")
    else:
        print("Sitoworks: Try a Lower number")
