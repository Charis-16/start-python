import random
number = random.randint(1,100)
guess = 0
print("Guess a number betwwen 1-100")

while guess!= number:
    guess= int(input("Enter your guess:"))
    if guess<number:
        print("too low")
    elif guess>number:
        print("too high")
    else:
        print("YOU GOT IT !")