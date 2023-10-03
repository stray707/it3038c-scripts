import random

secret = random.randint(1, 100)
guess = None
while guess != secret:
    guess = int(input("Guess the number between 1 and 100: "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
print(f"Congratulations! %s is the correct guess." % (secret))
