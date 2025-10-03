import random as rand

randInt  = int(rand.randint(1, 100))

guess = int(input("Guess the number I think: "))

while guess != randInt:
    if guess < randInt:
        print("Try bigger")
    else:
        print("Try less")
    guess = int(input("Guess the number I think: "))

print("Yes, you are right!")