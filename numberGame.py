import random

number = random.randint(1,9)
chances = 5

while chances > 0:
    plrNum = int(input("Enter your number"))

    if plrNum == number:
        print("You guessed correctly!!!!!!!!!!!!!")
        break
    elif plrNum > number:
        print("The number is lower")
    elif plrNum < number:
        print("The number is greater")

    chances = chances - 1

if chances == 0:
    print("You lost!!!!! (how)")